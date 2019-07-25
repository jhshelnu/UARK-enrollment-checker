FROM twilio/twilio-python:6.29.1

COPY mobile.py secrets.py ./

CMD ["python3", "mobile.py"]
