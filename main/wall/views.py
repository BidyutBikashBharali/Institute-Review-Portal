from flask import request, render_template, session, url_for, redirect
from . import wall_bp
from ..institute.models import Institute
import random
from ..review.models import Review

@wall_bp.route('/Instituteee')
def S_I_L():

    institute_list = Institute.query.all() 
    return render_template('InstituteParticular.html', i_l = institute_list) 


@wall_bp.route('/Instituteee/Reviews/<int:ins_id>')
def I_P_R(ins_id):
    c = random.choice(['red','indigo','green','brown','orange','pink','purple','deep-orange','blue-gray','teal','win8-pink','win8-emerald'])
    bc = random.choice(['red','indigo','green','brown','orange','pink','purple','deep-orange','blue-gray','teal','win8-pink','win8-emerald'])
    theInstitute = Institute.query.filter_by(i_i_d=ins_id).first()
    return render_template('ParticularReview.html', t_i = theInstitute, color = c, bcolor=bc)

@wall_bp.route('/RandomReview')
def R_R():
    c = random.choice(['red','indigo','green','brown','orange','pink','purple','deep-orange','blue-gray','teal','win8-pink','win8-emerald'])
    bc = random.choice(['red','indigo','green','brown','orange','pink','purple','deep-orange','blue-gray','teal','win8-pink','win8-emerald'])
    randomReview = Review.query.all()
    return render_template('RandomReview.html', r_r = randomReview, color = c, bcolor=bc)

@wall_bp.route('/Search')
def Search():
    return "Search Option Will Be Available In The Production Version Only"

@wall_bp.route('/About')
def About():
    return render_template('about.html')