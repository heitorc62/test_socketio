FROM python:3.10
EXPOSE 5000
WORKDIR /test_app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["python3", "-u", "run.py"]