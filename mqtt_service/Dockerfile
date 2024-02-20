FROM python:3.10
EXPOSE 1883
WORKDIR /mqtt_app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["python3", "-u", "mqtt.py"]
