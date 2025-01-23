#Name Ken Pierson
#W4 # Lab 4
#Date November 9, 2024
#SE116.02

#PROGRAM PROMPT: All end devices using IPv4 on a network require an IP address. IP addresses are classified as Class A, Class B Class C, Class D, or Class E. For the most part network administrators work with Class A, B, and C. Knowing an IP address’s class also reveals to you its default subnet mask, which can then be used to identify its network and host IDs. Each IP address consists of 4 octets. The first octet determines the class. 
#Write a program that will allow the user to enter as many IP addresses that they want. Each time an IP address is entered, the program should display back to the user: the full IP address, its class, and the class’s default subnet mask. For each IP address entered by the user, when redisplayed by the program, should appear exactly as it did when entered by the user including its . ). If the IP address is not a Class A, B, C, D, or E, the user should also be alerted and the entered IP address should still be reprinted.

#Class A - 1 - 127
#Class B - 128 - 191
#Class C - 192 - 223
#Class D - 224 - 239
#Class E - 240 - 255

#VARIABLE DICTIONARY


#---------------------------------------------------------------------

#start code below :]

print()
print("Welcoming to IP Classing! Being Classful is our only Goal!\n")

answer = "y"

while answer == "y":

    ip_address = input(f"Please enter an IP Address [1.0.0.0 - 255.255.255.255]: ")
    print()
    octet = ip_address.split(".")
    octet_1_convert = int(octet [0]) 
    first_octet = (octet_1_convert)
    
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

print("The Program has Ended! Now get out there and Class Up your Network\n")
