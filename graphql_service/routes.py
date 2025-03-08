from fastapi import APIRouter
from strawberry.fastapi import GraphQLRouter
from graphql_service.schema import schema

router = APIRouter()
router.include_router(GraphQLRouter(schema), prefix="/graphql")
