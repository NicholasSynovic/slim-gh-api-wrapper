from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Protocol


class ExceededRateLimitError(Exception):
    def __str__(self):
        return "No more tokens to use"


class PAT_Protocol(Protocol):
    token: str
    restLimits: dict[str, int | datetime]


class PAT_ABC(metaclass=ABCMeta):
    @abstractmethod
    def decrementRateLimit(self) -> None:
        ...

    @abstractmethod
    def resetRateLimit(self) -> None:
        """
        Reset token usage tracker "used" field to 0 and the number of availible
        calls to however many calls are remaining
        """
        ...

    @abstractmethod
    def getRateLimit(self) -> None:
        """
        Set the token usage tracker "calls" field to the maximum number of calls
        availible and the "used" field to the number of calls used
        """
        ...
