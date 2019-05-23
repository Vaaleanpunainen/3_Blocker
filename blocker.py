import time
from datetime import datetime as dt

hosts_temp = r"hosts"
hosts_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com"]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 10)) < dt.now() < (dt(dt.now().year, dt.now().month, dt.now().day, 15)):
        print("Working hours...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for ws in websites_list:
                if ws in content:
                    pass
                else:
                    file.write(redirect + " " + ws + "\n")
    else:
        print("Free time...")
    time.sleep(5)
