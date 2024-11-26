import ipGenerator

# Used to convert the CIDR notation into a subnet mask.





def main():
    start = int(input("Enter the starting IP: "))
    cidr = int(input("Enter the CIDR: "))
    ip = ipGenerator.ipGen(start, cidr)
    print(ip)


if __name__ == '__main__':
    main()