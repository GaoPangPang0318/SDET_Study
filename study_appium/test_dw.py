from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    @pytest.mark.skip
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

    @pytest.mark.skip
    def test_attribute(self):
        """
            1.打开雪球应用
            2.定位首页搜索框
            3.判断搜索框是否可用，并检查搜索框框name属性值
            4.打印搜索框这个元素的左上角坐标和他的宽高
            5.向搜索框输入：alibab
            6.判断【阿里巴巴】是否可见
            7.如果可见，打印搜索成功，否则打印“搜索失败
        """
        #定位搜索框元素
        el_search=self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        print("搜索框name：",el_search.text)
        print("搜索框坐标：",el_search.location)
        print("搜索框宽高：",el_search.size)
        if el_search.is_enabled():
            el_search.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            alibaba_el=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            el_display=alibaba_el.get_attribute("displayed")
            if el_display=="true":
                print("搜索成功")
            else:
                print("搜索失败")

    @pytest.mark.skip
    def test_touchaction(self):
        #定义 touchaction
        action=TouchAction(self.driver)

        #获取窗口大小
        windows_rect=self.driver.get_window_rect() #获取窗口大小
        print(windows_rect)
        width=windows_rect['width']
        height=windows_rect['height']
        x1=int(width/2)
        y_1=int(height*0.8)
        y_2=int(height*0.2)

        #显示等待
        #显示等待判断元素，元祖   （定位方式，定位值）
        locator=(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/home_search']")
        #显示等待使用格式   expected_conditions 后面条件得知道能更些啥
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))

        #touchaction方法，不要忘记perform（）
        action.press(x=x1,y=y_1).wait(200).move_to(x=x1,y=y_2).release().perform()

    @pytest.mark.skip
    def test_uiaotmator(self):
        """
          1.点击我的，进入个人信息页面
          2.点击登录，进入到登录页面
          3.输入用户名和密码
          4.点击登录
        """
        locator = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/home_search']")
        # 显示等待使用格式   expected_conditions 后面条件得知道能更些啥
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

        #uiautomator定位方法  虽然快，但是容易出错
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()   #必须使用‘  ’ ，find_element_by_android_uiautomator('new UiSelector().text("我的")')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('18362947918')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('gjj920318')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        sleep(5)

        #处理导入自选股票弹框，选择“取消”
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tv_left")').click()

        #滚动查找元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("雪球")').click()
        self.driver.find_element_by_android_uiautomator('resourceId("com.xueqiu.android:id/title_text").text("关注")').click()

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("酒鬼酒(SZ000799)").instance(0))').click()
        sleep(5)


    def test_parametrizesearch(self):
        pass


if __name__ == '__main__':
    pytest.main()