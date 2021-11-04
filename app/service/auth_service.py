import bcrypt

from app.database.schema import Users
from app.repository.auth_repository import is_email_exist


def create_user_if_not_found_email(reg_info, session):
    if is_email_exist(reg_info.email):
        return False
    hash_pw = bcrypt.hashpw(reg_info.pw.encode("utf-8"), bcrypt.gensalt())
    Users.create(session, auto_commit=True, password=hash_pw, email=reg_info.email, user_type_id=reg_info.user_type_id)

    return True
