class credential: 
    def id_overlap_check():
        url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL21lbWJlci9pZENoZWNrLmpzcD9pZD0="
        url = base64.b64decode(url)
        
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
        url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL21lbWJlci9pZENoZWNrLmpzcD9pZD0="
        url = base64.b64decode(url)
        
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
    import base64

    lollol = credential()
    lollol.id_overlap_check()
    lollol.id_verification()
