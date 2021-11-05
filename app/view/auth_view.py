from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.models import UserRegister
from app.database.conn import db
from app.service.auth_service import create_user_if_not_found_email, login_user_if_not_found_user

router = APIRouter(prefix="/auth")


@router.post("/user_signup", tags=['user'])
async def user_signup(reg_info: UserRegister, session: Session = Depends(db.session)):
    if not reg_info.email or not reg_info.pw:
        return JSONResponse(status_code=400, content=dict(msg="이메일과 패스워드는 반드시 포함되어야 합니다."))
    if not create_user_if_not_found_email(reg_info, session):
        return JSONResponse(status_code=400, content=dict(msg="이미 존재하는 이메일입니다"))
    return JSONResponse(status_code=201, content=dict(msg="회원가입되셨습니다."))


@router.post("/user/login", tags=['product'])
async def user_login(user_info: UserRegister, session: Session = Depends(db.session)):
    if not user_info.email or not user_info.pw:
        return JSONResponse(status_code=400, content=dict(msg="이메일과 패스워드는 반드시 포함되어야 합니다."))
    token = login_user_if_not_found_user(user_info, session)
    if not token:
        return JSONResponse(status_code=400, content=dict(msg="아이디와 패스워드를 확인해주시기 바랍니다."))
    return JSONResponse(status_code=200, content=dict(msg=token))
