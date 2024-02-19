from flask import Blueprint, render_template, request, g

bp = Blueprint('home', __name__, url_prefix='')

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
