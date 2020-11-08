from flask import request, render_template, url_for, redirect, session
from .. import db
from .models import Review
from ..institute.models import *
from ..institute.views import *
from . import review_bp
from .form import ReviewForm



@review_bp.route('/Review')
def refer():
        review_form = ReviewForm()
        return render_template("UserReviewForm.html", form=review_form)



@review_bp.route('/ReviewDone', methods=['GET', 'POST'])



def U_D_C_1():
        review_form = ReviewForm()
        iwrem=session['BBB_ins_wss']
        theUser = Institute.query.filter_by(institute_website=iwrem).first()
  
        
        if request.method == 'POST':
                        first_name = request.form.get('first_name')
                        last_name = request.form.get('last_name')
                        content = request.form.get('content')
                        
                        if review_form.validate_on_submit(): 
                                bbb = Review(first_name=first_name, last_name=last_name, content=content, institute_id=theUser.i_i_d)
                                db.session.add(bbb)
                                db.session.commit()
                                       
                                session.clear()
                                return redirect(url_for('wall.S_I_L'))

        
        return render_template("UserReviewForm.html", form=review_form)

