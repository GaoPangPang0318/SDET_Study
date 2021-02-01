"""
作业要求：
    1.创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
    2.将 fixture 方法存放在 conftest.py ，设置 scope=module
"""
import yaml
import pytest
from python_pytest.calculator.calculator import Calculator

# 一次性加载测试数据文件
with open("../datas/cal_datas.yml") as f:
    cal_datas = yaml.safe_load(f)

# 获取加法的测试数据和ids，并进行fixture参数化
add_datas = cal_datas["add"]["datas"]
add_ids = cal_datas["add"]["ids"]


@pytest.fixture(scope="module", params=add_datas, ids=add_ids)
def get_datas_add(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算结束")


# 获取减法的测试数据和ids，并进行fixture参数化
sub_datas = cal_datas["sub"]["datas"]
sub_ids = cal_datas["sub"]["ids"]


@pytest.fixture(scope="module", params=sub_datas, ids=sub_ids)
def get_datas_sub(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算结束")


# 获取乘法的测试数据和ids，并进行fixture参数化
mul_datas = cal_datas["mul"]["datas"]
mul_ids = cal_datas["mul"]["ids"]


@pytest.fixture(scope="module", params=mul_datas, ids=mul_ids)
def get_datas_mul(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算结束")


# 获取除法的测试数据和ids，并进行fixture参数化
div_datas = cal_datas["div"]["datas"]
div_ids = cal_datas["div"]["ids"]


@pytest.fixture(scope="module", params=div_datas, ids=div_ids)
def get_datas_div(request):
    print("开始计算")
    data = request.param
    yield data
    print("计算结束")


@pytest.fixture(scope="module")
def get_calc():
    """
        获取计算器实例
    :return: 计算机实例
    """
    calc = Calculator()
    return calc
