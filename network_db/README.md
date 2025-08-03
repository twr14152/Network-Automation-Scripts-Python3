# D.I.Y Network Database

Always wanted to set up my own database to hold network device data. So I thought I would give it a shot. It wasn't too difficult. I know that sqlite is probably not the best choice but for educational purposes its fine.

So first you need to define what data you want to hold in your DB. So here's the schema I came up with.
```
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ cat schema 
CREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT NOT NULL UNIQUE,
    os_version TEXT,
    mgmt_ip TEXT NOT NULL UNIQUE,
    config TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
The next step was to build the database and add the schema.
```
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ touch netwk.db
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ sqlite3
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .open netwk.db
sqlite> CREATE TABLE devices (
   ...>     id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>     hostname TEXT NOT NULL UNIQUE,
   ...>     os_version TEXT,
   ...>     mgmt_ip TEXT NOT NULL UNIQUE,
   ...>     config TEXT,
   ...>     last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
   ...> );
sqlite> .quit
);
```
I used netmiko to connect to one of the nxos devices in devnet to get some data. This data is not formated in json. It's simply pulled off the device. For the test its fine, it can always be refined. I used sqlite3 to add CRUD functionality. This script tests create, update, validates, and deletes the the data in the DB. in this example I commented out the update and delete function as this is first time we are adding data to our database. Only add and validations functions are being called. Used pprint to make the validation portion more readable.

```
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ python3.12 add_remove_device.py 
Enter host device: sandbox-nxos-1.cisco.com
Gathering device data......
Getting hostname:
-----------------
Getting os version:
-----------------
Getting mgmt_ip:
-----------------
Getting config: 
Gathering data complete....
Adding data to the database...
Device 'nxos 
' inserted successfully.
Reading data in the database...
(7,
 'nxos \n',
 '  NXOS: version 10.3(3) [Feature Release]\n',
 '  Internet Address is 10.10.20.95/24\n',
 '\n'
 '!Command: show running-config\n'
 '!Running configuration last done at: Sat Aug  2 19:44:45 2025\n'
 '!Time: Sat Aug  2 22:05:09 2025\n'
 '\n'
 'version 10.3(3) Bios:version  \n'
 'switchname nxos\n'
 'vdc nxos id 1\n'
 '  limit-resource vlan minimum 16 maximum 4094\n'
 '  limit-resource vrf minimum 2 maximum 4097\n'
 '  limit-resource port-channel minimum 0 maximum 511\n'
 '  limit-resource m4route-mem minimum 58 maximum 58\n'
 '  limit-resource m6route-mem minimum 8 maximum 8\n'
 '\n'
 'feature nxapi\n'
 'feature bash-shell\n'
 'cfs eth distribute\n'
 'feature ospf\n'
 'feature netconf\n'
 'feature hsrp\n'
 'feature vpc\n'
 '\n'
 'username admin password 5 '
 '$5$NOJJKL$mFlw8E8BC4h.LLDDTkBUuHQNtk3MFslr7hqy7j3Rwq5  role network-admin\n'
 'ssh key rsa 2048 \n'
 'ip domain-lookup\n'
 'copp profile strict\n'
 'snmp-server user admin network-admin auth md5 '
 '52036704DA8793EDC8726140EB5216EDEA84 priv aes-128 '
 '37462F1D8084C3B9C47C4E72B94807AEF7D2 localizedV2key\n'
 'rmon event 1 log trap public description FATAL(1) owner PMON@FATAL\n'
 'rmon event 2 log trap public description CRITICAL(2) owner PMON@CRITICAL\n'
 'rmon event 3 log trap public description ERROR(3) owner PMON@ERROR\n'
 'rmon event 4 log trap public description WARNING(4) owner PMON@WARNING\n'
 'rmon event 5 log trap public description INFORMATION(5) owner PMON@INFO\n'
 '\n'
 'vlan 1,1041\n'
 '\n'
 'vrf context management\n'
 '  ip route 0.0.0.0/0 10.10.20.254\n'
 '\n'
 'interface Ethernet1/1\n'
 '\n'
 'interface Ethernet1/2\n'
 '  no switchport\n'
 '  ip address 10.10.10.1/24\n'
 '  no shutdown\n'
 '\n'
 'interface Ethernet1/3\n'
 '\n'
 'interface Ethernet1/4\n'
 '\n'
 'interface Ethernet1/5\n'
 '\n'
 'interface Ethernet1/6\n'
 '\n'
 'interface Ethernet1/7\n'
 '\n'
 'interface Ethernet1/8\n'
 '\n'
 'interface Ethernet1/9\n'
 '\n'
 'interface Ethernet1/10\n'
 '\n'
 'interface Ethernet1/11\n'
 '\n'
 'interface Ethernet1/12\n'
 '\n'
 'interface Ethernet1/13\n'
 '\n'
 'interface Ethernet1/14\n'
 '\n'
 'interface Ethernet1/15\n'
 '\n'
 'interface Ethernet1/16\n'
 '\n'
 'interface Ethernet1/17\n'
 '\n'
 'interface Ethernet1/18\n'
 '\n'
 'interface Ethernet1/19\n'
 '\n'
 'interface Ethernet1/20\n'
 '\n'
 'interface Ethernet1/21\n'
 '\n'
 'interface Ethernet1/22\n'
 '\n'
 'interface Ethernet1/23\n'
 '\n'
 'interface Ethernet1/24\n'
 '\n'
 'interface Ethernet1/25\n'
 '\n'
 'interface Ethernet1/26\n'
 '\n'
 'interface Ethernet1/27\n'
 '\n'
 'interface Ethernet1/28\n'
 '\n'
 'interface Ethernet1/29\n'
 '\n'
 'interface Ethernet1/30\n'
 '\n'
 'interface Ethernet1/31\n'
 '\n'
 'interface Ethernet1/32\n'
 '\n'
 'interface Ethernet1/33\n'
 '\n'
 'interface Ethernet1/34\n'
 '\n'
 'interface Ethernet1/35\n'
 '\n'
 'interface Ethernet1/36\n'
 '\n'
 'interface Ethernet1/37\n'
 '\n'
 'interface Ethernet1/38\n'
 '\n'
 'interface Ethernet1/39\n'
 '\n'
 'interface Ethernet1/40\n'
 '\n'
 'interface Ethernet1/41\n'
 '\n'
 'interface Ethernet1/42\n'
 '\n'
 'interface Ethernet1/43\n'
 '\n'
 'interface Ethernet1/44\n'
 '\n'
 'interface Ethernet1/45\n'
 '\n'
 'interface Ethernet1/46\n'
 '\n'
 'interface Ethernet1/47\n'
 '\n'
 'interface Ethernet1/48\n'
 '\n'
 'interface Ethernet1/49\n'
 '\n'
 'interface Ethernet1/50\n'
 '\n'
 'interface Ethernet1/51\n'
 '\n'
 'interface Ethernet1/52\n'
 '\n'
 'interface Ethernet1/53\n'
 '\n'
 'interface Ethernet1/54\n'
 '\n'
 'interface Ethernet1/55\n'
 '\n'
 'interface Ethernet1/56\n'
 '\n'
 'interface Ethernet1/57\n'
 '\n'
 'interface Ethernet1/58\n'
 '\n'
 'interface Ethernet1/59\n'
 '\n'
 'interface Ethernet1/60\n'
 '\n'
 'interface Ethernet1/61\n'
 '\n'
 'interface Ethernet1/62\n'
 '\n'
 'interface Ethernet1/63\n'
 '\n'
 'interface Ethernet1/64\n'
 '\n'
 'interface mgmt0\n'
 '  vrf member management\n'
 '  ip address 10.10.20.95/24\n'
 '\n'
 'interface loopback0\n'
 '\n'
 'interface loopback10\n'
 '  ip address 1.1.1.1/32\n'
 '\n'
 'interface loopback20\n'
 '  ip address 2.2.2.2/32\n'
 '\n'
 'interface loopback40\n'
 '  ip address 4.4.4.4/32\n'
 '\n'
 'interface loopback50\n'
 '  ip address 5.5.5.5/32\n'
 'icam monitor scale\n'
 '\n'
 'line console\n'
 '  exec-timeout 0\n'
 '  terminal width  511\n'
 'line vty\n'
 'boot nxos bootflash:/nxos64-cs.10.3.3.F.bin \n'
 'router ospf TEST\n'
 '  router-id 1.1.1.1\n'
 '\n'
 'no logging console\n'
 '\n'
 '\n',
 '2025-08-03 15:25:12')

