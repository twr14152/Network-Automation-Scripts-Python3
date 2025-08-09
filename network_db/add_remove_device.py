import sqlite3
from datetime import datetime
from netmiko import ConnectHandler
from pprint import pprint as pp

hosts = input("Enter host device: ")
user = input("Username: ")
password = input("Password: ")

ios_rtr = {
        "device_type": "cisco_nxos",
        "ip": hosts,
        "username": user,
        "password": password,
}


conn = sqlite3.connect("netwk.db")
cursor = conn.cursor()

print("Gathering device data......")

net_connect = ConnectHandler(**ios_rtr)
hostname = net_connect.send_command("show hostname")
config = net_connect.send_command('show running-config')
mgmt_ip = net_connect.send_command('show interface mgmt 0  | inc "Internet Address"')
os_version = net_connect.send_command('show version | inc "NXOS: version"')


print("Getting hostname:")
#print(hostname)
print("-----------------")
print("Getting os version:")
#print(os_version)
print("-----------------")
print("Getting mgmt_ip:")
#print(mgmt_ip)
print("-----------------")
print("Getting config: ")
#print(config)
print("Gathering data complete....")


device = {
    "hostname": hostname, 
    "os_version": os_version,
    "mgmt_ip": mgmt_ip,
    "config": config,
}

def add(conn, **device):
    print("Adding data to the database...")
    try:
        cursor.execute("""
        INSERT INTO devices (hostname, os_version, mgmt_ip, config) 
        VALUES (:hostname, :os_version, :mgmt_ip, :config)
        """, device)
        conn.commit()
        print(f"Device '{device['hostname']}' inserted successfully.")
    except Exception as e:
        print(f"Error adding device: {e}")

def update(conn, **device):
    print("Updating data in the database...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE devices SET hostname = :hostname,
        os_version = :os_version,
        mgmt_ip = :mgmt_ip,
        config = :config,
        last_updated = CURRENT_TIMESTAMP 
        WHERE id = :id
        """, device)
        conn.commit()
        print(f"{device['hostname']} updated.")
    except Exception as e:
        print(f"Error update failed: {e}")

def read(conn, hostname):
    print("Reading data in the database...")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices WHERE hostname = ?", (hostname,))
    row = cursor.fetchone()
    pp(row)


def delete(conn, hostname):
    print("Deleting data from the database...")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM devices WHERE hostname = ?", (hostname,))
    conn.commit()
    if cursor.rowcount:
        print(f"Deleted device: '{hostname}'")
    else:
        print(f"No device '{hostname}' found")

add(conn, **device)
update(conn, **device)
read(conn, device["hostname"])
delete(conn, device["hostname"])
conn.close()
