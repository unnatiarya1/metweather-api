# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files to container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run migrations and server on container start
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
