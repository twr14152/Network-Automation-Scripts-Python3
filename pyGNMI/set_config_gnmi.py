from pygnmi.client import gNMIclient
import json

host_list = input("Enter host or hosts separated by ',': ")
hosts = [i.strip() for i in host_list.split(",")] 
PORT = 6030
USERNAME = "admin"
PASSWORD = "admin"

def main():
    for host in hosts:
        print("Add/Change interface description")
        intf = input("Enter interface: ")
        path = f"/interfaces/interface[name={intf}]/config/description"
        value = input("Enter interface description: ")
        target = (f"clab-lab3-{host}", PORT)
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
