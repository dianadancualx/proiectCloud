from flask import Flask, render_template, jsonify, request
import requests
#importam cheia pentru Google API
from key import key
app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/temperature', methods = ['POST'])
def temperature():
    yourcity = request.form['city']
    #apelam API
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?appid=95a6c4c3ab7bde93a43c3355ed7f0da8&q='+yourcity+'&units=metric')
    json_object = r.json()
    oras = str(json_object['name'])
    tara = json_object['sys']['country']
    descriere = json_object['weather'][0]['description']
    temperatura = float(json_object['main']['temp'])
    umiditate = float(json_object['main']['humidity'])
    nori = float(json_object['clouds']['all'])
    vant = float(json_object['wind']['speed'])
    return render_template('temperature.html', name=oras,country = tara, temp =temperatura, humidity = umiditate, all = nori, description = descriere, speed = vant)

@app.route("/layout", methods=["GET"])
def retrieve():
    return render_template('layout.html')

@app.route("/sendRequest/<string:query>")
def results(query):
    #trimitere request folosind cheia si obiectul cautat = query
    search_payload = {"key":key, "query":query}
    search_req = requests.get(search_url, params=search_payload)
    #return reprezentarea json
    search_json = search_req.json()

    #preluare place_id
    place_id = search_json["results"][0]["place_id"]

    #afisare detalii in Google Maps pentru place_id
    details_payload = {"key":key, "placeid":place_id}
    details_resp = requests.get(details_url, params = details_payload)
    details_json = details_resp.json()

    url = details_json["result"]["url"]
    return jsonify({'result' : url})

if __name__ == "__main__":
    app.run(debug=True)