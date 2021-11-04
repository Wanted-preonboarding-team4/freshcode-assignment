import uvicorn
from fastapi import FastAPI


def create_app():

    app = FastAPI()

    @app.get("/")
    def hello_fastapi():
        return "hello_fastapi"

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)