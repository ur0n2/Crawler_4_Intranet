#-*-coding: utf-8-*-
import requests
import csv
import urllib
import sys
import os
from bs4 import BeautifulSoup

def b64ff_module_check():
    sys.path.append("lib")

    try:
        import b64ff
        print("[+] b64ff.py import success.")
    except:
        print("[+] b64ff.py library downloding...")
        os.mkdir("lib")
        urllib.urlretrieve("https://raw.githubusercontent.com/ur0n2/b64ff/master/b64ff.py", "lib/b64ff.py")


"""
<textarea name="write" cols="50" rows="10"> notenotenotneotnoe </textarea>
len<2
"""

def letscleaning(sessionid, day):
    #url = "http://10.2.102.150/AhnTree/attendance/write_attendance.jsp"
    url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL2F0dGVuZGFuY2Uvd3JpdGVfYXR0ZW5kYW5jZS5qc3A=" 
    url = b64ff.decode_base64(url)

    cookies = {'JSESSIONID':sessionid}
    payload = {'write':' ', 'attendancename':'jhlee.trainee', 'attendanceday':day} #2017-06-09

    r = requests.post(url, cookies = cookies, data = payload)

    if r.status_code == 500:
        print("[-] Status code is 500 Internal Error")
        #except list save
        with open("except_day_cleaning.csv", "a") as f: 
            data = day
            f.write(data)
            f.write('\n')
        return 
    elif r.status_code == 200:
        #print("[-] Status code is 200 OK")
        print("[-] " + str(day) + " OK")
        pass 
    else: 
        print("[-] what is situation?" + r.status_code)
        pass


if __name__ == '__main__':
    b64ff_module_check()
    import datetime
    import b64ff


    sessionid = "B305C09F234EE257B30791A3F6D7B5E6"

    print("[+] Let's clean the pages.")
    with open("daynote_day.txt", "r") as f:
        date = f.readlines()
        lines = [line.rstrip('\n') for line in date]

    for date in lines:
        days = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        print days #days.date()말고 days로 보내면 초까지 가지는데 시간이 추가됨 ㅋㅋ오호.. 
        letscleaning(sessionid, days)
    
    print("[-] Clean the day record.")
    