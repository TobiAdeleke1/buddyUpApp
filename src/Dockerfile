# pull official base image
FROM python:3.11.4

# Set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED=1 

# install system dependencies
RUN apt-get update && \
        apt-get install -y netcat-traditional

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app

EXPOSE 8080

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["sh","/entrypoint.sh"]


CMD ["python", "manage.py", "run","--host", "0.0.0.0"] 