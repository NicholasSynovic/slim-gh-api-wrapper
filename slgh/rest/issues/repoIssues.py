from requests import Response, get

from slgh.pat import PersonalAccessToken


class RepoIssues:
    def __init__(self, owner: str, repo: str) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.endpoint: str = (
            f"https://api.github.com/repos/{self.owner}/{self.repo}/issues"
        )

    def updateEnpoint(self, owner: str, repo: str) -> None:
        self.owner: str = owner
        self.repo: str = repo
        self.endpoint: str = (
            f"https://api.github.com/repos/{self.owner}/{self.repo}/issues"
        )

    def getJSON(self, pat: PersonalAccessToken) -> None:
        get(url=self.endpoint, headers=pat.headers)
