"""
This python script restricts access to certain websites during a specified time frame tro avoid distractions.

"""

import time
from datetime import datetime as dt


hosts_path ="/etc/hosts"  # the host path
redirect = "127.0.0.1"  # the redirect ip
website_list =["www.facebook.com", "facebook.com", "www.nairaland.com"]   # website links to restrict
now = dt.now()  # creating a variable to hold the present date and time
start_time = now.replace(hour=0, minute=0, second=0, microsecond=0)  # time to start restricting access
end_time = now.replace(hour =4, minute = 52, second = 0, microsecond= 0)  # time to end website restriction

while True:  # infinite loop to ensure the program is always running
    if now >=  start_time and now < end_time:  # comparing if the present time is within the restricted time
        print("working hours")
        with open(hosts_path, "r+") as file:  # opening the host file for read and write operations
            content = file.read() # saving the content of the host file in 'content'
            for site in website_list:  # checking if the sites in the website lists are in the hosts file
                if site in content:
                    pass
                else:
                    file.write(redirect+" " +site+"\n")  # writing the redirect IP and the IP's to block in the hosts file

    else:
        with open(hosts_path, "r+") as file:
            content =file.readlines() #
            file.seek(0)  # placing the pointer at the begining of the file
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()  # deletes all the content beneath the website list
        print("You can do other things now")
    time.sleep(5)  # makes the program run every 5 seconds