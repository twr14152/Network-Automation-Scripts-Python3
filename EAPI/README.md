Sample output
```
$ python lab_script.py 
Enter device to connect to: clab-lab3-ceos1, clab-lab3-ceos2, clab-lab3-ceos3
Enter commands to run seperated by ",": enable, show lldp neighbors
Connected to clab-lab3-ceos1..
{'id': '1',
 'jsonrpc': '2.0',
 'result': [{},
            {'lldpNeighbors': [{'neighborDevice': 'ceos2',
                                'neighborPort': 'Ethernet1',
                                'port': 'Ethernet1',
                                'ttl': 120},
                               {'neighborDevice': 'ceos3',
                                'neighborPort': 'Ethernet1',
                                'port': 'Ethernet2',
                                'ttl': 120},
                               {'neighborDevice': 'ceos2',
                                'neighborPort': 'Management0',
                                'port': 'Management0',
                                'ttl': 120},
                               {'neighborDevice': 'ceos3',
                                'neighborPort': 'Management0',
                                'port': 'Management0',
                                'ttl': 120}],
             'tablesAgeOuts': 0,
             'tablesDeletes': 1,
             'tablesDrops': 0,
             'tablesInserts': 5,
             'tablesLastChangeTime': 1760877848.7299967}]}
Closing connection to clab-lab3-ceos1...


Connected to clab-lab3-ceos2..
{'id': '1',
 'jsonrpc': '2.0',
 'result': [{},
            {'lldpNeighbors': [{'neighborDevice': 'ceos1',
                                'neighborPort': 'Ethernet1',
                                'port': 'Ethernet1',
                                'ttl': 120},
                               {'neighborDevice': 'ceos3',
                                'neighborPort': 'Ethernet2',
                                'port': 'Ethernet2',
                                'ttl': 120},
                               {'neighborDevice': 'ceos1',
                                'neighborPort': 'Management0',
                                'port': 'Management0',
                                'ttl': 120},
                               {'neighborDevice': 'ceos3',
                                'neighborPort': 'Management0',
                                'port': 'Management0',
                                'ttl': 120}],
             'tablesAgeOuts': 0,
             'tablesDeletes': 1,
             'tablesDrops': 0,
             'tablesInserts': 5,
             'tablesLastChangeTime': 1760877838.4724615}]}
Closing connection to clab-lab3-ceos2...


Connected to clab-lab3-ceos3..
{'id': '1',
 'jsonrpc': '2.0',
 'result': [{},
            {'lldpNeighbors': [{'neighborDevice': 'ceos1',
                                'neighborPort': 'Ethernet2',
                                'port': 'Ethernet1',
                                'ttl': 120},
                               {'neighborDevice': 'ceos2',
                                'neighborPort': 'Ethernet2',
                                'port': 'Ethernet2',
                                'ttl': 120},
                               {'neighborDevice': 'ceos2',
                                'neighborPort': 'Management0',
                                'port': 'Management0',
                                'ttl': 120},
                               {'neighborDevice': 'ceos1',
                                'neighborPort': 'Management0',
                                'port': 'Management0',
                                'ttl': 120}],
             'tablesAgeOuts': 0,
             'tablesDeletes': 0,
             'tablesDrops': 0,
             'tablesInserts': 4,
             'tablesLastChangeTime': 1760727895.2706263}]}
Closing connection to clab-lab3-ceos3...

```
