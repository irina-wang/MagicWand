# Govel API reference: 
    # https://govee-public.s3.amazonaws.com/developer-docs/GoveeDeveloperAPIReference.pdf

import json
from urllib import response
import requests
from urllib.error import HTTPError

# 
# "supportCmds":["turn","brightness","color","colorTem"]
# =====================================
#  Cmd = ['turn' : on/off,
#         'color': r/g/b, 0-255,
#         'brightness': 0-100
#         'colorTem': depends on the app']
#


DEVICE_1 = {}; # LED Strip
DEVICE_2 = {}; # Light bulb


# myAPIkey = {'Govee-API-Key': 'a874519a-5251-475a-9f5b-f42a25786756'};

myAPIkey = {'Govee-API-Key': 'bd1f7b63-3a70-4528-adee-225e014d3499'};

putUrl = 'https://developer-api.govee.com/v1/devices/control'


def GET_info():
    response = requests.get(
        url='https://developer-api.govee.com/v1/devices', 
        headers=myAPIkey
    );

    if response.ok:
        objInfo = json.loads(response.text);
        DEVICE_1 = objInfo['data']['devices'][0]
        DEVICE_2 = objInfo['data']['devices'][1]
    
    return (DEVICE_1, DEVICE_2)


def ok(self):
    """Returns True if :attr:`status_code` is less than 400, False if not.

    This attribute checks if the status code of the response is between
    400 and 600 to see if there was a client error or a server error. If
    the status code is between 200 and 400, this will return True. This
    is **not** a check to see if the response code is ``200 OK``.
    """
    try:
        self.raise_for_status()
    except HTTPError:
        return False
    return True


# light_status = ['on', 'off']
def POST_Switch(device, light_status):
    requests_body = {
        'device': device['device'],
        'model': device['model'],
        'cmd': {
            'name': 'turn', 
            'value': light_status
    }};

    print(requests.put(putUrl, headers=myAPIkey, json=requests_body));


# r = [0:255]
# g = [0:255]
# b = [0:255]
def POST_Color(device, r, g, b):
    requests_body = {
        'device': device['device'],
        'model': device['model'],
        'cmd': {
            "name": "color",
             "value": {
                "r": r,
                "g": g,
                "b": b
    }}};

    requests.put(putUrl, headers=myAPIkey, json=requests_body);
   

# brightness = [0:100]
def POST_Brightness(device, brightness):
    requests_body = {
        'device': device['device'],
        'model': device['model'],
        'cmd': { 
            "name": "brightness",
            "value": brightness
    }};

    requests.put(putUrl, headers=myAPIkey, json=requests_body);

# brightness = [0:100]
def POST_ColorTem(device, temperature):
    colorTemRange = device['properties']['colorTem']['range'];
    if temperature <=  colorTemRange['min'] or temperature >=  colorTemRange['max']:
        print('POST_ColorTem request out of range')
        return 
    
    requests_body = {
        'device': device['device'],
        'model': device['model'],
        'cmd': { 
            "name": "colorTem",
            "value": temperature
    }};

    requests.put(putUrl, headers=myAPIkey, json=requests_body);


if __name__ == '__main__': 
# # function calls 
    (DEVICE_1,DEVICE_2) = GET_info();
    print(DEVICE_1)
    POST_Switch(DEVICE_1, 'on');
    # POST_turnOn(DEVICE_2, 'on');
    # POST_Color(DEVICE_1, 255,3,255);
    POST_Brightness(DEVICE_1,50);
    POST_Brightness(DEVICE_1,100);
    # POST_Switch(DEVICE_1, 'off');