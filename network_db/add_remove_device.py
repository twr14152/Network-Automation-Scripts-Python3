import sqlite3
from datetime import datetime
from netmiko import ConnectHandler
from pprint import pprint as pp

hosts = input("Enter host device: ")

ios_rtr = {
        "device_type": "cisco_nxos",
        "ip": hosts,
        "username": "admin",
        "password": "Admin_1234!",
}


conn = sqlite3.connect("netdb.sql")
cursor = conn.cursor()


net_connect = ConnectHandler(**ios_rtr)
hostname = net_connect.send_command("show hostname")
config = net_connect.send_command('show running-config')
mgmt_ip = net_connect.send_command('show interface mgmt 0  | inc "Internet Address"')
os_version = net_connect.send_command('show version | inc "NXOS: version"')
print("hostname:")
print(hostname)
print("**************")
print("os version:")
print(os_version)
print("**************")
print("Config: ")
print(config)

device = {
    "hostname": hostname, 
    "os_version": os_version,
    "mgmt_ip": mgmt_ip,
    "config": config,
}

def add_device(conn, **device):
    try:
        cursor.execute("""
        INSERT INTO devices (hostname, os_version, mgmt_ip, config) 
        VALUES (:hostname, :os_version, :mgmt_ip, :config)
        """, device)
        conn.commit()
        print(f"Device '{device['hostname']}' inserted successfully.")
    except Exception as e:
        print(f"Error adding device: {e}")

def update_device(conn, **device):
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

def validate_device(conn, hostname):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices WHERE hostname = ?", (hostname,))
    row = cursor.fetchone()
    pp(row)


def delete_device(conn, hostname):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM devices WHERE hostname = ?", (hostname,))
    conn.commit()
    if cursor.rowcount:
        print(f"Deleted device: '{hostname}'")
    else:
        print(f"No device '{hostname}' found")

add_device(conn, **device)
update_device(conn, **device)
validate_device(conn, device["hostname"])
delete_device(conn, device["hostname"])
conn.close()


