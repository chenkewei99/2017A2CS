import base64
import urllib

'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v2/match"


f = open('Angry.png', 'rb')
# 参数images：图像base64编码
img1 = base64.b64encode(f.read())
# 二进制方式打开图文件
f = open('Smiling.png', 'rb')
# 参数images：图像base64编码
img2 = base64.b64encode(f.read())

params = {"images":img1 + ',' + img2}
params = urllib.urlencode(params)

access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
request = urllib.Request(url=request_url, data=params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.urlopen(request)
content = response.read()
if content:
    print (content)