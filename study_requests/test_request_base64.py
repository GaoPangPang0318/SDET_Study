"""
第十阶段：接口测试框架——基于加密接口的测试用例设计
  1.调用Python自带的base64，直接对返回的响应做解密，即可得到解密后的响应
"""
import base64
import json
import requests


def test_encode_base64():
    url="http://127.0.0.1:9999/demo.txt"
    r=requests.get(url=url)
    res=json.loads(base64.b64decode(r.content))
    print(res)