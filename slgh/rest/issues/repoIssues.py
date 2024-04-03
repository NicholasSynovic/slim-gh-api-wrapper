from string import Template
from typing import Tuple

from requests import Response, get

from slgh import buildHeaders
from slgh.pat import PersonalAccessToken


class RepositoryIssues:
    def __init__(self, owner: str, repo: str) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.page: int = 1

        self.endpointTemplate: Template = Template(
            template="https://api.github.com/repos/${owner}/${repo}/issues?state=all&direction=asc&per_page=100&page=${page}",
        )
        self.endpoint: str = self.endpointTemplate.substitute(
            owner=self.owner,
            repo=self.repo,
            page=self.page,
        )

    def updateEndpoint(self, owner: str, repo: str, page: int = 1) -> None:
        self.owner = owner
        self.repo = repo
        self.page = page

        self.endpoint: str = self.endpointTemplate.substitute(
            owner=self.owner,
            repo=self.repo,
            page=self.page,
        )

    def incrementPage(self) -> None:
        self.page += 1
        self.endpoint: str = self.endpointTemplate.substitute(
            owner=self.owner,
            repo=self.repo,
            page=self.page,
        )

    def getJSON(self, pat: PersonalAccessToken) -> Tuple[str, int, dict]:
        resp: Response = get(
            url=self.endpoint, headers=buildHeaders(token=pat.getToken())
        )
        statusCode: int = resp.status_code
        json: dict = resp.json()

        return (self.endpoint, statusCode, json)
