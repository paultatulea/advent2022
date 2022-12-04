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


outcome_lookup = {
    "X": Outcome.LOSE,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN,
}

choice_lookup = {
    "A": Choice.ROCK,
    "B": Choice.PAPER,
    "C": Choice.SCISSORS,
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


def get_choice(opp: Choice, outcome: Outcome) -> Choice:
    if outcome == Outcome.DRAW:
        return opp
    if opp == Choice.ROCK:
        return Choice.PAPER if outcome == Outcome.WIN else Choice.SCISSORS
    if opp == Choice.PAPER:
        return Choice.SCISSORS if outcome == Outcome.WIN else Choice.ROCK
    if opp == Choice.SCISSORS:
        return Choice.ROCK if outcome == Outcome.WIN else Choice.PAPER


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
            opp, outcome = line.split()
            opp = Choice(choice_lookup[opp])
            outcome = Outcome(outcome_lookup[outcome])
            choice = get_choice(opp, outcome)
            choice_score = point_choice_lookup[choice]
            result_score = point_outcome_lookup[outcome]
            round_score = choice_score + result_score
            # print(f"{opp=} {choice=} {round_score=}")
            score += round_score
    print(f"{score=}")


solution()
