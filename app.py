# accuweather keys
# API key = 8aaae57f966915b85ed963bd8af3866f
# COdes for openweather https://openweathermap.org/weather-conditions

from flask import Flask, render_template, redirect, request, url_for,flash
import urllib, json, requests
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config["SECRET_KEY"] = '07f6eb13ea9fc96e2a0a213a0e17becd'


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
    form = RegistrationForm()
    if form.validate_on_submit(): 
        flash(f"Account succesfully created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in", "success ")
            return redirect(url_for('home'))
        else:
            flash("You did not put in your username and password correctly!!", "danger")  
    return render_template('login.html', title = 'login', form=form)



if __name__ == "__main__":  
    app.run(debug=True)


