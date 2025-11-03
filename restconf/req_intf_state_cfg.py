import requests
import json

USER = "admin"
PASS = "admin"
HOST = input("Enter device: ")
INTF = input("Enter interface (example Ethernet1..): ")
num = int(input("You want the config (press 1) or state (press 2): "))

requests.packages.urllib3.disable_warnings()

headers = {'Accept': 'application/yang-data+json'}

url_1 = f"https://{HOST}:6020/restconf/data/openconfig-interfaces:interfaces/interface={INTF}/config"
url_2 = f"https://{HOST}:6020/restconf/data/openconfig-interfaces:interfaces/interface={INTF}/state"
url_3 = "tbd"

if num == 1:
    result = requests.get(url_1, auth=(USER, PASS), headers=headers, verify=False)
    print(result.status_code)
    data = result.json()
    print(json.dumps(data, indent=2))

elif num == 2:
    result = requests.get(url_2, auth=(USER, PASS), headers=headers, verify=False)
    print(result.status_code)
    data = result.json()
    print(json.dumps(data, indent=2))

else:
    pass