```
You can use sqlite browser to see the data in the database in its proper format. But for our purposes this is what it looks like when you cat the db. Not pretty but you can see the data is there.
```
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ cat netwk.db 
?I???IP++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)?|OtabledevicesdevicesCREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT NOT NULL UNIQUE,
    os_version TEXT,
    mgmt_ip TEXT NOT NULL UNIQUE,
    config TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
???aW?]3nxos _autoindex_devices_2devices-Andexsqlite_autoindex_devices_1devices
  NXOS: version 10.3(3) [Feature Release]
  Internet Address is 10.10.20.95/24

!Command: show running-config
!Running configuration last done at: Sat Aug  2 19:44:45 2025
!Time: Sat Aug  2 22:05:09 2025

version 10.3(3) Bios:version  
switchname nxos
vdc nxos id 1
  limit-resource vlan minimum 16 maximum 4094
  limit-resource vrf minimum 2 maximum 4097
  limit-resource port-channel minimum 0 maximum 511
  limit-resource m4route-mem minimum 58 maximum 58
  limit-resource m6route-mem minimum 8 maximum 8

feature nxapi
feature bash-shell
cfs eth distribute
feature ospf
feature netconf
feature hsrp
feature vpc

username admin password 5 $5$NOJJKL$mFlw8E8BC4h.LLDDTkBUuHQNtk3MFslr7hqy7j3Rwq5  role network-admin
ssh key rsa 2048 
ip domain-lookup
copp profile strict
snmp-server user admin network-admin auth md5 52036704DA8793EDC8726140EB5216EDEA84 priv aes-128 37462F1D8084C3B9C47C4E72B94807AEF7D2 localizedV2key
rmon event 1 log trap public description FATAL(1) owner PMON@FATAL
rmon event 2 log trap public description CRITICAL(2) owner PMON@CRITICAL
rmon event 3 log trap public description ERROR(3) owner PMON@ERROR
rmon event 4 log trap public description WARNING(4) owner PMON@WARNING
rmon event 5 log trap public description INFORMATION(5) owner PMON@INFO

