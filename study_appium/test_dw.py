import pytest
from appium import webdriver


class TestDw:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.view.WelcomeActivityAlias'
        desired_caps['noResrt']=True
        #首次运行APP后不对APP进行重置操作
        desired_caps['dontStopAppOnReset']=True
        #跳过app初始化需要获取权限的操作
        desired_caps['skipDeviceInintialization']=True
        # send_keys的值为中文的话得有以下两个条件
        desired_caps['unicideKeyBoard']=True
        desired_caps['resetKeyBoard']=True

        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        #隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_dw(self):
        print('搜索测试')
        """
        1.打开 雪球 app
        2.点击搜索输入框
        3.向搜索输入框输入 “阿里巴巴”   中文
        4.在搜索结果里面选择“阿里巴巴” 然后进行点击
        5.获取这只上 阿里巴巴的股价，并判断这只股价是否大于2000
        """

        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')

        #常会出现resource-id相同的元素，此时不能使用by_id来定位元素，得使用xpath并合并其他条件一起确认
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']").click()

        #获取元素的文本信息
        current_price=float(self.driver.find_element_by_id('com.xueqiu.android:id/stock_current_price').text)

        #断言操作
        assert  current_price>200

if __name__ == '__main__':
    pytest.main()