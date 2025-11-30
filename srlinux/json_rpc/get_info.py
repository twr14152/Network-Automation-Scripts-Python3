import requests
import json

url_sw1 = "http://clab-lab1-sw1/jsonrpc"
url_sw2 = "http://clab-lab1-sw2/jsonrpc"
username = "admin"
password = "NokiaSrl1!"


sw1_get_commands = [
   {
    "path": "/system/information/version"
   },
]



sw2_set_commands = [
    {
     "path": "/system/information/version"
    }
]


payload_sw1 = {
    "jsonrpc": "2.0",
    "method": "get",
    "params": {
        "commands": sw1_get_commands,
        "output-format": "json" 
    },
    "id": 1
}


payload_sw2 = {
    "jsonrpc": "2.0",
    "method": "get",
    "params": {
        "commands": sw2_get_commands,
        "output-format": "json"
    },
    "id": 1
}


try:
    response = requests.post(
            url_sw1,
            data=json.dumps(payload_sw1),
            auth=(username, password),
            headers={"Content-Type": "application/json"},
            verify=False,
            timeout=5
            )
    print(response.status_code)
    print(json.dumps(response.json(), indent=2))
except requests.exceptions.RequestException as e:
    print("Error: ", e)



try:
    response = requests.post(
            url_sw2,
            data=json.dumps(payload_sw2),
            auth=(username, password),
            headers={"Content-Type": "application/json"},
            verify=False,
            timeout=5
            )
    print(response.status_code)
    print(json.dumps(response.json(), indent=2))
except requests.exceptions.RequestException as e:
    print("Error: ", e)
