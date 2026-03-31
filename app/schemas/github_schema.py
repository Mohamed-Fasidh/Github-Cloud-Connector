from pydantic import BaseModel

class RepoRequest(BaseModel):
    username: str

class IssueCreateRequest(BaseModel):
    owner: str
    repo: str
    title: str
    body: str

class IssueListRequest(BaseModel):
    owner: str
    repo: str

class CommitRequest(BaseModel):
    owner: str
    repo: str

class PullRequestCreate(BaseModel):
    owner: str
    repo: str
    title: str
    head: str   # feature branch
    base: str   # main branch
    body: str