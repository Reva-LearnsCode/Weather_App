🌦️ Weather Application

Project Description

A Python-based Weather Application that fetches real-time weather information using the OpenWeatherMap API.

Features

- Search weather by city name.
- Display temperature in Celsius.
- Display feels-like temperature.
- Show humidity.
- Show wind speed.
- Display weather description.
- Handle invalid city names.
- Handle invalid API keys.
- Handle network errors.
- Secure API key using environment variables.

Technologies Used

- Python
- OpenWeatherMap API
- Requests
- Python-dotenv

Project Structure

Weather_App/
│
├── weather.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

Installation

Install the required libraries:

pip install -r requirements.txt

How to Run

python weather.py

Enter a city name to view its weather information.

API Configuration

Create a ".env" file and add your OpenWeatherMap API key:

API_KEY=your_api_key

Note: Never upload your ".env" file or expose your API key publicly.

Author

Python Mini Project