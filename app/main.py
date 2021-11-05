import uvicorn
from fastapi import FastAPI
from database.conn import db
from view import auth_view, product_view
from common.config import conf
from dataclasses import asdict

description = """
# [Assignment 2] 프레시코드 과제


### 팀원 : 강대훈, 김훈태, 안다민, 이무현, 송빈호, 정성헌

"""

def create_app():
    app = FastAPI(title="Freshcode Restfull API",
                  description=description)
    c = conf()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    app.include_router(auth_view.router)
    app.include_router(product_view.router)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
