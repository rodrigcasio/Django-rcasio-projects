# using the official python image
FROM python:3.12-slim

# setting environment variables
ENV DOCKER_RUNNING=True
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# setting work directory
WORKDIR /app

# install system dependecies for PostgreSQL (psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# install dependecies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#  copy the project 
COPY . /app/

# expose port 8000
EXPOSE 8000

# start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
