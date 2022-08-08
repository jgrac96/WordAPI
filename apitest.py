# James Grace from https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/
# from https://www.educative.io/blog/python-fastapi-tutorial

from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Test API",
    openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "Hello, World"}


@api_router.get("/testing/")
def read_testing(name: str):
    return {"hi": name}


app.include_router(api_router)

if __name__  == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")