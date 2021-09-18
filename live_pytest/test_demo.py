# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : Lagou
# @File         : test_demo
# @Time         : 2021/5/11 9:17
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import pytest


@pytest.mark.parametrize('name',['哈利','赫敏','罗恩'])
def test_demo(name):
    print(name)

def test_login():
    print("login")

def test_login_fail():
    print("login")
    assert False
def test_search():
    print("search")

def test_env(cmdoption):
    # print(cmdoption)
    env, datas = cmdoption
    print(datas)
    host = datas['env']['host']
    port = datas['env']['port']
    url = str(host) + ":" + str(port)
    print(url)
