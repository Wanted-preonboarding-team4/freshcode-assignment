import uvicorn
from fastapi import FastAPI
from app.database.conn import db
from view import auth_view, product
from common.config import conf
from dataclasses import asdict

def create_app():
    app = FastAPI()
    c = conf()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    app.include_router(auth_view.router)
    app.include_router(product.router)

    @app.get("/")
    def hello_fastapi():
        return "hello_fastapi"

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
