import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host_list = input("Enter host or hostnames separated by ',': ")
hosts = [i.strip() for i in host_list.split(",")] #splits into a list and removes white space

commands = input('Enter commands to run seperated by ",": ')
cmds = commands.split(",")

for host in hosts:
    url = "https://clab-lab3-" + host + "/command-api"
    print(f"Connected to {host}..")
    headers = {'Content-Type': 'application/json'}
    payload = {
            "jsonrpc": "2.0",
            "method": "runCmds",
            "params": {
                "version": 1,
                "cmds": cmds,
                "format": "json"
                },
            "id": "1"
            }
    response = requests.post(url, data=json.dumps(payload), auth=('admin', 'admin'), verify=False)
    print(json.dumps(response.json(), indent=2))
    print(f"Closing connection to {host}...\n\n")

