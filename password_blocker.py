import time
from datetime import datetime as dt

hosts_path ="/etc/hosts" # the host path
redirect = "127.0.0.1" # the redirect ip
website_list =["www.facebook.com", "facebook.com", "www.nairaland.com"] # website links to restrict
now = dt.now() # creating a variable to hold the present date and time
start_time = now.replace(hour=8, minute=0, second=0, microsecond=0)  # time to start restricting access
end_time = now.replace(hour = 17, minute = 0, second = 0, microsecond= 0) # time to end website restriction

while True: # infinite loop to ensure the program is always running
    if now > start_time and now > end_time: #comparing if the present time is within the restricted time
        print("fun hours")
    else:
        print("you should be working")
    time.sleep(5)
