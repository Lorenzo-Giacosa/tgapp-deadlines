from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import backref, relation

from deadlines.model import DeclarativeBase
from tgext.pluggable import app_model, primary_key

class Sample(DeclarativeBase):
    __tablename__ = 'deadlines_samples'

    uid = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(16))

    user_id = Column(Integer, ForeignKey(primary_key(app_model.User)))
    user = relation(app_model.User)

