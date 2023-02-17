from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from .api.router import api_router
from .core.response import APIResponse
from .graphql.schema import schema

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.include_router(api_router, prefix="/api")


@app.get("/health")
def health() -> APIResponse:
    return APIResponse(message="OK")
