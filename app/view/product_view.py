from fastapi import APIRouter, Depends
from app.models import MenuRegister
from sqlalchemy.orm import Session
from app.database.conn import db
from starlette.responses import JSONResponse
from app.service.product_service import is_menu_name_exist, delete_product_if_exist, menu_list_service, \
    is_menu_exist_than_update_product, menu_detail_service
from typing import AnyStr, Any, Dict
from app.utils import JWTBearer, JWTBearerForAdminOnly

router = APIRouter(prefix="/products")

JSONObject = Dict[AnyStr, Any]


@router.post("/create", dependencies=[Depends(JWTBearerForAdminOnly())], tags=['product'])
def create_product(menu_info: MenuRegister, session: Session = Depends(db.session)):
    if not menu_info.category_id or not menu_info.name or not menu_info.description or not menu_info.item:
        return JSONResponse(status_code=400, content=dict(msg="빠지면 안되는 항목이 있습니다. 모두 추가해주세요."))
    if is_menu_name_exist(menu_info, session):
        return JSONResponse(status_code=400, content=dict(msg="이미 존재하는 메뉴입니다."))
    return JSONResponse(status_code=201, content=dict(msg=f"{menu_info.name} 생성 성공하였습니다."))


@router.patch("/{menu_id}", dependencies=[Depends(JWTBearerForAdminOnly())], tags=['product'])
def update_product(menu_id: int, request: JSONObject, session: Session = Depends(db.session)):
    update_result = is_menu_exist_than_update_product(menu_id, request, session)
    if not update_result:
        return JSONResponse(status_code=400, content=dict(msg=" 수정 실패하였습니다."))
    return JSONResponse(status_code=200, content=dict(msg=f"{update_result}수정 성공하였습니다."))


@router.delete("/{menu_id}", dependencies=[Depends(JWTBearerForAdminOnly())], tags=['product'])
def delete_product(menu_id: int, session: Session = Depends(db.session)):
    if delete_product_if_exist(menu_id, session):
        return JSONResponse(status_code=204, content="")
    return JSONResponse(status_code=400, content=dict(msg=" 수정 실패하였습니다."))


@router.get("/menu_list", dependencies=[Depends(JWTBearer())], tags=['product'])
async def menu_list(skip: int = None, limit: int = None, session: Session = Depends(db.session)):
    menu_list = menu_list_service(skip, limit, session)
    return JSONResponse(status_code=200, content=dict(msg=menu_list))


@router.get("/menu/{menu_id}", dependencies=[Depends(JWTBearer())], tags=['product'])
async def menu_detail(menu_id: int, session: Session = Depends(db.session)):
    menu_detail = menu_detail_service(menu_id, session)
    if type(menu_detail) == dict:
        return JSONResponse(status_code=200, content=dict(msg=menu_detail))
    else:
        return menu_detail
