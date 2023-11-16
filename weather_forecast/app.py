from flask import Flask, render_template, request
import mysql.connector
import requests


app = Flask(__name__)

# Configure your MySQL connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="priya999",
    database="weather_forecast"
)
@app.route("/")
def fun1():
    return render_template('forecast.html')

@app.route('/forecast', methods=['POST', 'GET'])
def fun2():
   
    if request.method == 'POST':
        city = request.form['city']
    

    api_key= 'e9cc596bc286ddf93f63ec4302bad38c'
    
    
    # Construct the API request URL with your API key
    forecast_data = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}').json()
    
    #forecast['city'] = city
   
         
            # Extract relevant weather data
    forecast_data_list = []
    for forecast in forecast_data['list']:
        forecast_info = {
            "name": city,
            "datetime": forecast['dt_txt'],
            "country_code": forecast_data['city']['country'],  # Different structure for country code
            "coordinate": f"{forecast_data['city']['coord']['lon']}, {forecast_data['city']['coord']['lat']}",  # Different structure for coordinate
            "description": forecast['weather'][0]['description'],
            "temperature": "{:.1f}".format(forecast['main']['temp'] - 273.15),
            "temp_min": "{:.1f}".format(forecast['main']['temp_min'] - 273.15),
            "temp_max": "{:.1f}".format(forecast['main']['temp_max'] - 273.15),
            "pressure": forecast['main']['pressure'],
            "humidity": forecast['main']['humidity']
        }
        forecast_data_list.append(forecast_info)

    # Insert the weather data into the MySQL database
    cursor = db.cursor()

    for forecast in forecast_data_list:
        cursor.execute("""
            INSERT INTO forecast_data (city_name, date_time, country_code, coordinate, description, temperature, temp_min, temp_max, pressure, humidity)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            forecast['name'],
            forecast['datetime'],
            forecast['country_code'],
            forecast['coordinate'],
            forecast['description'],
            forecast['temperature'],
            forecast['temp_min'],
            forecast['temp_max'],
            forecast['pressure'],
            forecast['humidity']
        ))

    db.commit()
    cursor.close()

    return render_template('forecast.html', forecast_data_list=forecast_data_list)
    
        

if __name__ == '__main__':
    app.run(debug=True)
