from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.1",
    "username": "admin",
    "password": "password",
}

commands = [
    "hostname HomeRouter",
    "ip dhcp pool HOME",
    "network 192.168.1.0 255.255.255.0",
    "default-router 192.168.1.1",
    "ip name-server 8.8.8.8",
]

def main():
    print("[+] Connecting to router...")
    conn = ConnectHandler(**device)
    print("[+] Pushing configuration...")
    output = conn.send_config_set(commands)
    print(output)
    conn.save_config()
    conn.disconnect()
    print("[+] Done.")

if __name__ == "__main__":
    main()
