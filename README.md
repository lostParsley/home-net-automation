# Home / Small Office Network with Automation

This repo sets up a small network (router + clients) and automates common tasks (DHCP, DNS, firewall) using **Ansible** and **Python (Netmiko, SNMP)**.
It also includes a starter **Prometheus + Grafana** monitoring setup.

> Educational purpose. Adjust to your devices (Cisco IOS / VyOS / pfSense / Linux router).

## Topology (example)
```
                +------------------+
Internet <----> | Router/Firewall  |
                +--------+---------+
                         |
                 +-------+-------+
                 |   Switch/VM   |
         +-------+-----+     +---+------+
         | Client 1    |     | Client 2 |
         +-------------+     +----------+
```

## Quick Start

### 1) Python environment
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Ansible inventory
Edit `ansible/hosts.ini` with your router details (Cisco IOS shown).

### 3) Run Ansible
```bash
ansible-playbook -i ansible/hosts.ini ansible/router-setup.yml
ansible-playbook -i ansible/hosts.ini ansible/dhcp-dns.yml
ansible-playbook -i ansible/hosts.ini ansible/firewall.yml
```

### 4) Python automation (Netmiko)
```bash
python python/configure_router.py
```

### 5) Basic SNMP check
```bash
python python/monitor_snmp.py
```

### 6) Monitoring (optional)
- Start Prometheus using `monitoring/prometheus.yml` (install Prometheus separately).
- Import `monitoring/grafana-dashboard.json` into Grafana.

## Folders
- `ansible/` — Playbooks for router baseline, DHCP/DNS, firewall
- `python/` — Netmiko config script & SNMP monitor
- `monitoring/` — Prometheus config & Grafana dashboard skeleton




