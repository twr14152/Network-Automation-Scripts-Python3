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
```
The other script is just a more streamlined version of the script that uses the actual jsonrpclib to run commands on the device using eAPI.
Just thought it was interesting.

```
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/controller$ python3 lab_script_2.py 
Enter commands: enable, show running-config  
[
  {},
  {
    "header": [
      "! device: ceos1 (cEOSLab, EOS-4.34.2F-43232954.4342F.1 (engineering build))"
    ],
    "comments": [],
    "cmds": {
      "no aaa root": null,
      "username admin privilege 15 role network-admin secret sha512 $6$dfnPlRK7dM5.gtV3$2buw6CucLcHz.LDPiJdP1H9cof6BShC6Om3nE02nE7VL/EWcwj3iXT7gM/TJLzFZWXviX5svPiUkzaTspnHcj.": null,
      "management api http-commands": {
        "comments": [],
        "cmds": {
          "protocol https ssl profile self-signed-certs": null,
          "no shutdown": null
        }
      },
      "no service interface inactive port-id allocation disabled": null,
      "transceiver qsfp default-mode 4x10G": null,
      "service routing protocols model multi-agent": null,
      "hostname ceos1": null,
      "spanning-tree mode mstp": null,
      "system l1": {
        "comments": [],
        "cmds": {
          "unsupported speed action error": null,
          "unsupported error-correction action error": null
        }
      },
      "management api gnmi": {
        "comments": [],
        "cmds": {
          "transport grpc default": {
            "comments": [],
            "cmds": {}
          }
        }
      },
      "management api netconf": {
        "comments": [],
        "cmds": {
          "transport ssh default": {
            "comments": [],
            "cmds": {}
          }
        }
      },
      "management api restconf": {
        "comments": [],
        "cmds": {
          "transport https default": {
            "comments": [],
            "cmds": {
              "ssl profile self-signed-certs": null
            }
          }
        }
      },
      "management security": {
        "comments": [],
        "cmds": {
          "ssl profile self-signed-certs": {
            "comments": [],
            "cmds": {
              "certificate self-signed.crt key self-signed.key": null
            }
          }
        }
      },
      "interface Ethernet1": {
        "comments": [],
        "cmds": {
          "description configured by controller": null,
          "no switchport": null,
          "ip address 10.0.0.1/24": null
        }
      },
      "interface Ethernet2": {
        "comments": [],
        "cmds": {
          "description to ceos3": null,
          "no switchport": null,
          "ip address 10.0.1.1/24": null
        }
      },
      "interface Ethernet3": {
        "comments": [],
        "cmds": {}
      },
      "interface Loopback0": {
        "comments": [],
        "cmds": {
          "description testing restconf": null,
          "ip address 1.1.1.1/32": null
        }
      },
      "interface Management0": {
        "comments": [],
        "cmds": {
          "ip address 172.20.20.5/24": null,
          "ipv6 address 3fff:172:20:20::5/64": null
        }
      },
      "ip access-list MGMT-ACL": {
        "comments": [],
        "cmds": {
          "10 permit icmp any any": null,
          "20 permit ip any any tracked": null,
          "30 permit udp any any eq bfd ttl eq 255": null,
          "40 permit udp any any eq bfd-echo ttl eq 254": null,
          "50 permit udp any any eq multihop-bfd micro-bfd sbfd": null,
          "60 permit udp any eq sbfd any eq sbfd-initiator": null,
          "70 permit ospf any any": null,
          "80 permit tcp any any eq ssh telnet www snmp bgp https msdp ldp netconf-ssh gnmi": null,
          "90 permit udp any any eq bootps bootpc ntp snmp ptp-event ptp-general rip ldp": null,
          "100 permit tcp any any eq mlag ttl eq 255": null,
          "110 permit udp any any eq mlag ttl eq 255": null,
          "120 permit vrrp any any": null,
          "130 permit ahp any any": null,
          "140 permit pim any any": null,
          "150 permit igmp any any": null,
          "160 permit tcp any any range 5900 5910": null,
          "170 permit tcp any any range 50000 50100": null,
          "180 permit udp any any range 51000 51100": null,
          "190 permit tcp any any eq 3333": null,
          "200 permit tcp any any eq nat ttl eq 255": null,
          "210 permit tcp any eq bgp any": null,
          "220 permit rsvp any any": null,
          "230 permit tcp any any eq 9340": null,
          "240 permit tcp any any eq 9559": null,
          "250 permit udp any any eq 8503": null,
          "260 permit udp any any eq lsp-ping": null,
          "270 permit udp any eq lsp-ping any range 51900 51999": null,
          "280 permit tcp any any eq 6020": null
        }
      },
      "ip routing": null,
      "system control-plane": {
        "comments": [],
        "cmds": {
          "ip access-group MGMT-ACL in": null
        }
      },
      "ip route 0.0.0.0/0 172.20.20.1": null,
      "ipv6 route ::/0 3fff:172:20:20::1": null,
      "router bgp 1": {
        "comments": [],
        "cmds": {
          "distance bgp 20 200 200": null,
          "neighbor 10.0.0.2 remote-as 2": null,
          "neighbor 10.0.0.2 description ceos2": null,
          "neighbor 10.0.0.2 timers 1 4": null,
          "network 1.1.1.1/32": null,
          "redistribute connected": null
        }
      },
      "router multicast": {
        "comments": [],
        "cmds": {
          "ipv4": {
            "comments": [],
            "cmds": {
              "software-forwarding kernel": null
            }
          },
          "ipv6": {
            "comments": [],
            "cmds": {
              "software-forwarding kernel": null
            }
          }
        }
      },
      "router ospf 1": {
        "comments": [],
        "cmds": {
          "network 0.0.0.0/0 area 0.0.0.0": null,
          "network 10.0.0.0/8 area 0.0.0.0": null,
          "max-lsa 12000": null
        }
      }
    }
  }
]
(lab_env) todd@todd-TOSHIBA-DX735:~/Code_folder/containerlab/containerlabs_sandbox/ceos_lab/lab3/scripts/controller$ 
```


