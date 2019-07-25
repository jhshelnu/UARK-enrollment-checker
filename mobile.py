import secrets
from time import sleep
from datetime import datetime
from pytz import timezone
from twilio.rest import Client
import requests
import re

url = "https://scheduleofclasses.uark.edu/Main"
querystring = {"strm":"1199"}
payload = "campus=FAY&subject=CSCE&catalog_nbr1=4623&class_section=001&Search=Search&undefined="
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "en-US,en;q=0.9",
    'cache-control': "no-cache"
    }
pattern = re.compile('<td class="EnrolledSize">(\d+)/(\d+)</td>');
client = Client(secrets.account_sid, secrets.auth_token)

while True: 
	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	match = pattern.search(response.text)
	# print(response.text)
	print(match.group(1) + '/' + match.group(2), end='\t')
	print(datetime.now(timezone('US/Eastern')).strftime("(%B %d %I:%M:%S%p)"))

	if (match.group(1) != match.group(2)):
		break

	sleep(1800)

client.messages.create(
    body="Hey go enroll in Mobile! http://uaconnect.uark.edu/",
    from_=secrets.phone_number_from,
    to=secrets.phone_number_to)
