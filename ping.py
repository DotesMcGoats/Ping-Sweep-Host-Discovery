import os
from decorators import timer, logger


def update_progress(formatted_time, i, total_ips):
    print(f"\r{formatted_time}; {i}/{total_ips} IPs scanned", end="")

@logger
@timer(lambda formatted_time, i, total_ips: update_progress(formatted_time, i, total_ips))
def ping(state, ip):
    param = '-n' if os.sys.platform.lower() == 'win32' else '-c'
    null_device = 'NUL' if os.sys.platform.lower() == 'win32' else '/dev/null'
    successful_hosts = []
    state['total_ips'] = len(ip)

    for i, ip in enumerate(ip, start=1):
        response = os.system(f"ping {param} 1 {ip} > {null_device} 2>&1")

        if response == 0:
            successful_hosts.append(ip)
        
        # Update the progress after each ping
        state['i'] = i
        update_progress(state['formatted_time'], i, state['total_ips'])  # Update progress with current values
    
    return successful_hosts