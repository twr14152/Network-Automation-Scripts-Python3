#!/usr/bin/python3.12

import requests
import json

username = "admin"
password = "NokiaSrl1!"

def all_nodes():
    nodes = ["leaf1", "leaf2", "spine"]
    commands = input("Enter commands seperated by ',': ")
    cli_commands = commands.split(",")
    for node in nodes:
        url = f"http://{node}/jsonrpc"
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

def node():
    node = input("Enter node: ")
    url = f"http://{node}/jsonrpc"
    
    commands = input("Enter commands seperated by ',': ")
    cli_commands = commands.split(",")

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


def main():
    ans = input("Log in to all nodes (y/n): ")
    if ans == "y":
        all_nodes()
    else:
        node()


if __name__ == "__main__":
    main()


