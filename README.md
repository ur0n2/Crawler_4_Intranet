# Crawler 4 Intrnet
- Practice to crawaling.

## Ordinal
- 26th: 201702~201708
- 25th: 201608~201702
- 24th: 201602~201608
- 23th: 201508~201602


## DIrectory Tree
```
login.py(ahn_crawl.py)
user_list.csv
except_hack.csv
except_id.csv
/legacy
/save
/_Files
/substitution_html
/convert_to_pdf
```

## except_hack.csv
- Hack query excepted user list.

## except_id.csv
- ID(selectSTE) overlap list.

## /legacy
- Just legacy directory.


## /save
- Export to the html files.


## /_Files
- Include *.js, *.css, *.ico


## /substitution_html
- Change *.js, *.css, *.ico path
- Change textarea rows size


## /convert_to_pdf
- Convert substitution-html to pdf

## Convert korean name to english name
- [Link](http://blog.daum.net/_blog/BlogTypeView.do?blogid=07TCh&articleno=11018047)

## For Development Comment
- len(r.text) == 648 is user id exist, 635 is not exist
- Get the user list in admin.page
1. Get the pass_id.csv from parsing.py
2. Except my name in pass_id.csv and copy to root directory.
3. 'id_verification' of function in lets.py, Verify the id from pass_id.csv
4. Export to html
5. substitution html tag for related to file path.
6. Convert to pdf -> 마땅한 모듈이 없어서 pass, pdf online 많은거 보면 다른 플랫폼에서 해야겠다. html로 봐도 깔끔하고

- 세션 넣고 with 주석 풀고 실행만 하면됨 23th ~ 26th month 5

## Password Change
http://10.2.102.150/AhnTree/member/modify_proc.jsp?id=jhlee.trainee&pass=123123&email=jhlee.trainee@ahnlab.com&auth=2&trainee_group=26&expired_date=&originpass=dfb53af394625a5610aeeb760f8a3d10

- original password의 true/false 상관없이 6자리 이하도 수정이됨. 
- 로그인시에도 js단에서만 막아둠
- auth에서 1/2/3 권한으로 계정 변경 가능할지
