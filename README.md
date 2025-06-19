# 🌦️ UK MetWeather API (Django + Docker + Render)

A Django-based backend application to **fetch, parse, store, and serve summarized UK climate data (Tmax)** from the UK MetOffice as a public REST API. The project is Dockerized, tested, and deployed to the cloud.

---

## 🔗 Live Demo

- 🛰️ API Endpoint: [https://metweather-api.onrender.com/api/climate/](https://metweather-api.onrender.com/api/climate/)
- 📊 (Optional) Frontend: Visualized via Streamlit (`streamlit_app.py`)

---

## 📌 Features

✅ Fetches historical Tmax temperature data (UK region)  
✅ Parses `.txt` format directly from MetOffice  
✅ Saves to local database via Django ORM  
✅ RESTful API using Django REST Framework  
✅ API supports filtering by year, month, region, and parameter  
✅ Fully Dockerized  
✅ Deployed to Render cloud  
✅ Includes unit tests  
✅ (Bonus) Optional Streamlit UI for graph-based visualization

---

## 📚 Dataset Source

UK Met Office Climate Data → [Tmax Dataset (UK)](https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt)

---

## ⚙️ Tech Stack

- Django 4.2
- Django REST Framework
- Docker
- SQLite (default DB)
- Render (for deployment)
- Streamlit (optional UI)

---

## 🚀 Local Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/unnatiarya1/metweather-api.git
   cd metweather-api


2. Create and activate a virtual environment
  python -m venv venv
  venv\Scripts\activate  # On Windows

3. Install dependencies
  pip install -r requirements.txt

4. Apply migrations
  python manage.py migrate

5. Fetch and populate weather data
  python manage.py fetch_climate_data

6. Run the development server
  python manage.py runserver

7. View API
  Go to: http://127.0.0.1:8000/api/climate/

🧪 Run Tests
  python manage.py test


🐳 Docker Setup

🔧 Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["sh", "-c", "python manage.py migrate && python manage.py fetch_climate_data && python manage.py runserver 0.0.0.0:8000"]

📜 requirements.txt
Django>=4.2,<5.0
djangorestframework>=3.14.0
requests>=2.31.0
django-filter>=23.5

📦 Build and Run Docker Image
docker build -t metweather .
docker run -p 8000:8000 metweather

Then open http://localhost:8000/api/climate/

☁️ Cloud Deployment (Render)

1. Push to GitHub: https://github.com/unnatiarya1/metweather-api
2. Go to https://render.com
3. New → Web Service
  Build Type: Docker
  Root directory: / (leave blank)
  Start command: use CMD from Dockerfile

5. Set ALLOWED_HOSTS in settings.py:
ALLOWED_HOSTS = ['metweather-api.onrender.com']

✅ After deployment:
Access your live API at https://metweather-api.onrender.com/api/climate/

🎁 Bonus: Frontend Visualization with Streamlit
streamlit_app.py is included in the repo.

👁️ To Run Locally
pip install streamlit altair pandas requests
streamlit run streamlit_app.py

📂 Directory Structure
metweather-api/
├── climate/
│   ├── management/commands/fetch_climate_data.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── tests.py
├── metweather/
│   └── settings.py
├── requirements.txt
├── Dockerfile
├── streamlit_app.py
└── manage.py


