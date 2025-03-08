from fastapi import FastAPI
from graphql_service.routes import router as graphql_router
import uvicorn

app = FastAPI()
app.include_router(graphql_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
