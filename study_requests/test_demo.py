"""
演练课程：接口请求构造GET/POST/PUT/HEAD
"""
import requests

class TestDemo:
    #简单的HTTP请求方法的构造
    def test_demo(self):
        r=requests.get('https://httpbin.testing-studio.com/get')
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
        r=requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code==200

    #Form请求参数构造——post方法：data参数
    def test_form(self):
        payload = {
            "level": 1,
            "name": "gaopangpang"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
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
        r = requests.get('https://httpbin.testing-studio.com/get', headers=headers)
        print(r.text)
        assert r.status_code == 200
        #断言
        assert r.json()['headers']["H"]=='header_gaopangpang'

    #cookie构造——get方法：cookies参数
    def test_cookie(self):
        cookies = dict(cookies_are='working')
        r = requests.get('https://httpbin.testing-studio.com/get', cookies=cookies)
        print(r.text)
        assert r.status_code == 200

