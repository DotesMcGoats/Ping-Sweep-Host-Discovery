import os


def ping(hosts):
    param = '-n' if os.sys.platform.lower() == 'win32' else '-c'
    successful_hosts = []
    
    for host in hosts:
        print(f"Pinging {host}")
        response = os.system(f"ping {param} 1 {host}")
        
        if response == 0:
            print(f"{host} is up!")
            successful_hosts.append(host)
        else:
            print(f"{host} is down!")
    
    return successful_hosts
