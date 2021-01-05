
import time
from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages

file_nr = open("telefon.txt")
file_message = open("message.txt", 'r', encoding='utf-8')

numbers = file_nr.read().splitlines() 
messages = file_message.read().splitlines() 
ipadress = input("IP adress?: ")

i = 0
ipo = 0

for lines in messages:
    i += 1

while ipo < i:


    ip = IPv4Address(ipadress)  # let's create an IP address object
    # now create a session
    session = AirmoreSession(ip)
    # if your port is not 2333
    # session = AirmoreSession(ip, 2334)  # assuming it is 2334

    session.is_server_running  # True if Airmore is running

    was_accepted = session.request_authorization()

    print(was_accepted)

    service = MessagingService(session)

    message_text = messages[ipo]

    mobile_nr = numbers[ipo]

    service.send_message(mobile_nr, message_text)

    time.sleep(1)

    ipo += 1