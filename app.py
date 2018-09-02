# accuweather keys
# API key = 8aaae57f966915b85ed963bd8af3866f
# COdes for openweather https://openweathermap.org/weather-conditions

from flask import Flask, render_template, redirect, request
import urllib, json, requests
JSON = {'coord': {'lon': -9.12, 'lat': 53.98}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 281.15, 'pressure': 1023, 'humidity': 100, 'temp_min': 281.15, 'temp_max': 281.15}, 'visibility': 10000, 'wind': {'speed': 3.1, 'deg': 320}, 'clouds': {'all': 20}, 'dt': 1535923800, 'sys': {'type': 1, 'id': 5238, 'message': 0.0043, 'country': 'IE', 'sunrise': 1535867276, 'sunset': 1535916158}, 'id': 2964233, 'name': 'Foxford', 'cod': 200}

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("template.html")

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
      

        return render_template("template.html", a=data['weather'][0]['icon'])
    else:
        print("entered else loop")
        render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)


