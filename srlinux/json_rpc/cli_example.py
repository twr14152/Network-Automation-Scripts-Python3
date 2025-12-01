import requests
import json


url = "http://clab-lab1-sw2/jsonrpc"
username = "admin"
password = "NokiaSrl1!"

cli_commands = [
                "network-instance default",
                "info"
]

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




'''
todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/srlinux_labs/lab1/scripts$ python3 cli_example.py 
200
{
  "result": [
    {
      "name": "default",
      "interface": [
        {
          "name": "ethernet-1/1.0"
        }
      ],
      "protocols": {
        "ospf": {
          "instance": [
            {
              "name": "default",
              "admin-state": "enable",
              "version": "ospf-v2",
              "router-id": "2.2.2.2",
              "area": [
                {
                  "area-id": "0.0.0.0",
                  "interface": [
                    {
                      "interface-name": "ethernet-1/1.0",
                      "admin-state": "enable",
                      "interface-type": "point-to-point"
                    }
                  ]
                }
              ]
            }
          ]
        }
      }
    }
  ],
  "id": 1,
  "jsonrpc": "2.0"
}
'''

