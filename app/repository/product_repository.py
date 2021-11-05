from database.schema import Menu, Item, Tag


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


def delete_product_if_exist(menu_id, session):
    session.query(Menu).filter(Menu.id == menu_id).delete()
    session.commit()
    return True


def menu_list_repository(skip, limit, session):
    menu_list = session.query(Menu).offset(skip).limit(limit)
    temp = []
    for i in menu_list:
        temp.append(i.to_dict())
    return temp


def menu_detail_repository(menu_id, session):
    menu_detail_item = session.query(Menu, Item).join(Item, Item.menu_id == menu_id).filter(Menu.id == menu_id).all()
    menu_detail_tag = session.query(Menu, Tag).distinct().join(Tag, Tag.id == Menu.tag_id).filter(
        Menu.id == menu_id).all()

    temp = menu_detail_item[0][0].to_dict()
    temp['item'] = []
    temp['tag'] = []
    for i in menu_detail_item:
        temp['item'].append(i[1].to_dict())

    for j in menu_detail_tag:
        temp['tag'].append(j[1].to_dict())
    return temp
