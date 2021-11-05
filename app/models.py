from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class UserRegister(BaseModel):
    email: EmailStr = "test@test.com"
    pw: str = "test"
    user_type_id: int = 1


class Item(BaseModel):
    name: str = "미디움"
    size: str = "M"
    price: int = 8000
    isSold: bool = False


class Tag(BaseModel):
    type: str = "vegetarianism"
    name: str = "페스코베지테리안"


class MenuRegister(BaseModel):
    category: str = "SALAD"
    menu_name: str = "깔라마리 달래 샐러드"
    description: str = "해산물 샐러드"
    menu_isSold: bool = False
    badge_id: int = 1
    item: list[Item]
    tags_id: int = 1
