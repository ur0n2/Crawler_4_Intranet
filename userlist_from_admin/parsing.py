#-*- coding:utf-8 -*- 
from bs4 import BeautifulSoup

for z in xrange(3,7): #3.html~6.html -> 23th ~ 26th
	with open(str(z) + ".html", "r") as f:
		data = f.read()
		soup = BeautifulSoup(data, "html.parser")
		elements = soup.findAll('a') #a태그에서

		datas = []
		for x in elements:
			if x.get('onclick') == None: #onclick = None인것 제외하고
				pass
			else:
				datas.append(x.get('onclick')) #onclick="..."이 가리키는 값을 datas에 저장해라

		ste = []
		for x in datas: #get한 datas에서 "'", "="로 split해서 "="뒤에 있는 ste(software test engineer)의 이름을 얻어라   
			ste.append (str(x.split("'")[1].split("=")[1]) + "," + str(z+20))
		ste = list(set(ste))

		print(ste)

		for y in ste:
			with open("pass_id.csv", "a") as f1:
				f1.write(y)
				f1.write("\n")
#Need to except my name

"""
<tr style="padding:0px; text-align:center;">
<td style="padding:0px; text-align:center;">강지혜</td> <!-- 이름 -->
<td style="padding:0px; text-align:center;">2</td> <!-- 권한 -->
<td style="padding:0px; text-align:center;">2016-02-19</td> <!-- 종료날짜 -->
<td style="padding:0px; text-align:center;"><a href="#none" onclick="window.open('/AhnTree/admin/modify_ste.jsp?selectSTE=jhkang.trainee',
			'_blank','width=400,height=700,scrollbars=yes,resizeable=no,left=150,top=150');">수정</a></td>
<td style="padding:0px; text-align:center;"><a href="#none" onclick="window.open('/AhnTree/admin/delete_ste.jsp?selectSTE=jhkang.trainee',
			'_blank','width=400,height=220,scrollbars=yes,resizeable=no,left=150,top=150');">삭제</a></td>
"""