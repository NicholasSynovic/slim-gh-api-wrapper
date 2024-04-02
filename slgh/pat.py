from datetime import datetime

from requests import Response, get


class PersonalAccessToken:
    def __init__(self, pat: str | None = None) -> None:
        self.pat: str | None = pat

        baseDict: dict[str, int | datetime] = {
            "limit": 0,
            "remaining": 0,
            "used": 0,
            "reset": datetime.now(),
        }

        # For core API endpoints
        self.core = baseDict

        # For GraphQL API endpoints
        self.graphql = baseDict

        # For Integration Manifest API endpoints
        self.im = baseDict

        # For Search API endpoints
        self.im = baseDict

    def testPAT(self) -> None:
        resp: Response = get(url="https://api.github.com/rate_limit")
        json: dict = resp.json()

        coreResources: dict = json["resources"]["core"]
        graphQLResources: dict = json["resources"]["graphql"]
        imResources: dict = json["resources"]["integration_manifest"]
        searchResources: dict = json["resources"]["search"]

        self.core["limit"] = coreResources["limit"]
        self.core["remaining"] = coreResources["remaining"]
        self.core["used"] = coreResources["used"]
        self.core["reset"] = datetime.fromtimestamp(coreResources["reset"])
