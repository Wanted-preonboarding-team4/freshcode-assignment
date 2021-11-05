from datetime import datetime, timedelta

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
from app.database.conn import Base, db


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
    __table_args__ = {'extend_existing': True}
    name          = Column(String(length=255), nullable=False)


class Users(Base, BaseMixin):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    user_type_id  = Column(Integer, ForeignKey(UserType.id))
    email         = Column(String(length=255), nullable=False)
    password      = Column(String(length=255), nullable=False)
    create_at     = Column(DateTime, nullable=False, default=func.utc_timestamp())
    update_at     = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())


class FoodCategory(Base, BaseMixin):
    __tablename__ = "food_category"
    __table_args__ = {'extend_existing': True}
    name          = Column(String(length=45), nullable=False)

class Badge(Base,BaseMixin):
    __tablename__ = "badge"
    __table_args__ = {'extend_existing': True}
    name          = Column(String(length=45), nullable=True)

class TagType(Base,BaseMixin):
    __tablename__ = "tag_type"
    __table_args__ = {'extend_existing': True}
    name          = Column(String(length=45), nullable=False)

class Tag(Base, BaseMixin):
    __tablename__ = "tag"
    __table_args__ = {'extend_existing': True}
    name          = Column(String(length=45), nullable=False)
    tag_type_id   = Column(Integer,ForeignKey(TagType.id))

class Menu(Base,BaseMixin):
    __tablename__    = "menu"
    __table_args__ = {'extend_existing': True}
    name             = Column(String(length=45), nullable=False)
    is_sold          = Column(Boolean(),nullable=False, default=False)
    count            = Column(String(length=45), nullable=False)
    food_category_id = Column(Integer, ForeignKey(FoodCategory.id))
    badge_id         = Column(Integer, ForeignKey(Badge.id), nullable=True)
    tag_id           = Column(Integer, ForeignKey(Tag.id))
    description= Column(String(length=500), nullable=False)

class SizeType(Base,BaseMixin):
    __tablename__ = "size_type"
    __table_args__ = {'extend_existing': True}
    name          = Column(String(length=45), nullable=False)

class Item(Base,BaseMixin):
    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}
    count         = Column(Integer,nullable=False)
    is_sold       = Column(Boolean(),nullable=False, default=False)
    price         = Column(Integer,nullable=False)
    menu_id       = Column(Integer,ForeignKey(Menu.id))
    size_id       = Column(Integer,ForeignKey(SizeType.id))