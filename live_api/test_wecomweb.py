# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : Lagou
# @File         : test_wecomweb
# @Time         : 2021/3/26 10:26
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import requests
from requests_toolbelt import MultipartEncoder


def get_token():
    ID = 'ww598d3519e9646a48'
    SECRET = 'kJTlk5pRU6POdDk16k1avcYE1ZFXy4fPk4ICDUsN1jU'
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

    #POST 请求multipart/form-data 格式的方法
    #使用MultipartEncoder类
    m=MultipartEncoder(
        fields={
            'name':'media',
            #打开方式要是二进制的
            'filename':('members.csv',open('./files/members.csv','rb'),'application/octet-stream')
        },
        boundary='acebdf13572468'
    )
    headers={
        'Content-Type':m.content_type,
        'boundary':m.boundary,
    }
    r=requests.post(url,data=m,headers=headers)
    print(r.json())
    media_id=r.json()['media_id']



    #2.增量更新成员
    add_url=f'https://qyapi.weixin.qq.com/cgi-bin/batch/syncuser?access_token={get_token()}'
    data={
        'media_id':media_id
    }
    r=requests.post(add_url,json=data)
    print(r.json())




