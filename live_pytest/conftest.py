# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : Lagou
# @File         : conftest
# @Time         : 2021/5/11 9:20
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import pytest
import yaml


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        #item.name 用例名称
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        #item.nodeid 用例路径
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'login' in item.nodeid:
            item.add_mark(pytest.mark.login)
    items.reverse()

def pytest_addoption(parser):
    mygroup=parser.getgroup("gaopangpang")
    mygroup.addoption("--env",default='test',dest='env',help='set your run env')

@pytest.fixture(scope='session')
def cmdoption(request):
    env=request.config.getoption('--evn',default='test')
    if env=='test':
        print('test 环境')
        datapath='datas/test/datas.yaml'
    elif env=='dev':
        print('test 环境')
        datapath = 'datas/dev/datas.yaml'

    with open(datapath) as f:
        datas=yaml.safe_load(f)
        return env,datas
