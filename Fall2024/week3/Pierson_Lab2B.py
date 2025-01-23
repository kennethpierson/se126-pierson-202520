#Name Ken Pierson
#W3 # Lab2B
#Date October 17, 2024
#SE116.02

#PROGRAM PROMPT: Rewrite Lab 2A but use input statements for: the available storage of the NAS in TB, number of videos weekly, and the average size of each video in GB. Display all input information back to the user and also include their days remaining of storage at their current rate as well as the storage days remaining if the rate were to triple.

#VARIABLE DICTIONARY
#total_storage      available storage of the NAS in TB
#video_size         average size of each video in GB
#videos_per_week    number of videos weekly


#---------------------------------------------------------------------

#start code below :]

#Step 1: Assign Known or Gather Needed Data
print()
total_storage = float(input("Enter total available storage space in TB: "))
video_size = float(input("Enter the average video size in GB: "))
videos_per_week = int(input("Enter the number of videos uploaded for the week: "))

#Step 2: Manipulate or create new data

total_storage_gb = total_storage * 1000
weekly_uploads =  video_size * videos_per_week
weeks_remaining = total_storage_gb / weekly_uploads
days_remaining = weeks_remaining * 7
days_remaining_x3 = days_remaining / 3

#Step 3: Output/Display the Solution Results

print()
print(f"Total Storage:                   {total_storage:.1f} TB")
print(f"Average Video Size:              {video_size:.1f} GB")
print(f"Videos Uploaded:                 {videos_per_week}")
print(f"Current upload rate:             {days_remaining:.1f} Days till storage is Full")
print(f"Triple the current upload rate:  {days_remaining_x3:.1f} Days till storage is Full\n")
