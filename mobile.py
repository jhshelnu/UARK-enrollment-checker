from time import sleep
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
    'cache-control': "no-cache",
    'Postman-Token': ""
    }
pattern = re.compile('<td class=\"EnrolledSize\">([0-9]*?)/([0-9]*?)</td>');
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

while True: 
	response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
	match = pattern.search(response.text)

	if (match.group(1) != match.group(2)):
		break

	sleep(600)

message = client.messages.create(
    body="Hey go enroll in Mobile! http://uaconnect.uark.edu/",
    from_='',
    to=''
)
