from pathlib import Path
import sys
import pytest
from queue import PriorityQueue

INPUT_TXT = Path(__file__).parent.resolve() / "input.txt"

INPUT_S = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
EXPECTED = 29


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test_case(input_s: str, expected: int) -> None:
    assert solution(input_s) == expected


def distance(row: int, col: int, end_row: int, end_col: int) -> int:
    # Manhattan distance
    return abs(row - end_row) + abs(col - end_col)


def check_in_grid(row: int, col: int, width: int, height: int) -> bool:
    return row >= 0 and col >= 0 and row < height and col < width


def solution(s: str) -> int:
    grid = []
    starting = []
    end = None
    for i, line in enumerate(s.splitlines()):
        row = []
        for j, c in enumerate(line):
            if c == "S" or c == "a":
                row.append(ord("a"))
                starting.append((i, j))
            elif c == "E":
                row.append(ord("z"))
                end = (i, j)
            else:
                row.append(ord(c))
        grid.append(row)

    height = len(grid)
    width = len(grid[0])

    best = sys.maxsize
    neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    unreachable = set()  # Track which points are unable to find a solution
    print(f"Searching {len(starting)} starting positions")
    for start_index, start in enumerate(starting):
        visited: set[tuple[int, int]] = set()
        # down, up, right, left
        q = PriorityQueue()
        initial_distance = distance(start[0], start[1], end[0], end[1])
        initial_priority = (0, initial_distance, 0)
        q.put_nowait((initial_priority, start))
        solution_found = False
        while not q.empty():
            item = q.get_nowait()
            (cost_to_node, heuristic, steps), node = item
            visited.add(node)
            row, col = node
            if node == end:
                solution_found = True
                best = min(best, steps)
                break

            for direction in neighbours:
                neighbour = row + direction[0], col + direction[1]
                x, y = neighbour

                # Not in grid
                if not check_in_grid(x, y, width, height):
                    continue

                # Limit at most one elevation higher
                if grid[x][y] - grid[row][col] > 1:
                    continue

                if neighbour in visited:
                    continue

                # f = g + h
                steps_to_node = steps + 1
                distance_to_end = distance(x, y, end[0], end[1])  # h
                cost = steps_to_node + distance_to_end
                priority = (cost, distance_to_end, steps_to_node)
                q.put_nowait((priority, neighbour))

        print(
            f"Finished searching position {start_index}. {'Solution found ' + str(steps) + ' steps' if solution_found else 'No solution found'}"
        )

    return best


def main() -> int:
    with open(INPUT_TXT) as f:
        s = f.read()
    print(solution(s))


if __name__ == "__main__":
    main()
