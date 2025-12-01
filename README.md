# Network-Automation-Scripts using Python3
# Libraries: pyGNMI, Pyeapi, eAPI, Netmiko, Napalm, Telnetlib, Restconf, Nxapi, Nornir, Netconf, Requests
This repository holds various scripts I've written over the years. 
The goal is to create a repository that could be used for knowledge retention and reference.

I will be archiving or deleting scripts that no longer provide value.
### json/rpc - SRLinux
- 11/30/2025 - Set up little lab usng Srlinux in containerlab. Used json/rpc to build the ospf connection between a couple of switches.
- config script - srlinux/json_rpc/enable_ospf.py
- gather ospf info script - srlinux/json_rpc/get_info.py
- update interface description - srlinux/json_rpc/update_intf_description.py


### pyGNMI
- 10/29/2025 - Arista ceos by default use port TCP/6030 which was pre-standard so updated that to TCP/57400. You do need to update MGMT-ACL to permit it to get it to work
- 10/24/2025 - Playing around with pyGNMI (get/set) functionality
- Interface configuration possible with arista openconfig yang models using pyGNMI
- Had no luck configurating any ospf on the devices using pyGNMI. Believe it to be an issue with aristas openconfig/yang compatability/integration
- pyGNMI/get_intf_info_gnmi.py - pulls interface - (config/state/counters/capabilities)
- pyGNMI/set_config_gnmi.py - set interface description

### eAPI
- 10/19/2025 - Using eAPI to get data and configure devices
- Script using requests - eAPI/lab_script.py
- Script using jsonrpclib -  eAPI/lab_script_2.py 
    
### Network_DB
- 08/03/2025 - DYI network database
- Used sqlite for the DB. ((This is not for production just a learning exercise))
- Used netmiko to pull data from a Devnet nxos device.
    - network_db/add_remove_device.py
    - network_db/schema
  
### DNAC
- Grabbing data out of DNAC
    - get_device_dnac.py
    - get_client_health_info.py

### Meraki
- Using requests to GET data from the meraki dashboard api (Orgs and Networks)
- Using requests POST to create a network through the meraki dashboard api
- Using requests PUT to update a SSID on a wireless device through the meraki dashboard api 

### Network Controller
- Playing around with Packet Tracer and testing out its network controller
- Grab network device info - network_controller/get_device_info.py
- Grab more generic info from network devices - network_controller/get_all_devices_info.py
- Update network devices (site wide) - network_controller/update_device_config.py

### Nornir - TestDrive 
- Cisco IOS - GNS3 lab - nornir/using_netmiko_plugin
- Arista Ceos lab - nornir/using_napalm_plugin 
- Testing newer version of Nornir, not backwards compatible with version 1.x

### Netconf
- Getting used to xmlns is a challenge and can be frustrating. Took me a while to find the proper xmlns to config a loopback
- Wrote a script to find out where that xmlns is in the server capabilities dump
    - netconf_svr_capability.py
    - netconf_svr_capability_ouput.txt
- Documentation around netconf is not intuitive from my point of view
- This will be a trial and error process. 
- Script to config loopback interface
    - netconf_config_device.py - configured a loopback on devnet router
    - netconf_config_device_output.text - results
- Script to do config backups. 
    - netconf_iosxe_cfg_bkup.py - rewrite of netconf_config_bkup.py
    - netconf_config_bkup.py - goes out pulls running config and places it in config_bkup/ directory
    - netconf_config_output.txt - the results of the script
- First time using netconf
  - netconf_ex1.py
  - netconf_get_conf.py

### Nxapi 
- Minor update to the  to make output from commands more readable 
  - added : print(json.dumps(response, indent=2, sort_keys=True))
  - added nxapi_script02.py and nxapi_script02_output.txt for comparison to original script
- Found this api documentation to be lacking
- Script examples I found were rigid and not very flexible
- Created a script to allow user to enter any commands (config/show) w/o having to rewrite the script.
  - nxapi_script_ex1.py

### Restconf 
- 11/03/2025 - Playing around with ceos in containerlab restconf enbaled.  Curl to device using hostname is very fast. Python using requests to hostname unbearably slow. Something with my set up?? Not sure.. IPv4 vs IPv6 setting in containerlab hostname resolution?? If I use the IPv4 address of the host instead, response time significantly improves.
    - req_intf_state_cfg.py - get interface config or state
    - req_intf_name_state_errors.py - get specific interface stats and print it out 
- 08/03/2025 - This repo is lacking in almost every way. I will try and update as time permits. 
     - restconf/08.03.2025_restconf_ex.py
