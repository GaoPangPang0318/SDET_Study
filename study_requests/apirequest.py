"""
第十阶段：接口测试框架——基于加密接口的测试用例设计
    2.封装对于不同算法的处理方法
"""
#定义一个解密处理方法的类
import base64
import json
import requests


class ApiRequests:
    #data的结构，应该放在测试用例中
    # req_data={
    #     "method":"get",
    #     "url":"http://127.0.0.1:9999/demo.txt",
    #     "headers":None,
    #     "encoding":"base64"
    # }

    def send(self,data:dict):
        #二次封装requests
        res=requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"]=="base64":
            return json.loads(base64.b64decode(res.content))

        #把加密过后的响应值发送给第三服务，让第三方服务做解密然后返回解密后的信息
        elif data["encoding"]=="private":
            return requests.post("url",data=res.content)