import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook "]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 10)) < dt.now() < (dt(dt.now().year, dt.now().month, dt.now().day, 15)):
        print("Working hours...")
    else:
        print("Free time...")
    time.sleep(5)
