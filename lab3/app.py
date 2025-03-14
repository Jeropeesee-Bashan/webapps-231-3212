from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, current_user

app = Flask(__name__)

app.secret_key = 'GEtdgfdgdfRGGsdgb'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        super().__init__()
        self.id = id

users = {"user": {"password": "qwerty"}}


@login_manager.user_loader
def load_user(login):
    if login not in users:
        return

    return User(login)


visit_count = 0

@app.route("/")
def count():
    global visit_count
    login_success = "login_success" in request.args
    visit_count += 1
    return render_template("count.html", visit_count=visit_count, login_success=login_success)


@app.route("/secret")
def secret():
    if not current_user.is_authenticated:
        next_ = "secret"
        return redirect(url_for("login", reason="unauthorized", next=next_))
    return render_template("secret.html", user=current_user.id)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        reason = request.args["reason"] if "reason" in request.args else ""
        return render_template("login.html", reason=reason)
    else:
        data = request.form
        login = data["login"]
        password = data["password"]

        if login in users and password == users[login]["password"]:
            remember = True if "remember" in data else False
            user = User(login)
            login_user(user, remember=remember)
            next_ = None
            if "next" in request.args:
                next_ = request.args["next"]
            return redirect("/?login_success=" if next_ is None else url_for(next_))
        return redirect(url_for("login", reason="badlogin"))


if __name__ == '__main__':
    app.run(debug=True)
