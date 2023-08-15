from fastapi import FastAPI
from routes.user import user


app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags= [{
        "name": "users",
        "description": "users soutes"
    }],
)

app.include_router(user)