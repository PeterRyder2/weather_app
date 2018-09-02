# accuweather keys
# location key (for foxford)= 210463
# API key = pc2TdWiYE3WoXW0xP339FGj8HWqXpeEc


from flask import Flask, render_template, redirect, request
import urllib, json, requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("template.html")

@app.route('/weather', methods = ["GET", "POST"])
def getweather():
    if request.method == "POST":
        print("entered loop")
        url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/210463?apikey=pc2TdWiYE3WoXW0xP339FGj8HWqXpeEc'
        
        response = requests.get(url)
        jresponse = response.text
        data = json.loads(jresponse)
        data2 = data["DailyForecasts"]['Day']
        #print("Data2 is {}".format(data2))
        return render_template("template.html",  a=data['DailyForecasts'])
    else:
        print("entered else loop")
        render_template("template.html")

if __name__ == "__main__":
    app.run(debug= True)



