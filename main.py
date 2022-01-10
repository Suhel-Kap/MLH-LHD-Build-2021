from flask import Flask 
from flask import render_template,request
import requests, json, os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'api_key' : 'ca39f170e71c8087182831e20a2ac201',
            'city_name' : city
        }
        url = requests.get('https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'.format(**params))
        data = url.json()
        temp = data['main']['temp']
        return render_template('weather.html', data=temp, city=city)
    return render_template('index.html')


def index():
    params = {
        'api_key' : 'ca39f170e71c8087182831e20a2ac201',
        'city_name' : 'London'
    }
    url = requests.get('https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'.format(**params))
    data = url.json()
    temp = data['main']['temp']
    return render_template('index.html', data=temp)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)