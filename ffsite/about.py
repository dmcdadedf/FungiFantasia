from flask import Blueprint, render_template, request, g

bp = Blueprint('about', __name__, url_prefix='')

@bp.route('/about', methods=['GET', 'POST'])
def index():
    return render_template('about.html')