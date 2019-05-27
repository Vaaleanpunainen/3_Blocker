import time
from datetime import datetime as dt

hosts_temp = r"D:\PythonProjekty\Udemy\3_Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites_list = ["www.facebook.com", "facebook.com"]

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 10)) < dt.now() < (dt(dt.now().year, dt.now().month, dt.now().day, 15)):
        print("working time...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for ws in websites_list:
                if ws in content:
                    pass
                else:
                    file.write(redirect + " " + ws + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(ws in line for ws in websites_list):
                    file.write(line)
            file.truncate()
        print("Fun time...")
    time.sleep(5)
