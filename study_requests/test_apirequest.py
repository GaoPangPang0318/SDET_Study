"""
测试apirequest功能的测试用例
"""
from study_requests import apirequest


class TestApiRequest:
    req_data={
        "method":"get",
        "url":"http://127.0.0.1:9999/demo.txt",
        "headers":None,
        "encoding":"base64"
    }

    def test_send(self):
       #实例化
       ar=apirequest.ApiRequests()
       print(ar.send(self.req_data).text)
