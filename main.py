import requests
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv

def config():   
    load_dotenv()


config()

#------------------Consent variable-----------------#
API_KEY = os.getenv('api_key')
LAT = 27.7166
LONG =  85.3485
URL = ' https://api.weatherapi.com/v1/forecast.json??'

SENDER = os.getenv("sender")
PASSCODE = os.getenv('pass')
RECEVER = os.getenv("rec")


#------------------paremeter-----------------#
parm = {
    'q':'Kathmandu,Chabahil,Nepal',
    'exclude':'current,daily',
    'key':API_KEY,
}

 

#--------------------------time-------------------------#
time = dt.datetime.now()


#----------main-------------#
server_request = requests.get(url=URL,params=parm)
server_request.raise_for_status()
raw_data = server_request.json()['forecast']['forecastday'][0]['hour']
required_new_data = [raw_data[i] for i in range(7,20)]
for i in range(len(required_new_data)):
    if required_new_data[i]['will_it_rain'] == 1:     
        with smtplib.SMTP('smtp.gmail.com',587,timeout=120) as conection:
            message = f"Subject:Weather Alert.\n\n\nDear Student,\n\nIt will rain today bring an umberalla.\n\nYours favourite creation,\n\nBot."
            conection.starttls()
            conection.login(user=SENDER,password=PASSCODE)
            conection.sendmail(from_addr=SENDER,to_addrs=RECEVER,msg=message)
        break

        




