from pathlib import Path


PATH = Path(__file__).parent.resolve() / "input.txt"

test = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def overlap(s1: int, e1: int, s2: int, e2: int) -> bool:
    return (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)


def solution(lines: list[str]):
    count = 0
    for line in lines:
        first, second = line.split(",")
        print(f"{first=} {second=}", end=" ")
        first_start, first_end = map(int, first.split("-"))
        second_start, second_end = map(int, second.split("-"))

        if overlap(first_start, first_end, second_start, second_end):
            print("TRUE", end="")
            count += 1
        print("")

    print(f"Overlap count: {count}")


def main():
    with open(PATH) as f:
        lines = f.readlines()
    solution((line.strip() for line in lines))


if __name__ == "__main__":
    main()
