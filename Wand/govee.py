# Govee-API-Key : {a874519a-5251-475a-9f5b-f42a25786756} // Irina's API key
# Content-Type : application/json

import requests

# LED Strip
#   'device': 'E0:A1:A4:C1:38:29:53:41'

myAPIkey = {'Govee-API-Key': 'a874519a-5251-475a-9f5b-f42a25786756'};
turnOn = {'device': 'E0:A1:A4:C1:38:29:53:41',
         'model' :'H6160',
         'cmd': 
            {'name': 'turn', 
            'value': 'on'}};


myAPIkey = {'Govee-API-Key': 'a874519a-5251-475a-9f5b-f42a25786756'};

turnOn = {'device': 'E0:A1:A4:C1:38:29:53:41',
         'model' :'H6160',
         'cmd': 
            {'name': 'turn', 
            'value': 'on'}};

turnOff = {'device': 'E0:A1:A4:C1:38:29:53:41',
         'model' :'H6160',
         'cmd': 
            {'name': 'turn', 
            'value': 'off'}};


Color = {'device': 'E0:A1:A4:C1:38:29:53:41',
         'model' :'H6160',
         'cmd': 
            {"name": "color",
             "value": {
                "r": 255,
                "g": 255,
                "b": 255
            }}};


ColorTem = {'device': 'E0:A1:A4:C1:38:29:53:41',
            'model' :'H6160',
            'cmd': 
                { 
                "name": "colorTem",
                'value': 2000
                }};



Brightness = {'device': 'E0:A1:A4:C1:38:29:53:41',
            'model' :'H6160',
            'cmd': 
                { 
                "name": "brightness",
                "value": 10
                }};




# "supportCmds":["turn","brightness","color","colorTem"]


# When cmd.name is "brightness":
#  the valid values are between 0 and 100, and 0 will turn off the device
#  Type: number


# x = requests.get('https://developer-api.govee.com/v1/devices', headers={'Govee-API-Key': 'a874519a-5251-475a-9f5b-f42a25786756'});
# x = requests.put('https://developer-api.govee.com/v1/devices/control', headers=myAPIkey, json=turnOn);

x = requests.put('https://developer-api.govee.com/v1/devices/control', headers=myAPIkey, json=Brightness);
print(x.text)

