
from flask import Flask,  render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message
import random
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catering.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'zybrzubryachestiy'
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



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
    category = db.Column(db.String(100), primary_key=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))

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
    updatetime = db.Column(db.Date, default=datetime.utcnow)

    def __repr__(self):
        return f"<сontacts {self.id}>"

db.create_all()
print("DB Created")

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/menus')
def menus():
    return render_template("menus2.html")

@app.route('/shop')
def shop():

    return render_template("shop.html")

@app.route('/feedback')
def feedbakreading():
    contacts = Contacts.query.all();
    return render_template("feedback.html", contacts = contacts)


@app.route('/newsletters')
def newsletters():
    contacts = Contacts.query.all();
    users = Users.query.all();
    return render_template("newsletters.html", contacts = contacts, users = users)

def sending_email_newsletter(subject, email, text):
    msg = Message('You letter to Simple Catering.', sender='obyelousova@gmail.com', recipients=[email])
    msg.body = "Hey, "+name+"! Thank you for contacting Simple Catering! We will answer for your letter as soon as possible."
    mail.send(msg)
    return "Message sent!"


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
            sending_email_feedbackform(name, email)
            return redirect('/')

        except:

            print("При регистрации произошла ошибка")

            return "При регистрации произошла ошибка"

    return render_template("contact.html")


@app.route('/addproduct', methods=['POST', 'GET'])

def addproduct():
    if request.method == "POST":

        name = request.form['productname']
        price = request.form['productprice']
        category = request.form['category']
        description = request.form['subject']
        file = request.files['filename']




        if file.filename == '':
            flash("No image selected for upload")
            return render_template("addproduct.html")

        if file and file.filename:

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))



        product = Products(title=name, price=price, category=category, description=description, photo=file.filename)

        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/')

        except:

            print("При добавлении товара произошла ошибка")

            return "При добавлении товара произошла ошибка"

    return render_template("addproduct.html")


def sending_email(name, email):
    msg = Message('Hello from the other side!', sender='obyelousova@gmail.com', recipients=[email])
    msg.body = "Hey,"+name+" you are successfully registered on Simple Catering."
    mail.send(msg)
    return "Message sent!"


def sending_email_feedbackform(name, email):
    msg = Message('You letter to Simple Catering.', sender='obyelousova@gmail.com', recipients=[email])
    msg.body = "Hey, "+name+"! Thank you for contacting Simple Catering! We will answer for your letter as soon as possible."
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


@app.route('/addproduct')
def addproductopen():
    return render_template("addproduct.html")


if __name__ == "__main__":
    app.run(debug=True)

