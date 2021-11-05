from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class UserRegister(BaseModel):
    email: EmailStr = "test@test.com"
    pw: str = "test"
    user_type_id: int = 1


class Item(BaseModel):
    name: str = "미디움"
    size_id: int = 1
    price: int = 8000
    is_sold: bool = False
    count: int = 100


class Tag(BaseModel):
    type: str = "vegetarianism"
    name: str = "페스코베지테리안"


class MenuRegister(BaseModel):
    category_id: int = 1
    name: str = "깔라마리 달래 샐러드"
    description: str = "해산물 샐러드"
    menu_isSold: bool = False
    badge_id: int = 1
    item: list[Item]
    tag_id: int = 1
    count: str = "1"