vlan 1,1041

vrf context management
  ip route 0.0.0.0/0 10.10.20.254

interface Ethernet1/1

interface Ethernet1/2
  no switchport
  ip address 10.10.10.1/24
  no shutdown

interface Ethernet1/3

interface Ethernet1/4

interface Ethernet1/5

interface Ethernet1/6

interface Ethernet1/7

interface Ethernet1/8

interface Ethernet1/9

interface Ethernet1/10

interface Ethernet1/11

interface Ethernet1/12

interface Ethernet1/13

interface Ethernet1/14

interface Ethernet1/15

interface Ethernet1/16

interface Ethernet1/17

interface Ethernet1/18

interface Ethernet1/19

interface Ethernet1/20

interface Ethernet1/21

interface Ethernet1/22

interface Ethernet1/23

interface Ethernet1/24

interface Ethernet1/25

interface Ethernet1/26

interface Ethernet1/27

interface Ethernet1/28

interface Ethernet1/29

interface Ethernet1/30

interface Ethernet1/31

interface Ethernet1/32

interface Ethernet1/33

interface Ethernet1/34

interface Ethernet1/35

interface Ethernet1/36

interface Ethernet1/37

interface Ethernet1/38

interface Ethernet1/39

interface Ethernet1/40

interface Ethernet1/41

interface Ethernet1/42

interface Ethernet1/43

interface Ethernet1/44

interface Ethernet1/45

interface Ethernet1/46

interface Ethernet1/47

interface Ethernet1/48

interface Ethernet1/49

interface Ethernet1/50

interface Ethernet1/51

interface Ethernet1/52

interface Ethernet1/53

interface Ethernet1/54

interface Ethernet1/55

interface Ethernet1/56

interface Ethernet1/57

interface Ethernet1/58

interface Ethernet1/59

interface Ethernet1/60

interface Ethernet1/61

interface Ethernet1/62

interface Ethernet1/63

interface Ethernet1/64

interface mgmt0
  vrf member management
  ip address 10.10.20.95/24

interface loopback0

interface loopback10
  ip address 1.1.1.1/32

interface loopback20
  ip address 2.2.2.2/32

interface loopback40
  ip address 4.4.4.4/32

interface loopback50
  ip address 5.5.5.5/32
icam monitor scale

line console
  exec-timeout 0
  terminal width  511
line vty
boot nxos bootflash:/nxos64-cs.10.3.3.F.bin 
router ospf TEST
  router-id 1.1.1.1

no logging console


2025-08-03 15:25:12
??
nxos 

??)W  Internet Address is 10.10.20.95/24
??
  evicespi@rasp4:~/Coding/python_folder/misc/netwk_db $ 

```
Now to delete the device from the database simply comment out the add, and validate functions and uncomment the delete function
```
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ python3.12 add_remove_device.py 
Enter host device: sandbox-nxos-1.cisco.com
Gathering device data......
Getting hostname:
-----------------
Getting os version:
-----------------
Getting mgmt_ip:
-----------------
Getting config: 
Gathering data complete....
Deleting data from the database...
Deleted device: 'nxos 
'
pi@rasp4:~/Coding/python_folder/misc/netwk_db $ cat netwk.db 
?I???IP++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)?|OtabledevicesdevicesCREATE TABLE devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hostname TEXT NOT NULL UNIQUE,
    os_version TEXT,
    mgmt_ip TEXT NOT NULL UNIQUE,
    config TEXT,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP
[-Andexsqlite_autoindex_devices_2devices-Andexsqlite_autoindex_devices_1devices
?

??
  evicespi@rasp4:~/Coding/python_folder/misc/netwk_db $ ```
