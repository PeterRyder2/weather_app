# accuweather keys
# API key = 8aaae57f966915b85ed963bd8af3866f
# COdes for openweather https://openweathermap.org/weather-conditions

from flask import Flask, render_template, redirect, request, url_for
import urllib, json, requests


# todays JSON output
JSON = {'coord': {'lon': -9.12, 'lat': 53.98}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 
'base': 'stations', 'main': {'temp': 285.15, 'pressure': 1027, 'humidity': 76, 'temp_min': 285.15, 'temp_max': 285.15}, 
'visibility': 10000, 'wind': {'speed': 4.1, 'deg': 310}, 'clouds': {'all': 20}, 'dt': 1535967000,
'sys': {'type': 1, 'id': 5238, 'message': 0.002, 'country': 'IE', 'sunrise': 1535953728, 'sunset': 1536002486},
'id': 2964233, 'name': 'Foxford', 'cod': 200}

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


