from app.database.schema import Menu, Item


def is_menu_name_exist(menu_name):
    get_menu = Menu.get(name=menu_name)
    if get_menu:
        return True
    return False


def is_menu_exist(menu_id):
    get_menu = Menu.get(id=menu_id)
    if get_menu:
        return get_menu
    return False


def is_menu_exist_than_update_product(menu_id, request, session):
    menu = session.query(Menu).filter(Menu.id == menu_id).first()
    for key, value in dict(request).items():
        setattr(menu, key.decode('UTF-8'), value)
    session.commit()
    return menu


def create_menu(menu_info, session):
    menu = Menu.create(session, auto_commit=True, name=menu_info.name, is_sold=menu_info.menu_isSold,
                       badge_id=menu_info.badge_id, tag_id=menu_info.tag_id, food_category_id=menu_info.category_id,
                       count=menu_info.count, description=menu_info.description)
    for each_item in menu_info.item:
        Item.create(session, auto_commit=True, menu_id=menu.id, size_id=each_item.size_id, price=each_item.price,
                    is_sold=each_item.is_sold, count=each_item.count)
    return True


def delete_product_if_exist(menu_id,session):
    session.query(Menu).filter(Menu.id == menu_id).delete()
    session.commit()
    return True