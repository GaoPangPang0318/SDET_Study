# content of test_sample.py
import pytest
import yaml


def func(x):
    return x + 1
@pytest.mark.parametrize('a,b',yaml.safe_load(open('./study_pytest/test_data.yaml')))   #参数化：将测试用以的变量参数化，可通过外部输入来传递
def test_answer(a,b):   #参数化后，方便生成多条测试用例
    assert func(a) == b

def test_a():
    assert  func(4)==5

@pytest.fixture()   #fixture：哪个函数需要此条件就在测试用例中调用此处方法
def login():
    username='Jerry'
    print("登录操作")
    return username

class TestDemo:
    #不能有__init__函数，否则会被当成一般函数处理
    def test_answer3(self,login):
        print(f"answer3 username = {login}")   #login方法名代表返回结果
        assert  func(5)==7

    def test_answer4(self):
        assert func(5)==6

    #测试函数名不满足test_* 和*_test 不执行
    def test_answer5(self,login):
        print(f"answer5 username {login}")
        assert func(5)==4



if  __name__=='__main__':
     pytest.main(['test_sample.py::test_answer','-v'])