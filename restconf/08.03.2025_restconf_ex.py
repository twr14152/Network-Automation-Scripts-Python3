import requests
import json

requests.packages.urllib3.disable_warnings()

HOST = "devnetsandboxiosxec8k.cisco.com"
USER = "<>"
PW = "<>"

interface_name = "Loopback72"
url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces/interface={interface_name}"

headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
}

data = {
    "ietf-interfaces:interface": {
        "name": interface_name,
        "description": "configured via RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.72.72.72",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

# POST to create the interface
post_response = requests.put(url, auth=(USER, PW), verify=False, headers=headers, data=json.dumps(data))
print("POST/PUT response:")
print(post_response.status_code)
print(post_response.text)

# GET all interfaces
get_url = f"https://{HOST}/restconf/data/ietf-interfaces:interfaces"
get_response = requests.get(get_url, headers=headers, auth=(USER, PW), verify=False)
print("\nGET response:")
print(get_response.status_code)
print(get_response.text)

