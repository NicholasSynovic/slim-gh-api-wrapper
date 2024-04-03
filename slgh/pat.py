from datetime import datetime

from requests import Response, get

from slgh import buildHeaders
from slgh._classes.exceptions import *
from slgh._classes.pat import PAT_ABC


class PersonalAccessToken(PAT_ABC):
    def __init__(self, token: str) -> None:
        self.token: str = token
        self.restLimits: dict[str, int | datetime] = {
            "calls": 0,
            "used": 0,
            "reset": datetime.now(),
        }

    def decrementRateLimit(self) -> None:
        if self.restLimits["calls"] > 0:
            self.restLimits["calls"] = self.restLimits["calls"] - 1
            self.restLimits["used"] = self.restLimits["used"] + 1
        else:
            raise ExceededRateLimitError()

    def resetRateLimit(self) -> None:
        endpoint: str = "https://api.github.com/rate_limit"
        resp: Response = get(
            url=endpoint,
            headers=buildHeaders(token=self.token),
        )
        json: dict = resp.json()

        restLimits: dict[str, int] = json["resources"]["core"]
        self.restLimits["calls"] = restLimits["remaining"]
        self.restLimits["used"] = 0
        self.restLimits["reset"] = datetime.fromtimestamp(restLimits["reset"])

    def getRateLimit(self) -> None:
        endpoint: str = "https://api.github.com/rate_limit"
        resp: Response = get(
            url=endpoint,
            headers=buildHeaders(token=self.token),
        )
        json: dict = resp.json()

        restLimits: dict[str, int] = json["resources"]["core"]
        self.restLimits["calls"] = restLimits["limit"]
        self.restLimits["used"] = restLimits["used"]
        self.restLimits["reset"] = datetime.fromtimestamp(restLimits["reset"])
