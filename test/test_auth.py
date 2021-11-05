import os
from database import Users, UserType
from main import create_app
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.database.conn import db, Base
from fastapi.testclient import TestClient

app = create_app()


# def setUp(client, session):
#     os.environ["API_ENV"] = "local"
#
#     Users.create(session=session,
#                  auto_commit=True,
#                  email='helloworld@freshcode.co.kr',
#                  password='123456',
#                  user_type_id=1)


def test_signup_post_success(client, session):
    """
    회원가입 성공 시 201 status 반환
    return :
    """

    data = {
        'email': 'helloworld@freshcode.co.kr',
        'pw': '123456',
        'user_type_id': 1
    }
    Users.create(session=session, password=data['pw'], email=data['email'], user_type_id=data['user_type_id'])
    response = client.post("auth/user_signup", json=data)
    response_body = response.json()
    assert response.status_code == 201


def test_signup_post_validation_email_fail(client):
    """
    이미 존재하는 이메일 시 400 status 반환
    return :
    """
    data = {
        'email': 'helloworld@freshcode.co.kr',
        'pw': '123456',
        'user_type_id': 1
    }

    response = client.post("auth/user_signup", json=data)
    response_body = response.json()
    assert response.status_code == 400


def test_signup_post_validation_password_fail(client):
    """
    비밀번호 확인이 틀렸을시 400 status 반환
    return :
    """
    data = {
        'email': 'helloworld@freshcode.co.kr',
        'pw': '12345678',
        'user_type_id': 1
    }

    response = client.post("auth/user_signup", json=data)
    response_body = response.json()
    assert response.status_code == 400


def test_login_post_success(client):
    """
    로그인 성공 시 status 200 반환
    return :
    """
    data = {
        'email': 'helloworld@freshcode.co.kr',
        'pw': '123456',
        'user_type_id': 1
    }

    response = client.post("auth/user/login", json=data)
    response_body = response.json()
    assert response.status_code == 200


def test_login_post_empty_email(client):
    """
    아이디, 비밀번호에 값이 없을 시 status 401 발생
    return :
    """
    data = {
        'email': '',
        'pw': '123456',
        'user_type_id': 1
    }

    response = client.post("auth/user/login", json=data)
    response_body = response.json()
    assert response.status_code == 422

def test_login_post_empty_password(client):
    """
    아이디, 비밀번호에 값이 없을 시 status 400 발생
    return :
    """
    data = {
        'email': 'helloworld@freshcode.co.kr',
        'pw': '',
        'user_type_id': 1
    }

    response = client.post("auth/user/login", json=data)
    response_body = response.json()
    assert response.status_code == 400


def test_login_post_empty_both(client):
    """
    아이디, 비밀번호에 값이 없을 시 status 400 발생
    return :
    """
    data = {
        'email': '',
        'pw': '',
        'user_type_id': 1
    }

    response = client.post("auth/user/login", json=data)
    response_body = response.json()
    assert response.status_code == 422


def test_login_post_wrong_password(client):
    """
    비밀번호가 틀렸을 시 status 400 발생
    return :
    """
    data = {
        'email': 'helloworld@freshcode.co.kr',
        'pw': '123dfgdgsd',
        'user_type_id': 1
    }

    response = client.post("auth/user/login", json=data)
    response_body = response.json()
    assert response.status_code == 400
