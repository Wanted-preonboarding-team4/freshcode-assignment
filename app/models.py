from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class UserRegister(BaseModel):
    email: EmailStr = "test@test.com"
    pw: str = "test"
    user_type_id: int = 1
