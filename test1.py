#-*-coding:utf-8-*-
import requests
import base64

def export_to_html(r):
	f = open("export_to_html\\" + i + ".html", "w") #
	f.write(r.content)
	f.close()
	#url base64 decode for github

	"""
	loop: http://10.2.102.150/AhnTree/attendance/set_page.jsp?selectSTE=jhlee.trainee&month=02&year=2017
	base_url = "http://10.2.102.150/AhnTree/attendance/set_page.jsp?selectSTE="
	values = {"id:"A', "pass":"B"} # load_user_list to the input 

	"""
	"""
	.ico
	kube.css
	common.css definetely path change
	

	Warning: Failed to load c://common.css (ignore)
	Warning: Failed to load file:///AhnTree/css/kube.css (ignore)
	Warning: Failed to load file:///AhnTree/css/common.css (ignore)
	Warning: Failed to load file:///AhnTree/resource/AhnLab_CI.png (ignore)
	"""

def substitution_html():
	f = open('t.txt','r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace("ython","PPPPPJYTHON")

	f = open('tt.txt','w')
	f.write(newdata)
	f.close()

	with open('t.txt', 'r') as file :
	  filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('ython', 'GGGGGGG')

	# Write the file out again
	with open('ttt.txt', 'w') as file:
	  file.write(filedata)
	
def convert_to_pdf():
	"""
	wkhtmltopdf
	C:\Users\Administrator>wkhtmltopdf c:\\asd.html c:\\out.pdf
	Loading pages (1/6)

	subprocess or import pdfkit

	pdfkit.from_file('test.html', 'out.pdf')
	"""
	pass	

def login(): #auto login omission
	#url = "http://10.2.102.150/AhnTree/attendance/set_page.jsp" 
	#'url'?selectSTE=jhlee.trainee&month=02&year=2017'
	url = "aHR0cDovLzEwLjIuMTAyLjE1MC9BaG5UcmVlL2F0dGVuZGFuY2Uvc2V0X3BhZ2UuanNw"
	url = base64.decodestring(url)
	cookies = {"JSESSIONID":"F03EAC33A6D3381F2CA28777DE3640D2"}

	r = requests.get(url, cookies = cookies)

	#r.header #include JSESSIONID이라서 get 할 수 있음 매번 세션값 안넣고

	if r.status_code == 500:
		print "r.status_code is 500 Internal Error"
		pass #r.status_code == 500: name+ 01 try
		#excpet난거 축적해서 프린트 예외 
		"""
		#substition

		f = open('t.txt','r')
		filedata = f.read()
		f.close()

		newdata = filedata.replace("ython","PPPPPJYTHON")

		f = open('tt.txt','w')
		f.write(newdata)
		f.close()

		with open('t.txt', 'r') as file :
		  filedata = file.read()

		# Replace the target string
		filedata = filedata.replace('ython', 'GGGGGGG')

		# Write the file out again
		with open('ttt.txt', 'w') as file:
		  file.write(filedata)
	 	"""
	elif r.status_code == 200:
		print "r.status_code is 200 OK"
		export_to_html(r)
		#with open("/Users/apple/Desktop/sample.jpg", 'wb') as f:
			#f.write(response.content)
	else: #I expect to 'r.status_code == 200'
		pass


def load_user_list():
	user_list = {"A":"B"} # fopen file 4 #user name+01
	#test jypark01

	f = open('user_list.txt', 'w')

def main():
	print "main"

	#load_user_list()
	login()

	substitution_html()
	convert_to_pdf()

	a = raw_input("Do you want some download to *.css file? (y or yes)")

	if a == 'y' or a == 'yes':
		pass
	elif:
		exit()

if __name__ == '__main__':
	main()
	
#todo: everyday blank through selenium 
