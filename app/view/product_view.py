from fastapi import APIRouter

router = APIRouter(prefix="/products")


@router.post("/create")
def create_product(menu_info: MenuRegister, session: Session = Depends(db.session)):
    if not menu_info.category or not menu_info.menu_name or not menu_info.description or not menu_info.item:
        return JSONResponse(status_code=400, content=dict(msg="빠지면 안되는 항목이 있습니다. 모두 추가해주세요."))
    if is_menu_name_exist(menu_info, session):
        return JSONResponse(status_code=400, content=dict(msg="이미 존재하는 메뉴입니다."))
    return JSONResponse(status_code=201, content=dict(msg=f"{menu_info.menu_name} 생성 성공하였습니다."))