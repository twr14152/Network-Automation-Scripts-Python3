# eAPI
- A simple way to interface with arista using jsonrpc. 
- It only uses POST for runCmds method.
- The only challenging thing about it is formating the output of the data
 

Sample output
```
$ python lab_script.py 
Enter device to connect to: clab-lab3-ceos1, clab-lab3-ceos2, clab-lab3-ceos3
Enter commands to run seperated by ",": enable, show lldp neighbors
Connected to clab-lab3-ceos1..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "tablesLastChangeTime": 1760877848.7299972,
      "tablesInserts": 5,
      "tablesDeletes": 1,
      "tablesDrops": 0,
      "tablesAgeOuts": 0,
      "lldpNeighbors": [
        {
          "port": "Ethernet1",
          "neighborDevice": "ceos2",
          "neighborPort": "Ethernet1",
          "ttl": 120
        },
        {
          "port": "Ethernet2",
          "neighborDevice": "ceos3",
          "neighborPort": "Ethernet1",
          "ttl": 120
        },
        {
          "port": "Management0",
          "neighborDevice": "ceos2",
          "neighborPort": "Management0",
          "ttl": 120
        },
        {
          "port": "Management0",
          "neighborDevice": "ceos3",
          "neighborPort": "Management0",
          "ttl": 120
        }
      ]
    }
  ]
}
Closing connection to clab-lab3-ceos1...


Connected to clab-lab3-ceos2..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "tablesLastChangeTime": 1760877838.4724617,
      "tablesInserts": 5,
      "tablesDeletes": 1,
      "tablesDrops": 0,
      "tablesAgeOuts": 0,
      "lldpNeighbors": [
        {
          "port": "Ethernet1",
          "neighborDevice": "ceos1",
          "neighborPort": "Ethernet1",
          "ttl": 120
        },
        {
          "port": "Ethernet2",
          "neighborDevice": "ceos3",
          "neighborPort": "Ethernet2",
          "ttl": 120
        },
        {
          "port": "Management0",
          "neighborDevice": "ceos1",
          "neighborPort": "Management0",
          "ttl": 120
        },
        {
          "port": "Management0",
          "neighborDevice": "ceos3",
          "neighborPort": "Management0",
          "ttl": 120
        }
      ]
    }
  ]
}
Closing connection to clab-lab3-ceos2...


Connected to clab-lab3-ceos3..
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "tablesLastChangeTime": 1760727895.270626,
      "tablesInserts": 4,
      "tablesDeletes": 0,
      "tablesDrops": 0,
      "tablesAgeOuts": 0,
      "lldpNeighbors": [
        {
          "port": "Ethernet1",
          "neighborDevice": "ceos1",
          "neighborPort": "Ethernet2",
          "ttl": 120
        },
        {
          "port": "Ethernet2",
          "neighborDevice": "ceos2",
          "neighborPort": "Ethernet2",
          "ttl": 120
        },
        {
          "port": "Management0",
          "neighborDevice": "ceos2",
          "neighborPort": "Management0",
          "ttl": 120
        },
        {
          "port": "Management0",
          "neighborDevice": "ceos1",
          "neighborPort": "Management0",
          "ttl": 120
        }
      ]
    }
  ]
}
Closing connection to clab-lab3-ceos3...


