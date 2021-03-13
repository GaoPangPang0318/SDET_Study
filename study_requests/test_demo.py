"""
演练课程：接口请求构造GET/POST/PUT/HEAD
"""
import requests
from jsonpath import jsonpath
from requests.auth import HTTPBasicAuth


class TestDemo:
    #简单的HTTP请求方法的构造
    def test_demo(self):
        r=requests.get('https://httpbin.org/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert  r.status_code==200

    #get query请求方法的构造——get方法：params参数
    def test_get(self):
        payload={
            "level":1,
            "name":"gaopangpang"
        }
        r=requests.get('https://httpbin.org/get',params=payload)
        print(r.text)
        assert r.status_code==200

    #Form请求参数构造——post方法：data参数
    def test_form(self):
        payload = {
            "level": 1,
            "name": "gaopangpang"
        }
        r = requests.post('https://httpbin.org/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    #文件上传——post方法:files参数
    # 无环境，不演练
    #files={'file':open('report.xsl','rb')}
    #r=requests.post(url,files=files)

    #header构造——get方法：headers参数
    def test_header(self):
        headers = {
            "H":"header_gaopangpang",
            "User-Agent": "gaopangpang-app/0.0.1"
        }
        r = requests.get('https://httpbin.org/get', headers=headers)
        print(r.text)
        assert r.status_code == 200
        #断言
        assert r.json()['headers']["H"]=='header_gaopangpang'

    #cookie构造——get方法：cookies参数
    def test_cookie(self):
        cookies = dict(cookies_are='working')
        r = requests.get('https://httpbin.org/get', cookies=cookies)
        print(r.text)
        assert r.status_code == 200

    #Json请求体构造——post方法：json参数
    def test_post_json(self):
        payload={
            "level":1,
            "name":"gaopangpang"
        }
        r=requests.post('https://httpbin.org/post',json=payload)
        print(r.text)
        assert r.status_code==200
        assert r.json()["json"]["level"]==1

    #XML请求构造——post方法：参数data=xml headers=headers
    #xml=【xml结构内容】
    #headers={"Content-Type": "application/xml"}
    #r=requests.post('https://httpbin.org/post',data=xml,headers=headers)
    #不做多余演示

    #JSON Path 断言
    def test_json_path(self):
        r=requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code==200
        print(jsonpath(r.json(), '$..name'))
        #使用jsonpath进行断言
        assert jsonpath(r.json(),'$..name')[8]=="霍格沃兹测试学院公众号"

    #HTTPBasic——认证体系
    def test_auth(self):
        r=requests.get(url="https://httpbin.org/basic-auth/gaopangpang/123",auth=HTTPBasicAuth("gaopangpang","123"))
        print(r)


    

