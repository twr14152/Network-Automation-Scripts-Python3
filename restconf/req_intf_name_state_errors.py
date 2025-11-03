import requests
import json

requests.packages.urllib3.disable_warnings()

host = input("Enter host: ")
intf = input("Enter interface you want to check: ")

url = f"https://{host}:6020/restconf/data/openconfig-interfaces:interfaces/interface={intf}/state"
resp = requests.get(url, auth=("admin", "admin"), verify=False, headers={"Accept": "application/yang-data+json"})
data = resp.json()

interface_name = data["openconfig-interfaces:name"]
admin_status = data["openconfig-interfaces:admin-status"]
counters = data["openconfig-interfaces:counters"]

print(f"Interface: {interface_name}")
print(f"Status: {admin_status}")
print(f"In Packets: {counters['in-pkts']}")
print(f"Out Packets: {counters['out-pkts']}")
print(f"In Discards: {counters['in-discards']}")
print(f"In Errors: {counters['in-errors']}")
print(f"Out Discards: {counters['out-discards']}")
print(f"Out Errors: {counters['out-errors']}")
