# accuweather keys
# API key = 8aaae57f966915b85ed963bd8af3866f
# COdes for openweather https://openweathermap.org/weather-conditions

from flask import Flask, render_template, redirect, request, url_for
import urllib, json, requests

app = Flask(__name__)
 
@app.route('/')
@app.route('/home') 
def index():
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

if __name__ == "__main__":
    app.run(debug=True)


