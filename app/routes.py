
from flask import render_template, redirect, request, url_for, flash
import urllib, json, requests
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, UserMixin, current_user, logout_user


@app.route('/')
@app.route('/home') 
def home():
    return render_template("layout.html")


@app.route('/weather', methods = ["GET", "POST"])
def getweather():
    if request.method == "POST":
        print("entered loop")
        try:
            url= 'https://api.openweathermap.org/data/2.5/weather?lat=53.976192&lon=-9.117549&appid=8aaae57f966915b85ed963bd8af3866f'
            response = requests.get(url)
            jresponse = response.text
            data = json.loads(jresponse)
        except:
            raise ValueError("could not load json properly")
        return render_template("weatherres.html", title='Weather Result', weather=data['weather'][0]['description'], icon=data['weather'][0]['icon'])
    else:
        print("entered else loop")
        render_template("layout.html")

@app.route('/register', methods = ["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit(): 
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created. You can now login", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)


@app.route('/login', methods = ["GET","POST"])
def login():
    # if the user is already logged in, direct to the home page again
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        #query database for user email and if its in database login and remmeber 
        # redirect to home page
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash("login unsuccesful !!", "danger")  
    return render_template('login.html', title = 'login', form=form)



@app.route('/logout')
def logout():
    #using the logout package logout the user
    logout_user()
    return redirect(url_for('home'))


