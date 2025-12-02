import requests
import json


node = input("Enter node: ")
url = f"http://clab-lab2-{node}/jsonrpc"

commands = input("Enter commands seperated by ',': ")
cli_commands = commands.split(",")



username = "admin"
password = "NokiaSrl1!"


payload = {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
        "commands": cli_commands,
        "output-format": "json" # "text" is bascially unreadable dont use....
    },
    "id":1
}

try:
    print(f"Connecting to {node}")
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


