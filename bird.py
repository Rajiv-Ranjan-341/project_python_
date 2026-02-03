import ipaddress

def allocate_subnets(base_network, departments):
    network = ipaddress.ip_network(base_network, strict=False)
    current_address = network.network_address
    allocated_subnets = []
    sorted_departments = sorted(departments, key=lambda x: x[1], reverse=True)
    
    for dept_name, host_count in sorted_departments:
      
        required_ips = host_count + 2  
        subnet_prefix = 32 - (required_ips - 1).bit_length()
        subnet = ipaddress.ip_network(f"{current_address}/{subnet_prefix}", strict=False)
        allocated_subnets.append({
            "Department": dept_name,
            "Network Address": str(subnet.network_address),
            "Subnet Mask": str(subnet.netmask),
            "Broadcast Address": str(subnet.broadcast_address),
            "Usable IP Range": f"{subnet.network_address + 1} - {subnet.broadcast_address - 1}"
        })
        current_address = subnet.broadcast_address + 1
    
    return allocated_subnets
university_network = "172.16.0.0/16"
departments = [
    ("Engineering", 2000),
    ("Medical", 1500),
    ("Management", 1000),
    ("Library", 500),
    ("Admin", 300)
]
subnet_details = allocate_subnets(university_network, departments)

for subnet in subnet_details:
    print(f"Department: {subnet['Department']}")
    print(f"  Network Address: {subnet['Network Address']}")
    print(f"  Subnet Mask: {subnet['Subnet Mask']}")
    print(f"  Broadcast Address: {subnet['Broadcast Address']}")
    print(f"  Usable IP Range: {subnet['Usable IP Range']}")
    print("-")
