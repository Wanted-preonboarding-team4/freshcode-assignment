import asyncio
import os
from os import path
from typing import List

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from fastapi import FastAPI
from app.database.schema import Users
from app.main import create_app
from app.database.conn import db, Base
from app.service import login_user_if_not_found_user, create_user_if_not_found_email

"""
1. DB 생성
2. 테이블 생성
3. 테스트 코드 작동
4. 테이블 레코드 삭제 
"""

@pytest.fixture(scope="session")
def app():
    os.environ["API_ENV"] = "local"
    return create_app()


@pytest.fixture(scope="session")
def client(app):
    # Create tables
    Base.metadata.create_all(db.engine)
    return TestClient(app=app)


@pytest.fixture(scope="function", autouse=True)
def session():
    sess = next(db.session())
    yield sess
    # clear_all_table_data(
    #     session=sess,
    #     metadata=Base.metadata,
    #     except_tables=[]
    # )
    sess.rollback()



@pytest.fixture(scope="function")
def login(session):
    """
    테스트전 사용자 미리 등록
    :param session:
    :return:
    """
    db_user = Users.create(session=session, email="Hello@naver.com", password="123", user_type_id=1)
    session.commit()
    access_token = create_user_if_not_found_email(db_user, session)
    # access_token = create_access_token(data=UserToken.from_orm(db_user).dict(exclude={'pw', 'marketing_agree'}),)
    return dict(Authorization=f"Bearer {access_token}")


def clear_all_table_data(session: Session, metadata, except_tables: List[str] = None):
    session.execute("SET FOREIGN_KEY_CHECKS = 0;")
    for table in metadata.sorted_tables:
        if table.name not in except_tables:
            session.execute(table.delete())
    session.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()
