from app.repository import product_repository

def is_menu_name_exist(menu_info, session):
    if product_repository.is_menu_name_exist(menu_info.menu_name):
        return True
    product_repository.create_menu(menu_info,session)
    return False
