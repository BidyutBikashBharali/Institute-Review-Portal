from .. import db
from ..institute.models import *


class Review(db.Model):
    __tablename__ = 'reviews'
    i_r_d = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), index=True, nullable=False)
    last_name = db.Column(db.String(100), index=True, nullable=False)
    content = db.Column(db.Text(), index=True, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()) 
    institute_id = db.Column(db.Integer, db.ForeignKey('institute.i_i_d'))

    def __init__(self, first_name, last_name, content, institute_id):
        self.first_name = first_name
        self.last_name = last_name
        self.content = content
        self.institute_id = institute_id

