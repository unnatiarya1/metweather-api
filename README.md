# 🌦️ UK MetOffice Climate API

A Django-based application that **parses UK weather data** from the MetOffice and **exposes it via a RESTful API**.  
Data includes monthly climate summaries such as **Tmax**, **Tmin**, **Rainfall**, etc.

> ✅ Built with Django + Django REST Framework  
> 🐳 Dockerized and deployed on Render  
> 🌐 Public API access + optional frontend dashboard

---

## 📌 Features

- ✅ Parse climate datasets (e.g., Tmax) from UK MetOffice `.txt` files
- ✅ Save structured monthly data to the database
- ✅ Serve data via RESTful API: `/api/climate/`
- ✅ Dockerized for easy deployment
- ✅ Fetches data automatically at startup

---

## 🖼️ API Demo

```http
GET /api/climate/

Example Response:

[
  {
    "region": "UK",
    "parameter": "Tmax",
    "year": 2023,
    "month": 6,
    "value": 18.9
  },
  {
    "region": "UK",
    "parameter": "Tmax",
    "year": 2023,
    "month": 7,
    "value": 19.1
  }
]

🛠️ Local Setup (Without Docker)

git clone https://github.com/unnatiarya/metweather-api.git
cd metweather-api

# Set up virtual env
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

# Setup DB and fetch weather data
python manage.py migrate
python manage.py fetch_climate_data

# Run the server
python manage.py runserver


🐳 Docker Setup

Build and run the project in Docker:
docker-compose up --build

This automatically:
Applies migrations
Fetches weather data from MetOffice
Starts the Django API server on port 8000

Then visit:
👉 http://localhost:8000/api/climate/

🧪 Run Tests
python manage.py test

🌐 Deployment
Deployed on Render:

Build: uses Dockerfile

Start command: defined in Dockerfile (migrate + fetch + runserver)

Live API: https://metweather-api.onrender.com/api/climate/