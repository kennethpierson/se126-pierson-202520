
valid_ip = False


print()
print("Welcoming to IP Classing! Being Classful is our only Goal!\n")

answer = "y"

while answer == "y":
    try:
        while valid_ip == False:
            ip_address = input(f"Please enter an IP Address [1.0.0.0 - 255.255.255.255]: ")
            octet = ip_address.split(".")
            octet_1_convert = int(octet [0]) 
            first_octet = (octet_1_convert)
            octet_2_convert = int(octet [1])
            second_octet = (octet_2_convert)
            octet_3_convert = int(octet [2])
            third_octet = (octet_3_convert)
            octet_4_convert = int(octet [3])
            fourth_octet = (octet_4_convert)
            if first_octet > 0 and first_octet <= 255 and second_octet > 0 and second_octet <= 255 and third_octet > 0 and third_octet <= 255 and fourth_octet > 0 and fourth_octet <= 255:
                valid_ip = True
            else:
                print("*** Invalid IP Address! Please Try Again ***")
        if first_octet > 0 and first_octet <= 127:
            a_class = "A"
            a_mask = "225.0.0.0"
            print("\n****IP Information (Classful)****\n")
            print(f"IP address:  {ip_address}" )
            print(f"Subnet Mask: {a_mask}")
            print(f"IP Class:    Class {a_class}")
        elif first_octet >= 128 and first_octet <= 191:
            b_class = "B"
            b_mask = "255.255.0.0"
            print("\n****IP Information (Classful)****\n")
            print(f"IP address:  {ip_address}" )
            print(f"Subnet Mask: {b_mask}")
            print(f"IP Class:    Class {b_class}")
        elif first_octet >= 192 and first_octet <= 223:
            c_class = "C"
            c_mask = "255.255.255.0"
            print("\n****IP Information (Classful)****\n")
            print(f"IP Address:  {ip_address}")
            print(f"Subnet Mask: {c_mask}")
            print(f"IP Class:    Class {c_class}")
        elif first_octet >= 224 and first_octet <= 239:
            d_class = "D"
            print("\n****IP Information (Classful)****\n")
            print(f"IP Address:  {ip_address}")
            print(f"Subnet Mask: No default subnet mask. Used for multicast")
            print(f"IP Class:    Class {d_class}")
        elif first_octet >= 240 and first_octet <= 255:
            e_class = "E"
            print("\n****IP Information (Classful)****\n")
            print(f"IP Address:  {ip_address}")
            print(f"Subnet Mask: No default subnet mask. Reserved for experimental purposes")
            print(f"IP Class:    Class {e_class}")
        else:
            print("Not a Valid IP Address!")
        print()
        answer = input("Would you like to enter another IP Address? [y/n]: ").lower()
        valid_ip = False
    except:
        print("BOOO THAT'S A BAD INPUT!")
print("The Program has Ended! Now get out there and Class Up your Network\n")
