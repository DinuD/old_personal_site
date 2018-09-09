from flask import Blueprint, render_template

mod_personal = Blueprint('personal', __name__, template_folder='templates')

@mod_personal.route('/')
def index(title=None):
    return render_template('home.html', title='Home - DinuD11')

