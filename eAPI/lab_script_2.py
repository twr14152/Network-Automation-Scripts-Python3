from jsonrpclib import Server
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

host_list = input("Enter host or hosts separated by ',': ")
hosts = [i.strip() for i in host_list.split(",")] 

commands = input("Enter commands: ")
cmds = commands.split(",")

for host in hosts:
    switch = Server(f"https://admin:admin@clab-lab3-{host}/command-api")
    response = switch.runCmds( 1, cmds )
    print(json.dumps(response, indent=2))

