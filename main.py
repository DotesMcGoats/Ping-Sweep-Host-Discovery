import subnet
import ping
from decorators import logger


@logger
def main():
    start = input("Enter the starting IP in CIDR notation: ")
    ip = subnet.cidr(start)
    ip = ping.ping(ip)
    print(f'\n\n{ip}')


if __name__ == '__main__':
    main()
