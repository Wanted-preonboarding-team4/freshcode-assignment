from datetime import datetime, timedelta
from os import name

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum,
    Boolean,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session,relationship
from sqlalchemy.sql.expression import _BindParamClause
from sqlalchemy.sql.functions import count
from database.conn import Base, db


class BaseMixin:
    id = Column(Integer, primary_key=True, index=True)

    def all_columns(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name != "created_at"]

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def create(cls, session: Session, auto_commit=False, **kwargs):
        obj = cls()
        for col in obj.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(obj, col_name, kwargs.get(col_name))
        session.add(obj)
        session.flush()
        if auto_commit:
            session.commit()
        return obj

    @classmethod
    def get(cls, **kwargs):
        session = next(db.session())
        query = session.query(cls)
        for key, val in kwargs.items():
            col = getattr(cls, key)
            query = query.filter(col == val)

        if query.count() > 1:
            raise Exception("Only one rowis supposed to be returned, but got more than one.")
        return query.first()


class UserType(Base, BaseMixin):
    __tablename__ = "user_type"
    name = Column(String(length=255), nullable=False)


class Users(Base, BaseMixin):
    __tablename__ = "user"
    user_type_id = Column(Integer, ForeignKey(UserType.id))
    email = Column(String(length=255), nullable=False)
    password = Column(String(length=255), nullable=False)
    create_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    update_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    user_type=relationship("UserType")

class FoodCategory(Base, BaseMixin):
    __tablename__= "food_category"
    name = Column(String(length=45), nullable=False)

class Badge(Base,BaseMixin):
    __tablename__= "badge"
    name = Column(String(length=45), nullable=False)

class Menu(Base,BaseMixin):
    __tablename__= "menu"
    name = Column(String(length=45), nullable=False)
    is_sold = Column(Boolean(),nullable=False, default=False)
    count = Column(String(length=45), nullable=False)
    food_category_id = Column(Integer, ForeignKey(FoodCategory.id))
    badge_id = Column(Integer, ForeignKey(Badge.id))

class TagType(Base,BaseMixin):
    __tablename__="tag_type"
    name = Column(String(length=45), nullable=False)

class Tag(Base, BaseMixin):
    __tablename__="tag"
    name = Column(String(length=45), nullable=False)
    menu_id = Column(Integer,ForeignKey(Menu.id))
    tag_type_id = Column(Integer,ForeignKey(TagType.id))

class SizeType(Base,BaseMixin):
    __tablename__="size_type"
    name = Column(String(length=45), nullable=False)

class Item(Base,BaseMixin):
    __tablename__="item"
    count = Column(Integer,nullable=False)
    is_sold = Column(Boolean(),nullable=False, default=False)
    price = Column(Integer,nullable=False)
    menu_id = Column(Integer,ForeignKey(Menu.id))
    size_id = Column(Integer,ForeignKey(SizeType.id))