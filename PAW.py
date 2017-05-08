#-*-coding:utf-8-*-
import requests
import base64
import argparse
import pdfkit


def download_css_file()
	pass


def convert_to_pdf():
	"""
	wkhtmltopdf
	C:\Users\Administrator>wkhtmltopdf c:\\asd.html c:\\out.pdf
	Loading pages (1/6)

	subprocess or import pdfkit

	pdfkit.from_file('test.html', 'out.pdf')
	"""
	pass	


def main():
	print "main"

	#load_user_list
    with open('user_list.txt', 'w') as f: #count the user_count
        for i, l in enumerate(f):
            pass
    	user_count = i + 1
    #print readlines
    #f.close()

	user_list = {"A":"B"} # fopen file 4 #user name+01
	#test jypark01

	for user in user_count:
		#login
		url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL2F0dGVuZGFuY2Uvc2V0X3BhZ2UuanNw"
		url = base64.decodestring(url)
		cookies = {"JSESSIONID":"F03EAC33A6D3381F2CA28777DE3640D2"}

		r = requests.get(url, cookies = cookies)
		#r.header #include JSESSIONID이라서 get 할 수 있음 매번 세션값 안넣고

		if r.status_code == 500:
			print "r.status_code is 500 Internal Error"
			pass #r.status_code == 500: name+ 01 try
			#excpet난거 축적해서 프린트 예외 
		elif r.status_code == 200:
			print "r.status_code is 200 OK"
				f = open("export_to_html\\" + user + ".html", "w") #
				f.write(r.content)
				f.close()
		else: 
			pass


	a = raw_input("Do you want some download to *.css file? (y or yes)")

	if (a == 'y') or (a == 'yes'):
		pass
		download_css_file()
	elif:
		exit()
	
	print("Run to convert to *.pdf")	
	convert_to_pdf()

if __name__ == '__main__':
	main()
	


#tod: everyday blank through selenium 
