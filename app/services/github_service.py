import requests
from fastapi import HTTPException
from app.config import HEADERS

BASE_URL = "https://api.github.com"


def get_repos(username: str):
    url = f"{BASE_URL}/users/{username}/repos"

    try:
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )

        repos = response.json()

        # Clean response (important)
        return [
            {
                "name": repo["name"],
                "url": repo["html_url"],
                "private": repo["private"]
            }
            for repo in repos
        ]

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


def create_issue(owner: str, repo: str, title: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    try:
        response = requests.post(
            url,
            json={"title": title, "body": body},
            headers=HEADERS
        )

        if response.status_code not in [200, 201]:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )

        data = response.json()

        # Return only useful fields
        return {
            "title": data["title"],
            "state": data["state"],
            "url": data["html_url"]
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


def list_issues(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/issues"

    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )

        issues = response.json()

        # Clean response
        return [
            {
                "title": issue["title"],
                "state": issue["state"],
                "url": issue["html_url"]
            }
            for issue in issues
        ]

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/pulls"

    data = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }

    try:
        response = requests.post(url, json=data, headers=HEADERS)

        if response.status_code not in [200, 201]:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )

        pr = response.json()

        return {
            "title": pr["title"],
            "state": pr["state"],
            "url": pr["html_url"]
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_commits(owner: str, repo: str):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )

        commits = response.json()

        return [
            {
                "message": commit["commit"]["message"],
                "author": commit["commit"]["author"]["name"],
                "url": commit["html_url"]
            }
            for commit in commits[:10]  # limit
        ]

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))