- Created two scripts one to create an interface and the other to delete it
    - create_intf.py
    - delete_intf.py
    - script_output.txt
    
### Pyeapi - Python client for Arista eAPI 
 - Created some scripts for use with ceoslab
 - pyeapi_w_out_conf.py - using pyeapi without config file
 - Cleaning up directory archived some scripts and created interactive script folder
 - Posted configs and validation scripts for ceos demo
 - Posted configs and validation from demo
 - hidden host config file, needs to be located in ~/.eapi.conf
 - created two sample scripts

### Netmiko testing
- 06/25/2025 - Playing around with clabs and FRR simple script to make config changes on frr devices:
    -  netmiko/FRR/load_config_file
    -  The files used to load the configs could also be used to run multiple show commands
    -  The netmiko script is simply looping through the series of command line instructions in the files the script loads
    -  Netmiko does not have a FRR NOS option so you have to use linux
- 06/19/2025 - contribution from Uniuqe: ospf_configurator
    -  netmiko/ospf_configurator 
- Playing around with FRR in containerlabs sample code FRR/lab_script.py
- Got a request today to help someone write a script. Created folder and will keep the scripts in there. 
    - script_requests/req_config_script_07292020.py 
- Haven't messed around with Netmiko in quite a while decided to play around and try and update an old script to have both (show/conf) functionality.
- It's painfully slow as I haven't added any features such as MP to it to speed it up, but it was working with the devnet CSRs.
- Basically the script will ask the user if this is going to be a configuration or show commands script. Depending on the answer the script will do one or the other.  
  - test_stuff/interactive_script.py 
  - test_stuff/interactive_script_output.txt
- NetworkDiscovery/host_file_and_script/ has the most pragmatic scripts for doing network discovery (ie..scripts that run show commands and captures the results and saves them to files)
- Netmiko scripts for running show commands can be found in the NetworkDiscovery folder 
  - show_commands.py - easiest for every day troubleshooting and operations and lab work
- Python3.7 works with the scripts as written. Python3.8 is not yet ready. 
- Reorganized some config scripts into config_scripts folder
  - Scripts are self explanatory
- Created a script to go out and automatically determine the device_type for a host_list or seedfile.
  - NetworkDiscovery/host_file_and_script/auto_detect_script.py
- sample script to connect to juniper device
  - juniper_script1.py
  - juniper_conf_from_file.py
- scp 
  - file transfers to veos devices hosted using vagrant
  - file transfers to multiple devices using containerized eos or ceos 
- Network-Automation-Scripts_Python3/netmiko/NetworkDiscovery/host_file_and_script/
  - ios_discovery_enable_mode.py - if enable pw is required
  - ios_discovery_script.py - if username/password priv level 15
  - host_file.txt
- Added 3 examples of how to use jinja templates with netmiko
 - conf_bgp_r4_r5_using_class_obj. - uses class object to populate template
 - conf_bgp_r4_r5_using_dict.py - uses dictionaries to populate template
 - conf_bgp_yaml_jinja2.py - uses yaml files to populate a jinja2 template
- Created new script that provide you a sandbox to say how many devices, what devices, and what to configure on each
    - ssh_sandbox.py
- Created a very basic ssh script useful for discovery + updated with error handling
- Created script that can handle multiple device with multiple unique configuration files
- Added multiprocessing to speed up
    - netmiko_multi_dev_cfg.py
- Added multiprocessing Pools to scripts to speed them up
    - netmiko_script5.py
    - netmiko_show_cmds.py
    - netmiko speed comparison between serial and multi-processing pools
- netmiko_script#.py
- capture output of scripts

### Napalm for eos
- /config_scripts/conf_merge 
- /config_scripts
- Tested with ipython(python3.6) - EOS_lab_Napalm_test_results
- napalm_eos_script1.py

### Napalm for cisco ios
- napalm discovery script and post script
    - discovery_ios_svc_now.py
    - post_svc_now_rest_api.py
- created a config_scripts directory added new script
    - script_config_ios.py
- added new get_facts and get config script to directory
- Testing with python3 napalm_base and napalm_ios
- In my gns3 environment I'm using the following code
    - C7200-ADVENTERPRISEK9-M, Version 15.2(4)S7
    - IOS provides access to a subset of napalms features
    - EOS has been a more feature rich testbed with napalm

### Telnetlib module
- Added script that works with devices that require enable password
- Use python3 telnetlib module
- capture output of scripts

### Misc stuff
- script to find duplicate ips
  - findingDupIPs.py
- simple way to iterate through cli commands when running a script
  - loop_thru_cli_cmds.py
  - loop_thru_cli_cmds_output.txt



