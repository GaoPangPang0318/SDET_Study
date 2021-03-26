# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : Lagou
# @File         : test_wecomweb
# @Time         : 2021/3/26 10:26
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import requests

def get_token():
    ID = 'ww598d3519e9646a48'
    SECRET = 'kJTlk5pRU6POdDk16k1avSN6spNWux2zKpI8yUMVMLI'
    url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'
    token=requests.get(url).json()['access_token']
    print(token)
    return token

#成员管理部分接口：简单的GET和POST
def test_addmen():
    url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    add_body={
        'userid':'gaopangpang',
        'name':'高胖胖',
        "mobile": "+86 18312300000",
        'department':[1]
    }
    r=requests.post(url,json=add_body)
    print(r.json())
    assert 0==r.json()["errcode"]

def test_readmem():
    userid='GaoJingJing'
    url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid={userid}'
    r=requests.get(url)
    print(r.json())
    assert '高晶晶' == r.json()["name"]

#异步批量接口:增量更新成员信息
def test_increupdatemem():
    #参考博客:https://blog.csdn.net/qq_38486203/article/details/101711696
    #1.上传临时素材，获取media_id
    media_type='file'
    url=f'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={get_token()}&type={media_type}'
    data={"file":open('./files/members.csv','rb')}
    r=requests.post(url,data=data)
    print(r.json())

    #2.增量更新成员




