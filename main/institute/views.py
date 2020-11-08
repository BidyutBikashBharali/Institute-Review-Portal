from flask import request, render_template, url_for, redirect, session, render_template_string
from .models import Institute
from .. import db
from . import institute_bp
from .form import InstituteForm
from .find_dfi import *


@institute_bp.route('/', methods=['GET', 'POST'])
def U_D_C_0():
      institute_form = InstituteForm()
      if request.method == 'POST':
            
            institute_name = request.form.get('institute_name')
            institute_address = request.form.get('institute_address')

            if institute_form.validate_on_submit(): 

                  session['institute_name'] = institute_name
                  session['institute_address'] = institute_address

                  return redirect(url_for('institute.find_insd'))
   
      return render_template('InstituteForm.html', form=institute_form) 

