#-*-coding: utf-8-*-
#그날이 평일인지 일기가 있는지로 체크 내가 일기 쓴날만 체크 지우기 위해서 ㅋㅋ 
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
def viewday(sessionid, days): #pretest and verification
    #url = "http://10.2.102.150/AhnTree/attendance/view_day.jsp"
    url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL2F0dGVuZGFuY2Uvdmlld19kYXkuanNw"
    url = b64ff.decode_base64(url)
    cookies = {'JSESSIONID':sessionid}
    payload = {"selectSTE":"jhlee.trainee", "month":days.month, "year":days.year, "day":days.day}
    r = requests.post(url, cookies = cookies, data = payload)

    soup = BeautifulSoup(r.text, 'html.parser')    
    data = soup.findAll('textarea')[0].get_text()
    length = len(data)

    if length < 2:
        pass #print "no" #"[-] " + str(days) + " is none: " + str(length)
    else:
        with open("daynote_day.txt", "a") as f:
            print days
            f.write(str(days)+"\n")



if __name__ == '__main__':
    b64ff_module_check()
    import datetime
    import b64ff
    
    with open("daynote_day.txt", "w") as f:
        f.write('')

    sessionid = "B305C09F234EE257B30791A3F6D7B5E6"

    print("[+] Start viewday")
    date1 = #'2017-02-15' 
    date2 = '2017-08-11' #2017-08-15
    
    start = datetime.datetime.strptime(date1, '%Y-%m-%d')
    end = datetime.datetime.strptime(date2, '%Y-%m-%d')
    
    step = datetime.timedelta(days=1)


    while start <= end:
        days = start.date()        
        viewday(sessionid, days) #month, year, day
        start += step
    
    print("[-] End viewday")


