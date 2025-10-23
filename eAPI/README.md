# eAPI
- A simple way to interface with arista using requests and jsonrpc. 
- It only uses POST for runCmds method.
- The only challenging thing about it is formating the output of the data


The first script uses requests and is written with more explicit code. You can see the data format. 
```
script.py 
```
Sample output
```
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/controller$ python lab_script.py 
Enter host or hostnames separated by ',': ceos1, ceos2, ceos3
Enter commands to run seperated by ",": show hostname
Connected to ceos1..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {
      "hostname": "ceos1",
      "fqdn": "ceos1"
    }
  ]
}
Closing connection to ceos1...


Connected to ceos2..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {
      "hostname": "ceos2",
      "fqdn": "ceos2"
    }
  ]
}
Closing connection to ceos2...


Connected to ceos3..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {
      "hostname": "ceos3",
      "fqdn": "ceos3"
    }
  ]
}
Closing connection to ceos3...
```
The other script is just uses jsonrpclib (instead of requests) to run commands on the device. There is a little more implicit with its code. You do not see the data format for the commands being sent. Its more implicit. 
```
lab_script_2.py
```
```
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/controller$ python lab_script_2.py 
Enter host or hosts separated by ',': ceos1, ceos2, ceos3
Enter commands: show hostname
[
  {
    "hostname": "ceos1",
    "fqdn": "ceos1"
  }
]
[
  {
    "hostname": "ceos2",
    "fqdn": "ceos2"
  }
]
[
  {
    "hostname": "ceos3",
    "fqdn": "ceos3"
  }
]
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/controller$ 
```


