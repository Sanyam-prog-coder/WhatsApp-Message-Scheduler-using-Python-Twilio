# Compilling process
"""
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install twilio
python3 main.py

"""

# step 1 install required liabraries

from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step 2 twilio creadentials

account_sid = 'AC769ca928c8e1648d1c2a3d6a828397e5'
auth_token = 'ef745867830600740226590c78e71f24'

client = Client(account_sid, auth_token)

# step 3 degine send message function\

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_ = 'whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{recipient_number}'
        )
        print(f'message sent succesfully! Message SID{message.sid}')
    except Exception as e:
        print(f"Error: {e}")

# step 4 user input 

name = input("Enter the recipient name : ")
recipient_number = input("Enter the recipient whatsapp number with country code : ")
message_body = input(f"Enter the message you want to send to {name} : ")

# step 5 parse date / time and calculater delay

date_str = input("Enter the data to send the message (YYYY-MM-DD) : ")
time_str = input("Enter the time to send the message (HH:MM) : ")

# datetime 

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# calculate delay

time_diffrence = schedule_datetime - current_datetime
delay_second = time_diffrence.total_seconds()

if delay_second <= 0:
    print("The specified time is in past. please enter a future date and time: ")
else:
    print(f'Message schedule to be sent to {name} at sheduled {schedule_datetime}.')

    # wait untile the shedule time
    time.sleep(delay_second) # 1000

    # send the message
    send_whatsapp_message(recipient_number, message_body)