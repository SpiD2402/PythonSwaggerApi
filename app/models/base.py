from sqlalchemy_mixins import AllFeaturesMixin
from app import db


class BaseModel(db.Model,AllFeaturesMixin):
    __abstract__=True
    