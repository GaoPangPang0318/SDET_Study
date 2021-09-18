import json

import requests

from live_requests.wework.base import Base


class Address(Base):
    def get_member_information(self, user_id):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": user_id
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()  #将断言与通用操作分离，不在通用操作类型进行断言操作，与PO规则相似。返回json用于测试用例进行判断

    def update_member(self, user_id, name, mobile):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
        }
        r = self.send("POST",url=update_member_url, json=data)
        return r.json()

    def create_member(self, user_id, name, mobile, department):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            'department': department
        }
        r = self.send("POST", url=create_member_url, json=data)
        return r.json()

    def delete_member(self, userid):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {"userid": userid}  #将url中所带参数信息很可能会比较多，因此单独拎出来，可以减少url的长度
        r = self.send("GET", delete_url, params=params)  #在发送请求的时候，将参数赋值给params
        return r.json()  #返回删除操作的记过

def test_data():
    data = {'a': 20}
    r = requests.post("https://httpbin.org/post",data=data)   #data=data：数据放在form字段，json=data的话，数据放在data中，且Content-Type显示json格式，
    print(r.json())