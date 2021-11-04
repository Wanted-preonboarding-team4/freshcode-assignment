from app.database.schema import Users


def is_email_exist(email: str):
    get_email = Users.get(email=email)
    if get_email:
        return True
    return False