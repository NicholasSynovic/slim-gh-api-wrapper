from datetime import datetime

from requests import Response, get


def setHeaders(token: str | None = None) -> dict[str, str]:
    if token is None:
        return {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "nsynovic/slim-gh-api-wrapper",
        }
    else:
        return {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "nsynovic/slim-gh-api-wrapper",
            "Authorization": f"Bearer {token}",
        }


class PersonalAccessToken:
    def __init__(self, token: str | None = None) -> None:
        self.token: str | None = token
        self.headers: dict[str, str] = setHeaders(token=self.token)

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

    def setRateLimits(self) -> None:
        resp: Response = get(
            url="https://api.github.com/rate_limit",
            headers=self.headers,
        )

        json: dict = resp.json()

        coreResources: dict = json["resources"]["core"]
        graphQLResources: dict = json["resources"]["graphql"]
        imResources: dict = json["resources"]["integration_manifest"]
        searchResources: dict = json["resources"]["search"]

        self.core["limit"] = coreResources["limit"]
        self.core["remaining"] = coreResources["remaining"]
        self.core["used"] = coreResources["used"]
        self.core["reset"] = datetime.fromtimestamp(coreResources["reset"])

        # TODO: Add support for graphql, IM, and search endpoints
