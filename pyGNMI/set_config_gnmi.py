from pygnmi.client import gNMIclient
import json


HOST = "clab-lab3-ceos1"
PORT = 6030
USERNAME = "admin"
PASSWORD = "admin"

path = "/interfaces/interface[name=Ethernet1]/config/description"
value = "connected to ceos2"

def main():
    target = (HOST, PORT)
    with gNMIclient(target=target, username=USERNAME, password=PASSWORD, insecure=True) as gc:
        config = [(path, json.dumps(value))]
        try:
            resp = gc.set(update=config)
            print("Set response:")
            print(resp)
        except Exception as e:
            print("Error performing gNMI set:", e)

if __name__ == "__main__":
    main()
