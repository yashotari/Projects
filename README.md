# Algorithmic Trading
Algorithmic Trading is when people use mathematical algorithms and predefined strategies to trade in the stock market. This way of trading is faster, more efficient and more consistent than manual trading. It’s like you’re playing a game where you need to make quick decisions, and a predefined strategy can help you make those decisions faster and better.
# Weather Forecast Web Application

This web application allows users to retrieve weather forecasts for specific cities using the OpenWeatherMap API.
The app displays a 5-day forecast for the selected city, presenting information such as temperature, humidity, pressure, and weather description.

## Features

- Search by City: Users can input a city name to get a 5-day/3 hr weather forecast.
- Display Weather Information: Provides detailed weather information including temperature, humidity, pressure, etc.
- MySQL Integration: Stores weather forecast data in a MySQL database for historical tracking.

## Technologies Used

- Flask: Backend server framework for handling HTTP requests and responses.
- MySQL: Database for storing weather forecast data.
- OpenWeatherMap API: External API used to retrieve weather forecast information.
- HTML/CSS: Frontend templates for user interface.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/PriyadarshiniJadhav/weather_forecast.git
2. Install dependencies: `pip install -r requirements.txt`
3. Set up a MySQL database and configure the connection in `app.py`.
4. Obtain an API key from OpenWeatherMap and replace `api_key` in `app.py`.
5. Run the application: `python app.py`

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Enter a city name in the search box and click 'Search'.
3. View the weather forecast details displayed on the webpage.


## Acknowledgments

This project utilizes weather data provided by OpenWeather (https://openweathermap.org/) through their API.
We express our gratitude for their valuable service that enables us to access weather forecasts and integrate weather information into this project.
