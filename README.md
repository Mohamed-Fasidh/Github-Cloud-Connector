# GitHub Cloud Connector (FastAPI)

## Overview

This project is a GitHub Cloud Connector built using FastAPI. It integrates with GitHub REST APIs to perform operations such as fetching repositories, creating issues, listing issues, fetching commits, and creating pull requests.

The project demonstrates external API integration, secure authentication, clean backend architecture, and real-world Git workflows.

---

## Features

- Fetch repositories for a GitHub user  
- Create issues in a repository  
- List issues from a repository  
- Fetch recent commits from a repository  
- Create pull requests between branches  
- Secure authentication using GitHub Personal Access Token (PAT)  
- Clean and modular backend architecture  
- Optimized API responses (no raw GitHub payloads)  

---

## Tech Stack

- Python  
- FastAPI  
- Requests  
- Pydantic  

---

## Project Structure


app/
├── main.py
├── config.py
├── routes/
│ └── github_routes.py
├── services/
│ └── github_service.py
├── schemas/
│ └── github_schema.py


---

## Setup

### 1. Clone Repository


git clone https://github.com/Mohamed-Fasidh/AI-Market.git

cd AI-Market


### 2. Install Dependencies


pip install -r requirements.txt


### 3. Configure Environment Variables

Create a `.env` file:


GITHUB_TOKEN=your_personal_access_token


### 4. Run the Application


uvicorn app.main:app --reload


### 5. Access API Docs


http://127.0.0.1:8000/docs


---

## API Endpoints

### 1. Fetch Repositories

POST `/repos`

**Request:**
```json
{
  "username": "Mohamed-Fasidh"
}
```
Response:
``` json 
[
  {
    "name": "AI-Market",
    "url": "https://github.com/Mohamed-Fasidh/AI-Market",
    "private": false
  }
]
```
### 2. Create Issue

POST /create-issue

Request:
``` json 

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market",
  "title": "Test Issue from API",
  "body": "Created using FastAPI"
}
```
Response:
``` json 
{
  "title": "Test Issue from API",
  "state": "open",
  "url": "https://github.com/Mohamed-Fasidh/AI-Market/issues/1"
}
```
### 3. List Issues

POST /list-issues

Request:
``` json

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market"
}
```
Response:
``` json 
[
  {
    "title": "Test Issue from API",
    "state": "open",
    "url": "https://github.com/Mohamed-Fasidh/AI-Market/issues/1"
  }
]
```
### 4. Fetch Commits

POST /commits

Request:
``` json 

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market"
}
```
Response:
``` json 
[
  {
    "message": "Initial commit",
    "author": "Mohamed Fasidh",
    "url": "https://github.com/Mohamed-Fasidh/AI-Market/commit/..."
  }
]
```
### 5. Create Pull Request (Bonus)

POST /create-pr

Request:
``` json 

{
  "owner": "Mohamed-Fasidh",
  "repo": "AI-Market",
  "title": "New Feature PR",
  "head": "feature-branch",
  "base": "main",
  "body": "Adding new feature"
}
```
Response:
``` json 
{
  "title": "New Feature PR",
  "state": "open",
  "url": "https://github.com/Mohamed-Fasidh/AI-Market/pull/3"
}
```
## Security

-GitHub token stored in .env

-No hardcoded credentials

-Secure header handling

## Demo

-Issues created via API

-Pull requests created via API

-Verified in GitHub UI

-Tested using Swagger

## Challenges Faced

-JSON validation errors

-Git branch synchronization issues

-Pull request history mismatch

## Improvements (Future Scope)

-OAuth 2.0 authentication

-Async API using httpx

-Pagination support

-Rate limiting

## Conclusion

This project demonstrates backend engineering skills including API integration, authentication, structured design, error handling, and Git workflows using FastAPI.