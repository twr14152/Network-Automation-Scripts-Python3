import requests
import json


url = "http://clab-lab1-sw2/jsonrpc"
username = "admin"
password = "NokiaSrl1!"


set_commands = [
    # set ospf version
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/version",
        "value": "ospf-v2"
    },
    # set ospf router id
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/router-id",
        "value": "2.2.2.2"
    },
    # add interface to ospf
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]",
        "value": {}
    },
    # set interface to be point-to-point network in ospf
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/interface-type",
        "value": "point-to-point"
    },
    # enable interface in ospf
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/admin-state",
        "value": "enable"
    }
]


payload = {
    "jsonrpc": "2.0",
    "method": "set",
    "params": {
        "commands": set_commands,
        "output-format": "json"  
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


