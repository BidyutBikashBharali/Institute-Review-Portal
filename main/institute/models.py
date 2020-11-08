from .. import db 
from ..review.models import *


class Institute(db.Model):
    __tablename__ = 'institute'

    i_i_d = db.Column(db.Integer, primary_key=True)
    institute_name = db.Column(db.String(100), nullable=False, index=True)
    institute_address = db.Column(db.String(100), nullable=False, index=True)
    institute_website = db.Column(db.String(100), nullable=False, index=True)
    institute_founded_in = db.Column(db.String(20), nullable=False) 
    institute_map = db.Column(db.Text(), nullable=False)
    institute_desc = db.Column(db.Text(), nullable=False)
    institute_logo = db.Column(db.Text(), nullable=False)
    reviews = db.relationship('Review', backref='institute', lazy='dynamic')



    def __init__(self, institute_name, institute_address, institute_website, institute_founded_in, institute_map, institute_desc, institute_logo):

        self.institute_name = institute_name
        self.institute_address = institute_address
        self.institute_website = institute_website
        self.institute_founded_in = institute_founded_in
        self.institute_map = institute_map
        self.institute_desc = institute_desc
        self.institute_logo = institute_logo






