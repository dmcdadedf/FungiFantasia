import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from . import firebase

auth = firebase.auth()

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            if user:
                session.clear()
                session['user'] = user['email']
                session['idToken'] = user['idToken']
                return redirect(url_for('home.index'))
        except:
            return "Failed to login"

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user')
    user_idToken = session.get('idToken')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id
        g.idToken = user_idToken

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view