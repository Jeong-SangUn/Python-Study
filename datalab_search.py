# import os
# import sys
# import urllib.request
# client_id = "m6iN62CAdaCQ6blzyE0j"
# client_secret = "jThz1pEIE2"
# encText = urllib.parse.quote("대구 달서구 이곡동 떡볶이")
# url = "https://openapi.naver.com/v1/search/local?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

import os
import sys
import urllib.request
import json

client_id = "IVFza5lJZlUKvtdHAB96"
client_secret = "YaCiR1HTI3"
url = "https://openapi.naver.com/v1/datalab/search"
body = '''
{
    "startDate":"2019-08-01",
    "endDate":"2019-09-09",
    "timeUnit":"month",
    "keywordGroups":[
        {"groupName":"분식","keywords":["떡볶이","라면"]}
        ],
        "device":"pc",
        "ages":["1","2","3"],
        "gender":"f"}
'''

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)