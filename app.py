# accuweather keys
# location key (for foxford)= 210463
# API key = 8aaae57f966915b85ed963bd8af3866f


from flask import Flask, render_template, redirect, request
import urllib, json, requests, objectpath

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("template.html")

@app.route('/weather', methods = ["GET", "POST"])
def getweather():
    if request.method == "POST":
        print("entered loop")
        url= 'https://api.openweathermap.org/data/2.5/weather?lat=53.976192&lon=-9.117549&appid=8aaae57f966915b85ed963bd8af3866f'
        response = requests.get(url)
        jresponse = response.text
        data = json.loads(jresponse)
        #print("Data2 is {}".format(data2))
        return render_template("template.html", a=data)
    else:
        print("entered else loop")
        render_template("template.html")

if __name__ == "__main__":
    app.run(debug=True)



