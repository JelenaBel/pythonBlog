from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catering.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), primary_key=False)
    price = db.Column(db.Float(7), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<products {self.id}>"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<users {self.id}>"


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
def contact():
    return render_template("contact.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
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
            return redirect('/signup')
        except:

            print("При регистрации произошла ошибка")
            return "При регистрации произошла ошибка"

    return render_template("register.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug =True)

