FROM twilio/twilio-python:6.29.1

COPY . .

CMD ["python3", "mobile.py"]
