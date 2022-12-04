from enum import Enum
import io


class Choice(str, Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"


class Outcome(Enum):
    LOSE = -1
    DRAW = 0
    WIN = 1


choice_lookup = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
    "X": Choice.ROCK,
    "Y": Choice.PAPER,
    "Z": Choice.SCISSORS,
}

point_choice_lookup = {
    Choice.ROCK: 1,
    Choice.PAPER: 2,
    Choice.SCISSORS: 3,
}

point_outcome_lookup = {
    Outcome.LOSE: 0,
    Outcome.DRAW: 3,
    Outcome.WIN: 6,
}


def get_result(choice: Choice, other: Choice) -> Outcome:
    if choice == other:
        return Outcome.DRAW
    if choice == Choice.ROCK:
        return Outcome.WIN if other == Choice.SCISSORS else Outcome.LOSE
    if choice == Choice.PAPER:
        return Outcome.WIN if other == Choice.ROCK else Outcome.LOSE
    if choice == Choice.SCISSORS:
        return Outcome.WIN if other == Choice.PAPER else Outcome.LOSE


f = io.StringIO(
    """A Y
B X
C Z
"""
)


def solution():
    path = "day02/input.txt"
    score = 0
    with open(path) as f:
        for line in f:
            opp, me = line.split()
            opp = Choice(choice_lookup[opp])
            me = Choice(choice_lookup[me])
            choice_score = point_choice_lookup[me]
            result = get_result(me, opp)
            result_score = point_outcome_lookup[result]
            round_score = choice_score + result_score
            print(f"{opp=} {me=} {round_score=}")
            score += round_score
    print(f"{score=}")


solution()
