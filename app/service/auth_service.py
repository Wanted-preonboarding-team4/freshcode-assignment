import bcrypt
import jwt

from database.schema import Users
from repository.auth_repository import is_email_exist
from common.consts import JWT_ALGORITHM, JWT_SECRET
import time



def create_user_if_not_found_email(reg_info, session):
    if is_email_exist(reg_info.email):
        return False
    hash_pw = bcrypt.hashpw(reg_info.pw.encode("utf-8"), bcrypt.gensalt())
    Users.create(session, auto_commit=True, password=hash_pw, email=reg_info.email, user_type_id=reg_info.user_type_id)

    return True


def login_user_if_not_found_user(user_info, session):
    if not is_email_exist(user_info.email):
        return False
    user = Users.get(email=user_info.email)
    password_match = bcrypt.checkpw(user_info.pw.encode('utf-8'), user.password.encode('utf-8'))
    if user and password_match:
        token = jwt.encode({'user_id': user.id, "expires": time.time() + 600}, JWT_SECRET, JWT_ALGORITHM)
        return token
    return False
