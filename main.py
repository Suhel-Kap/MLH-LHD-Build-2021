from flask import Flask
from flask import render_template, request
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

API_KEY = os.getenv("API_KEY")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'api_key': API_KEY,
            'city_name': city
        }
        url = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'.format(**params))
        data = url.json()
        my_string = "static/img/" + data['weather'][0]['icon']+ ".svg"
        city_name = data['name'] 
        country_name = data['sys']['country']
        temp = data['main']['temp']
        return render_template('weather.html', data=data,my_string=my_string, city_name=city_name, temp=temp, country_name=country_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
