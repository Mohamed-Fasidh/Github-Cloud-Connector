from fastapi import APIRouter
from app.schemas.github_schema import RepoRequest, IssueCreateRequest, IssueListRequest,CommitRequest, PullRequestCreate
from app.services.github_service import get_repos, create_issue, list_issues,get_commits,create_pull_request

router = APIRouter()

@router.get("/")
def home():
    return {"message": "GitHub Connector API Running"}

@router.post("/repos")
def fetch_repos(request: RepoRequest):
    return get_repos(request.username)

@router.post("/create-issue")
def create_issue_api(request: IssueCreateRequest):
    return create_issue(request.owner, request.repo, request.title, request.body)

@router.post("/list-issues")
def list_issues_api(request: IssueListRequest):
    return list_issues(request.owner, request.repo)

@router.post("/commits")
def fetch_commits(request: CommitRequest):
    return get_commits(request.owner, request.repo)

@router.post("/create-pr")
def create_pr(request: PullRequestCreate):
    return create_pull_request(
        request.owner,
        request.repo,
        request.title,
        request.head,
        request.base,
        request.body
    )