"""
 企业微信外出打卡操作
   断言：打卡成功
   注意事项：动态网页的处理
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestWecomCockin:
    def setup(self):
        #设置初始化参数
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True  # 首次启动的时候，不停止APP，方便进行调试
        desired_caps['skipDeviceInitialization'] = True  # 跳过安装，权限设置等操作
        desired_caps['waitForIdleTimeout']=0  #动态页面等待时间设置，设置成0秒，当成已经加载好的页面进行处理

        # 创建driver对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wecom_clockin(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()

        #滑动屏幕后定位，次操作会先执行下拉刷新的操作，然后再进行滑动
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0))').click()

        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/awt"]').click()
        assert "外出打卡成功"==self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/pu']").text


