from flask import Flask, render_template, request
import requests
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
 
    # Make a request to the OpenWeatherMap API
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
 
    if data['cod'] == '404':
        message = f'City "{city}" not found!'
        return render_template('index.html', message=message)
    else:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('weather.html', weather=weather_data)
 
if __name__ == '__main__':
    app.run()