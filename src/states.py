from enum import Enum


class State(Enum):
    Start = 1
    NewQuestion = 2
    AnswerAndNewQuestion = 3
