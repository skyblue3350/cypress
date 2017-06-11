from functools import wraps
from flask import Flask, render_template, redirect, url_for, request, abort
from flask_login import LoginManager, login_user, UserMixin, current_user
from flask_ldap3_login import LDAP3LoginManager
from flask_ldap3_login.forms import LDAPLoginForm

from user import User
from reverseproxy import ReverseProxy

app = Flask(__name__)
app.wsgi_app = ReverseProxy(app.wsgi_app)
app.config.from_object("config")

login_manager = LoginManager(app)
ldap_manager = LDAP3LoginManager(app)

users = {}

@login_manager.user_loader
def load_user(id):
    if id in users:
        return users[id]
    return None

@ldap_manager.save_user
def save_user(dn, username, data, memberships):
    user = User(dn, username, data)
    users[dn] = user
    return user

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user or current_user.is_anonymous:
            return redirect(url_for("login", next=request.url, _external=True))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def index():
    return render_template("index.html", user=current_user)

@app.route("/init")
def init():
    if not current_user or current_user.is_anonymous:
        return redirect(url_for("login", next=request.args.get("next", ""), _external=True))
    else:
        return redirect(url_for("index", _external=True))

@app.route("/check")
def check():
    if not current_user or current_user.is_anonymous:
       return abort(401)
    else:
       return "ok"

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LDAPLoginForm()

    if form.validate_on_submit():
        login_user(form.user)
        return redirect(request.args.get("next", url_for("index", _external=True)))

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(
        debug=app.config["DEBUG"],
        host=app.config["HOST"],
        port=app.config["PORT"],
    )
