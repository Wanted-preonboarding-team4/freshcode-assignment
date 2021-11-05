from app.repository import product_repository


def is_menu_name_exist(menu_info, session):
    if product_repository.is_menu_name_exist(menu_info.name):
        return True
    product_repository.create_menu(menu_info, session)
    return False


def is_menu_exist_than_update_product(menu_id, request, session):
    return product_repository.is_menu_exist_than_update_product(menu_id, request, session)


def delete_product_if_exist(menu_id, session):
    return product_repository.delete_product_if_exist(menu_id, session)
