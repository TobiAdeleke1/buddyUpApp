FROM python:3.11.4

ENV PYTHONBUFFERED=1 

WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:create_app()", "--log-level", "debug"]
