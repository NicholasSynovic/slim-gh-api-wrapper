def buildHeaders(token: str) -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "nsynovic/slgh",
        "Authorization": f"Bearer {token}",
    }
