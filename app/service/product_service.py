from repository import product_repository, menu_list_repository, menu_detail_repository,is_menu_exist
from starlette.responses import JSONResponse


def is_menu_name_exist(menu_info, session):
    if product_repository.is_menu_name_exist(menu_info.name):
        return True
    product_repository.create_menu(menu_info, session)
    return False


def is_menu_exist_than_update_product(menu_id, request, session):
    return product_repository.is_menu_exist_than_update_product(menu_id, request, session)


def delete_product_if_exist(menu_id, session):
    return product_repository.delete_product_if_exist(menu_id, session)


def menu_list_service(skip, limit, session):
    menu_list = menu_list_repository(skip, limit, session)
    return menu_list

def menu_detail_service(menu_id, session):
    find_menu = is_menu_exist(menu_id)
    if not find_menu:
        return JSONResponse(status_code=401, content=dict(msg="존재하지 않는 상품입니다."))
    menu_datail = menu_detail_repository(menu_id, session)
    return menu_datail
