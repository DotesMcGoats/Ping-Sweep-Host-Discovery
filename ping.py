import os
import time


def ping(ip):
    param = '-n' if os.sys.platform.lower() == 'win32' else '-c'
    successful_hosts = []
    null_device = 'NUL' if os.sys.platform.lower() == 'win32' else '/dev/null'
    total_ips = len(ip)
    start_time = time.time()  # Start time of the scan
    last_update = start_time

    for i, ip in enumerate(ip, start=1):
        response = os.system(f"ping {param} 1 {ip} > {null_device} 2>&1")

        if response == 0:
            successful_hosts.append(ip)

        # Updates the how much time has passed and how many IPs have been pinged every second
        current_time = time.time()
        if current_time - last_update >= 1:
            elapsed_time = time.time() - start_time  # Calculate elapsed time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) # Format elapsed time
            print(f"\r{formatted_time}; {i}/{total_ips} IPs scanned", end="")
            last_update = current_time
    
    return successful_hosts
