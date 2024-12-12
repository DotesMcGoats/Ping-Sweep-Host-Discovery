import os
import time


'''def ping(hosts):
    param = '-n' if os.sys.platform.lower() == 'win32' else '-c'
    successful_hosts = []
    
    for host in hosts:
        response = os.system(f"ping {param} 1 {host}")
        
        if response == 0:
            successful_hosts.append(host)
        else:
            continue
    
    return successful_hosts'''


'''def ping(ip):
    # Simulate pinging an IP address
    time.sleep(0.1)  # Simulate some processing time
    return f"Ping result for {ip}"

def scan_ips(ip_list):
    total_ips = len(ip_list)

    for i, ip in enumerate(ip_list, start=1):
        result = ping(ip)
        print(f"\r{i}/{total_ips} IPs scanned", end="")
    
    # Print a newline at the end to move to the next line
    print()'''


def ping(ip):
    param = '-n' if os.sys.platform.lower() == 'win32' else '-c'
    successful_hosts = []
    total_ips = len(ip)
    start_time = time.time()  # Start time of the scan

    for i, ip in enumerate(ip, start=1):
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f"\r{elapsed_time:.2f}:{i}/{total_ips} IPs scanned", end="")
        response = os.system(f"ping {param} 1 {ip}")

        if response == 0:
            successful_hosts.append(ip)
        else:
            continue
    
    return successful_hosts
