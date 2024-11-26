# Generate an octet for an IP address based on the starting IP and the CIDR that is passed.
def ipGen(start, cidr):
    ip = []
    start = int(start[0])
    for i in range(start, cidr):
        ip.append(f"{i}")
    return ip