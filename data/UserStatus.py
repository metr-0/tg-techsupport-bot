from enum import Enum


class UserStatus(Enum):
    Blocked = -1
    WaitingName = 0
    WaitingCompanyName = 1
    WaitingQuestion = 2
