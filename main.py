import ipGenerator
import subnet
import ping
import subprocess


def main():
    start = int(input("Enter the starting IP: "))
    cidr = int(input("Enter the CIDR: "))
    ip = subnet.get_subnet(start, cidr)
    ping.ping(ip)


if __name__ == '__main__':
    main()