from flask import request, render_template, url_for, session, redirect
from .models import Institute
from .. import db
from . import institute_bp
from .find_dfi import *

@institute_bp.route('/abc', methods=['GET', 'POST'])

def I_D_C():

    try:

        institute_name = session['BBB_institute_titlee'] 
        institute_address = session['BBB_ins_addrr'] 
        institute_website = session['BBB_ins_wss'] 
        institute_founded_in = session['BBB_ins_founded_inn']
        institute_map = session['BBB_institute_locationn']
        institute_desc = session['BBB_institute_summeryy']
        institute_logo = session['BBB_l_s_oo'] 
        

        isExistinstitute = Institute.query.filter_by(institute_website=institute_website).first()

        if isExistinstitute is None:
            print("Didn't Exist Before!")
                   
            info = Institute(institute_name=institute_name, institute_address=institute_address, institute_website=institute_website, institute_founded_in = institute_founded_in, institute_map = institute_map, institute_desc = institute_desc, institute_logo = institute_logo)
            db.session.add(info)
            db.session.commit()

            print("Information Has Been Inserted To DB!")
            return redirect(url_for('review.refer'))

        else:
            print("Already Exist!")
            print("Information Already Exist...Just Give Us A Review Only!")
            return redirect(url_for('review.refer'))
            #return "INSERTED!"


    except Exception as e:
       return redirect(url_for('institute.U_D_C_0'))




   