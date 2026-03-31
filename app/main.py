from fastapi import FastAPI
from app.routes.github_routes import router

app = FastAPI(title="GitHub Cloud Connector")

app.include_router(router)
