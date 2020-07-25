import time
from datetime import datetime as dt
#r<- raw string means no \n \t ...etc
#OR "C:\\Windows\\System32\\drivers\etc\\hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
#temp use
host_temp=r"D:\Desktop\PyWin20-21\pythonMegaUdemy10proj\app3\hosts"
redirect="127.0.0.1" #browser will be redirected to this ip when u try to access forbidden websites
website_list=["www.facebook.com","facebook.com"]#["www..","..."]
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,7,25) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,7,32):
        with open(host_temp,'r+') as file: #r+ read + append
            content=file.read()
            for website in website_list:
                if website not in content:
                    file.write(redirect+" "+website+" "+"\n")

    else:
        with open(host_temp,'r+') as file:
            content_list=file.readlines()
            file.seek(0)
            for line in content_list:
                if not any([website in line for website in website_list]):
                    file.write(line)
            file.truncate()
