import requests
from django.conf import settings
import json

def send_pattern_sms(mobile_number, pattern_code, otp_code):
    
    url = "https://api.mediana.ir/sms/v1/send/pattern"

    payload = json.dumps({
    "recipients": [
         str(mobile_number),
     ],
     "patternCode": "800128",
     "parameters": {
      "otp": str(otp_code),
        }
    })
    headers = {
    'Content-Type': 'application/json',
     'Accept': 'text/plain',
     'Authorization': f"Bearer {settings.MEDIANA_API_KEY}"
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)

    

    
    
    
  
def send_pattern_sms_order(mobile_number, pattern_code, parameters):
    
    url = "https://api.mediana.ir/sms/v1/send/pattern"

    payload = json.dumps({
    "recipients": [
         str(mobile_number),
     ],
     "patternCode": pattern_code,
     "parameters": parameters
    })
    
    
    
    
    headers = {
    'Content-Type': 'application/json',
     'Accept': 'text/plain',
     'Authorization': f"Bearer {settings.MEDIANA_API_KEY}"
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)

     
    

    return response
    
    
    
    
    
