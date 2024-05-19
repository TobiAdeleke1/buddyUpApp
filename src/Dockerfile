# pull official base image
FROM python:3.11.4

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED=1 

WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y netcat-traditional

COPY . .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8080

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]



CMD ["python", "manage.py", "run","--host", "0.0.0.0"] 