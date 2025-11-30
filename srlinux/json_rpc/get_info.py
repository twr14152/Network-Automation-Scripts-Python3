import requests
import json

url_sw1 = "http://clab-lab1-sw1/jsonrpc"
url_sw2 = "http://clab-lab1-sw2/jsonrpc"
username = "admin"
password = "NokiaSrl1!"


sw1_ospf_nei = "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/neighbor"

sw2_ospf_nei = "/network-instance[name=default]/protocols/ospf/instance[name=default]/area[area-id=0.0.0.0]/interface[interface-name=ethernet-1/1.0]/neighbor"



payload_sw1 = {
    "jsonrpc": "2.0",
    "method": "get",
    "params": {
        "datastore": "state",
        "commands": [
            {"path": sw1_ospf_nei},
            ],
        "recursive": True
    },
    "id": 1
}


payload_sw2 = {
    "jsonrpc": "2.0",
    "method": "get",
    "params": {
        "datastore": "state",
        "commands": [
            {"path": sw2_ospf_nei},
            ],
        "recursive": True
    },
    "id": 1
}


try:
    print("sw1: ")
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
    print("sw2: ")
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

