from fastapi import APIRouter, Depends
from app.models import MenuRegister
from sqlalchemy.orm import Session
from app.database.conn import db
from starlette.responses import JSONResponse
from app.service.product_service import is_menu_name_exist, is_menu_exist_than_update_product, delete_product_if_exist
from typing import AnyStr, Any, Dict
from app.utils import JWTBearer,JWTBearerForAdminOnly


router = APIRouter(prefix="/products")

JSONObject = Dict[AnyStr, Any]


@router.post("/create", dependencies=[Depends(JWTBearerForAdminOnly())])
def create_product(menu_info: MenuRegister, session: Session = Depends(db.session) ):
    if not menu_info.category_id or not menu_info.name or not menu_info.description or not menu_info.item:
        return JSONResponse(status_code=400, content=dict(msg="빠지면 안되는 항목이 있습니다. 모두 추가해주세요."))
    if is_menu_name_exist(menu_info, session):
        return JSONResponse(status_code=400, content=dict(msg="이미 존재하는 메뉴입니다."))
    return JSONResponse(status_code=201, content=dict(msg=f"{menu_info.name} 생성 성공하였습니다."))


#
# @router.patch("/{menu_id}")
# def update_product(menu_id: int,menu_info: MenuRegister, session: Session = Depends(db.session)):
#     if is_menu_exist(menu_id, session):
#
#     return JSONResponse(status_code=201, content=dict(msg=f"{menu_info.menu_name} 생성 성공하였습니다."))