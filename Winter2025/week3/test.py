#--IMPORTS---------------------------------------------
import csv

#--FUNCITONS-------------------------------------------

#--MAIN EXECUTING CODE---------------------------------

#create empty list for every potential field in the file
comp_type = []      #computer type Desktop or Laptop
comp_mfr = []       #for the computer manufacturer
comp_cpu = []       #processor type
comp_ram = []       #total ram
hd_1 = []           #hard drive one
number_hd = []      #number of hard drives
hd_2 = []           #hard drive two
os = []             #operating system
yr = []             #year the machine was purchased

#initialize the counting variables

#-----connected to file--------
with open("text_files/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        if record[0] == "D":
            comp_type.append("Desktop")
        else:
            comp_type.append("Laptop")

        if record[1] == "DL":
            comp_mfr.append("Dell")
        elif record[1] == "GW":
            comp_mfr.append("Gateway")
        elif record[1] == "HP":
            comp_mfr.append("HP")
        
        comp_cpu.append(record[2])
        comp_ram.append(int(record[3]))
        hd_1.append(record[4])
        number_hd.append(int(record[5]))
                
        if int(record[5]) == 1:
            hd_2.append("-" * 5)
            os.append(record[6])
            yr.append(record[7])
        else:    
            hd_2.append(record[6])
            os.append(record[7])
            yr.append(record[8])

print(f"\n{"Type":<10} {"Brand":<10} {"CPU":<5} {"RAM":<5} {"1st Disk":<10} {"No HDD":<10}{"2nd Disk":<10}  {"OS":<5} {"YR"}")
print("-" * 80)
for i in range(0, len(comp_type)):
    print(f"{comp_type[i]:<10} {comp_mfr[i]:<10} {comp_cpu[i]:<5} {comp_ram[i]:<5} {hd_1[i]:<10} {number_hd[i]:<10} {hd_2[i]:<10} {os[i]:<5} {yr[i]}")

old_desktops = 0
old_laptops = 0

for i in range(0, len(yr)):
    if int(yr[i]) <= 16:
        if comp_type[i] == "Desktop":
            old_desktops += 1
        else:
            old_laptops += 1

#-----Final Output--------        
print("-" * 80)
print(f"\nTotal number of computers: {len(comp_type)} ")
print(f"Total number of desktops to replace: {old_desktops} ")
print(f"Total cost for desktop replacement: ${old_desktops * 2000:.2f}")
print(f"Total number of laptops to replace:  {old_laptops} ")
print(f"Total cost for laptop replacement:  ${old_laptops * 1500:.2f}")
print("\nThank you for using the program. Goodbye.\n")