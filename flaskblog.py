from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "29b88f280b5ab6fbc8996226930c6e0b" # secrets.token_hex(16)

posts = [
    {
        "author": "Guillermo N",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "May 29, 2022",
    },
    {
        "author": "Tulio Fra",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "May 30, 2022",
    }
]

@app.route("/")
@app.route("/home")
def home():

    return render_template("home.html", posts=posts)


@app.route("/about")
def about():

    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "test@example.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
            
    return render_template("login.html", title="LogIn", form=form)


if __name__ == '__main__':
    app.run(debug=True)