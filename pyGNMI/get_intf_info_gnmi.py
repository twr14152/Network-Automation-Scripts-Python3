from pygnmi.client import gNMIclient
import json

host_list = input("Enter host or hosts separated by ',': ")
hosts = [i.strip() for i in host_list.split(",")] 
PORT = 6030
USERNAME = "admin"
PASSWORD = "admin"


interface = input("Enter target interface (example Ethernet1):")
intf_settings = input("What do you want to look at (config, state, counters, capabilities): ")

'''
/interfaces
/interfaces/interface[name]/config
/interfaces/interface[name]/state
/interfaces/interface[name]/subinterfaces/subinterface[index]/config
/interfaces/interface[name]/subinterfaces/subinterface[index]/state
/interfaces/interface[name]/state/counters
'''

config_path = f"/interfaces/interface[name={interface}]/config"
state_path = f"/interfaces/interface[name={interface}]/state"
counters_path = f"/interfaces/interface[name={interface}]/state/counters"


def main():
        for host in hosts:
            target = (f"clab-lab3-{host}", PORT)
            #target = (HOST, PORT)
            with gNMIclient(target=target, username=USERNAME, password=PASSWORD, insecure=True) as gc:
                try:
                    if intf_settings == "config":
                        result = gc.get(path=[config_path], encoding="json_ietf")
                        print(f"{host} interface configuration:")
                        print(json.dumps(result, indent=2))
                    elif intf_settings == "state":
                        result = gc.get(path=[state_path], encoding="json_ietf")
                        print(f"{host} interface status:")
                        print(json.dumps(result, indent=2))
                    elif intf_settings == "counters":
                        result = gc.get(path=[counters_path], encoding="json_ietf")
                        print(f"{host} interface counters:")
                        print(json.dumps(result, indent=2))
                    elif intf_settings == "capabilities":
                        result = gc.capabilities()
                        print(f"{HOST} capabilities:")
                        print(json.dumps(result, indent=2))
                except Exception as e:
                    print("Error performing gNMI get:", e)

if __name__ == "__main__":
    main()



