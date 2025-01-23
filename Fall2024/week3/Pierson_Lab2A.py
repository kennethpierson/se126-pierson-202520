#Name Ken Pierson
#W3 # Lab2A
#Date October 16, 2024
#SE116.02

#PROGRAM PROMPT: You are currently working for a small start-up company that produces short “How-to” videos. The company is currently producing videos for customers who need to know how to fix common networking problems. You oversee the company’s network and the owner of the company has just informed you that the company will also be producing “How-to” videos on how to install, configure and manage a Linux OS. You need to let the owner of the company know if you will have enough storage on your current NAS (Network Attached Storage). You currently have 250 videos stored on your NAS which occupy 1.4 TB of disk space. Your NAS has 8 TB of storage. The company is currently producing 15 videos a week with an average file size of 5.6 GB. The company expects to triple that average once they start producing videos for the OS. If the average file size of each video is 5.6 GB how long will it be before you run out of storage space? Tell the user how many days left of storage are available just by making their current How-To videos, as well as how many days are left if they started their How-To videos today (which increases the videos being produced weekly 3x). Every output value should be format rounded to the 1st decimal place. Write a program that will determine how many days of storage is left on the NAS. [Note: this means you will have two possibilities for days left of storage]

#VARIABLE DICTIONARY
#total_storage      8 TB
#space_used         1.4 TB
#video_size         5.6 GB
#videos_per_week    15


#---------------------------------------------------------------------

#start code below :]

#Step 1: Assign Known or Gather Needed Data

total_storage = 8
space_used = 1.4
video_size = 5.6
videos_per_week = 15

#Step 2: Manipulate or create new data

available_storage_tb = total_storage - space_used
available_storage_gb = available_storage_tb * 1000
weekly_uploads = videos_per_week * video_size
weeks_remaining = available_storage_gb / weekly_uploads
days_remaining = weeks_remaining * 7
days_remaining_x3 = days_remaining / 3

#Step 3: Output/Display the Solution Results

print()
print(f"Current Upload Rate:            {days_remaining:.1f} Days till Storage is Full")
print(f"Triple the Current Upload Rate: {days_remaining_x3:.1f} Days till Storage is Full\n")