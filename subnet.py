import ipGenerator


# Used to convert the CIDR notation into a subnet mask.
def cidr(ipAddr):
    ip, cidr = ipAddr.split("/")
    cidr = int(cidr)
    oct1, oct2, oct3, oct4 = ip.split(".")
    oct1 = [oct1]
    oct2 = [oct2]
    oct3 = [oct3]
    oct4 = [oct4]
    match cidr:
        case 0:
            oct1 = ipGenerator.ipGen(0, 256)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 1:
            oct1 = ipGenerator.ipGen(oct1, 128)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 2:
            oct1 = ipGenerator.ipGen(oct1, 64)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 3:
            oct1 = ipGenerator.ipGen(oct1, 32)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 4:
            oct1 = ipGenerator.ipGen(oct1, 16)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 5:
            oct1 = ipGenerator.ipGen(oct1, 8)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 6:
            oct1 = ipGenerator.ipGen(oct1, 4)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 7:
            oct1 = ipGenerator.ipGen(oct1, 2)
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 8:
            oct2 = ipGenerator.ipGen(oct2, 256)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 9:
            oct2 = ipGenerator.ipGen(oct2, 128)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 10:
            oct2 = ipGenerator.ipGen(oct2, 64)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 11:
            oct2 = ipGenerator.ipGen(oct2, 32)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 12:
            oct2 = ipGenerator.ipGen(oct2, 16)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 13:
            oct2 = ipGenerator.ipGen(oct2, 8)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 14:
            oct2 = ipGenerator.ipGen(oct2, 4)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 15:
            oct2 = ipGenerator.ipGen(oct2, 2)
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 16:
            oct3 = ipGenerator.ipGen(oct3, 256)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 17:
            oct3 = ipGenerator.ipGen(oct3, 128)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 18:
            oct3 = ipGenerator.ipGen(oct3, 64)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 19:
            oct3 = ipGenerator.ipGen(oct3, 32)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 20:
            oct3 = ipGenerator.ipGen(oct3, 16)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 21:
            oct3 = ipGenerator.ipGen(oct3, 8)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 22:
            oct3 = ipGenerator.ipGen(oct3, 4)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 23:
            oct3 = ipGenerator.ipGen(oct3, 2)
            oct4 = ipGenerator.ipGen(oct4, 256)
        case 24:
            oct4 = ipGenerator.ipGen(oct4, 256)
            print(oct4)
        case 25:
            oct4 = ipGenerator.ipGen(oct4, 128)
            print(oct4)
        case 26:
            oct4 = ipGenerator.ipGen(oct4, 64)
            print(oct4)
        case 27:
            oct4 = ipGenerator.ipGen(oct4, 32)
            print(oct4)
        case 28:
            oct4 = ipGenerator.ipGen(oct4, 16)
            print(oct4)
        case 29:
            oct4 = ipGenerator.ipGen(oct4, 8)
            print(oct4)
        case 30:
            oct4 = ipGenerator.ipGen(oct4, 4)
            print(oct4)
        case 31:
            oct4 = ipGenerator.ipGen(oct4, 2)
            print(oct4)
        case 32:
            print("There's only one IP address in this subnet...stoopid.")

    ipAddr = []
    for i in range(len(oct1)):
        for j in range(len(oct2)):
            for k in range(len(oct3)):
                for l in range(len(oct4)):
                    ipAddr.append(f"{oct1[i]}.{oct2[j]}.{oct3[k]}.{oct4[l]}")
    
    return ipAddr