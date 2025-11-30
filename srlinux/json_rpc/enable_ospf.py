import requests
import json

url_sw1 = "http://clab-lab1-sw1/jsonrpc"
url_sw2 = "http://clab-lab1-sw2/jsonrpc"
username = "admin"
password = "NokiaSrl1!"


sw1_set_commands = [
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/version",
        "value": "ospf-v2"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/router-id",
        "value": "1.1.1.1"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]",
        "value": {}
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/interface-type",
        "value": "point-to-point"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/admin-state",
        "value": "enable"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/admin-state",
        "value": "enable"
    }

]



sw2_set_commands = [
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/version",
        "value": "ospf-v2"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/router-id",
        "value": "2.2.2.2"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]",
        "value": {}
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/interface-type",
        "value": "point-to-point"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/admin-state",
        "value": "enable"
    },
    {
        "action": "update",
        "path": "/network-instance[name=default]/protocols/ospf/instance[name=default]/admin-state",
        "value": "enable"
    }

]


payload_sw1 = {
    "jsonrpc": "2.0",
    "method": "set",
    "params": {
        "commands": sw1_set_commands,
        "output-format": "json" 
    },
    "id": 1
}


payload_sw2 = {
    "jsonrpc": "2.0",
    "method": "set",
    "params": {
        "commands": sw2_set_commands,
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

