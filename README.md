## GitHub Cloud Connector (FastAPI)
# Overview

This project is a GitHub Cloud Connector built using FastAPI. It integrates with GitHub REST APIs to perform operations such as fetching repositories, creating issues, listing issues, fetching commits, and creating pull requests.

The project demonstrates external API integration, secure authentication, clean backend architecture, and real-world Git workflows.

## Features

Fetch repositories for a GitHub user
Create issues in a repository
List issues from a repository
Fetch recent commits from a repository
Create pull requests between branches
Secure authentication using GitHub Personal Access Token (PAT)
Clean and modular backend architecture
Optimized API responses (no raw GitHub payloads)

## Tech Stack

Python
FastAPI
Requests
Pydantic

## Project Structure

app/
 ├── main.py
 ├── config.py
 ├── routes/
 │    └── github_routes.py
 ├── services/
 │    └── github_service.py
 ├── schemas/
 │    └── github_schema.py

## Setup 

1. Clone Repository
git clone https://github.com/Mohamed-Fasidh/AI-Market.git
cd AI-Market
2. Install Dependencies
pip install -r requirements.txt
3. Configure Environment Variables

Create a .env file in the root directory:

GITHUB_TOKEN=your_personal_access_token
4. Run the Application
uvicorn app.main:app --reload
5. Access API Documentation
http://127.0.0.1:8000/docs

## API Endpoints

1. Fetch Repositories

POST /repos

Request:

{
  "username": "Mohamed-Fasidh"
}

Response:

[
  {
    "name": "AI-Market",
    "url": "https://github.com/...",
    "private": false
  }
]
2. Create Issue

POST /create-issue

Request:

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market",
  "title": "Test Issue from API",
  "body": "Created using FastAPI"
}

Response:

{
  "title": "Test Issue from API",
  "state": "open",
  "url": "https://github.com/..."
}
3. List Issues

POST /list-issues

Request:

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market"
}

Response:

[
  {
    "title": "Test Issue from API",
    "state": "open",
    "url": "https://github.com/..."
  }
]
4. Fetch Commits

POST /commits

Request:

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market"
}

Response:

[
  {
    "message": "commit message",
    "author": "author name",
    "url": "https://github.com/..."
  }
]
5. Create Pull Request (Bonus)

POST /create-pr

Request:

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market",
  "title": "New Feature PR",
  "head": "feature-branch",
  "base": "main",
  "body": "Adding new feature"
}

Response:

{
  "title": "New Feature PR",
  "state": "open",
  "url": "https://github.com/..."
}
## Security

GitHub Personal Access Token is stored in .env
No sensitive data is hardcoded
Headers handled securely
Demo
Successfully created issues via API
Successfully created pull requests via API
Verified real-time updates in GitHub UI
Tested using FastAPI Swagger UI

## Challenges Faced

JSON validation errors in request handling
Git branch synchronization issues
Pull request creation constraints (branch history mismatch)

## Improvements (Future Scope)

OAuth 2.0 authentication
Async API calls using httpx
Pagination support for large data
Rate limiting and retry mechanisms

## Conclusion

This project demonstrates backend engineering skills including API integration, authentication, structured code design, error handling, and real-world Git operations using FastAPI.