"""
课后作业：
    1.补全计算器（加减乘除）的测试用例，编写用例顺序：加-除-减-乘
    2.创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
    3.将 fixture 方法存放在 conftest.py ，设置 scope=module
    4.控制测试用例顺序按照【加-减-乘-除】这个顺序执行
    5.结合 allure 生成本地测试报告
"""
import allure
import pytest


# 禁用原因：每调用一次都会open一次文件然后再关闭，当测试用例增多时既影响效率又占用资源，因此不是一个好方法
#
# def get_data(dataflag:str)->list:
#     """
#         获取yaml中的数据
#     :param dataflag: 获取测试数据类型标志  add：加法测试数据 sub:减法测试数据 mul：乘法测试数据 div：除法测试数据
#     :return:  测试数据和标记的list
#     """
#     with open("../datas/cal_datas.yml") as f:
#         data=yaml.safe_load(f)[dataflag]
#         testing_data=data['datas']  #测试数据
#         ids=data['ids']  #ids
#         return [testing_data,ids]

@allure.feature("测试计算器")
class TestCal:
    # 加法测试用例,并设置执行顺序为1
    @allure.story("加法测试")
    @pytest.mark.run(order=1)
    # @pytest.mark.parametrize("a,b,expect",get_data("add")[0],ids=get_data("add")[1])
    def test_add(self, get_calc, get_datas_add):
        with allure.step("计算两数之和："):
            result = get_calc.add(get_datas_add[0], get_datas_add[1])

        # 对浮点数测试用例，结果精确到小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_add[2]

    # 除法测试用例，并设置执行顺序为4
    @allure.story("除法测试")
    @pytest.mark.run(order=4)
    # @pytest.mark.parametrize("a,b,expect", get_data("div")[0], ids=get_data("div")[1])
    def test_div(self, get_calc, get_datas_div):
        with allure.step("计算两数之商："):
            result = get_calc.div(get_datas_div[0], get_datas_div[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_div[2]

    # 减法测试用例，并设置执行顺序为2
    @allure.story("减法测试")
    @pytest.mark.run(order=2)
    # @pytest.mark.parametrize("a,b,expect", get_data("sub")[0], ids=get_data("sub")[1])
    def test_sub(self, get_calc, get_datas_sub):
        with allure.step("计算两数之差："):
            result = get_calc.sub(get_datas_sub[0], get_datas_sub[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_sub[2]

    # 乘法测试用例，并设置执行顺序为3
    @allure.story("乘法测试")
    @pytest.mark.run(order=3)
    # @pytest.mark.parametrize("a,b,expect", get_data("mul")[0], ids=get_data("mul")[1])
    def test_mul(self, get_calc, get_datas_mul):
        with allure.step("计算两数之积："):
            result = get_calc.mul(get_datas_mul[0], get_datas_mul[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_datas_mul[2]
