import subnet
import ping


def main():
    start = input("Enter the starting IP in CIDR notation: ")
    ip = subnet.cidr(start)
    ip = ping.ping(ip)
    print(ip)


if __name__ == '__main__':
    main()
