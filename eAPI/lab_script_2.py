from jsonrpclib import Server
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context

commands = input("Enter commands: ")
cmds = commands.split(",")

switch = Server( 'https://admin:admin@clab-lab3-ceos1/command-api' )
response = switch.runCmds( 1, cmds )
print(json.dumps(response, indent=2))
