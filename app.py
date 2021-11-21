
from flask import Flask,  render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catering.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'zybrzubryachestiy'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'obyelousova@gmail.com'
app.config['MAIL_PASSWORD'] = 'Kokoshnik45'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), primary_key=False)
    price = db.Column(db.Float(7), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(100))

    def __repr__(self):
        return f"<products {self.id}>"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<users {self.id}>"


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(300), nullable=False)
    message = db.Column(db.Text(300), nullable=False)

    def __repr__(self):
        return f"<сontacts {self.id}>"


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/menus')
def menus():
    return render_template("menus2.html")


@app.route('/menusdetail')
def menusdetail():
    return render_template("menusdetail.html")


@app.route('/contact', methods=['POST', 'GET'])
def feedback():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['customertext']
        message = request.form['subject']

        contact1 = Contacts(name=name, email=email, subject=subject, message=message)

        try:
            db.session.add(contact1)
            db.session.commit()

            return redirect('/')

        except:

            print("При регистрации произошла ошибка")

            return "При регистрации произошла ошибка"

    return render_template("contact.html")


def sending_email(name, email):
    msg = Message('Hello from the other side!', sender='obyelousova@gmail.com', recipients=[email])
    msg.body = "Hey,"+name+" you are successfully registered on Simple Catering."
    mail.send(msg)
    return "Message sent!"


@app.route('/signup')
def signup_open():
    return render_template("signup.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        if email and password:

            user = Users.query.filter_by(email=email).first()

            if user.password == password:
                session['user'] = user.name
                session['user_email'] = user.email
                flash('You were successfully logged in')

                render_template("index.html")
            else:
                flash('Login or password is not correct')
        else:
            flash('Login or password is not given')

    return render_template("signup.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        if request.form['password'] == request.form['passwordRepeat']:
            password = request.form['password']

            user = Users(name=name, email=email, password=password)

        try:
            db.session.add(user)
            db.session.commit()
            sending_email(name, email)
            return redirect('/signup')

        except:

            print("При регистрации произошла ошибка")

            return "При регистрации произошла ошибка"

    return render_template("register.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

