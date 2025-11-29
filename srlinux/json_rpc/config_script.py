import requests
import json


url = "http://clab-lab1-sw1/jsonrpc"
username = "admin"
password = "NokiaSrl1!"

# List of set commands

set_commands = [
        {
                "action": "update",
                #"path": "/interface[name=mgmt0]/description:set-via-json-rpc"
                "path": "/interface[name=ethernet-1/1]/subinterface[index=0]/description: connection to sw2"

            }
]

payload = {
    "jsonrpc": "2.0",
    "method": "set",
    "params": {
        "commands": set_commands,
        "output-format": "json"  # or "text" if you prefer
    },
    "id": 1
}

try:
    response = requests.post(
            url,
            data=json.dumps(payload),
            auth=(username, password),
            headers={"Content-Type": "application/json"},
            verify=False,
            timeout=5
    )
    print(response.status_code)
    print(json.dumps(response.json(), indent=2))
except requests.exceptions.RequestException as e:
    print("Error: ", e)

