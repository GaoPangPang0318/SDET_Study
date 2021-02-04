"""
课堂演示：
   使用uiautomatorviewer定位webview元素
   注意：uiautomatorviewer虽然可以定位webview元素，但是由于不同设备，不同手机渲染出来的效果不同，因此定位元素的信息会出现差别，当更换设备后再测试会出现问题

   模拟器：mumu
   软件：apidemo
   操作：点击view，进入新界面
        下滑点击webview
        文本框sendkeys
        点击link
"""
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBroswer:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage":"io.appium.android.apis",  #apidemo
            "appActivity":".ApiDemos",
            "noReset":True,
            "skipDeviceInitialization":True,
            "chromedriverExcutable":"E:\Android\chromedriver\chromedriver_2.240"  #mumu模拟器
            #"chromedriverExcutable":"E:/Android/chromedriver/chromedriver_2.20"  #android自带模拟器
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # No Chromedriver found that can automate Chrome '44.0.2403'
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        #1.点击views
        self.driver.find_element_by_accessibility_id("Views").click()

        #2.新界面，找到webview并点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0))').click()

        #3.定位文本框，并sendkeys
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="i_am_a_textbox"]').send_keys("Hello,tester.")
        sleep(5)

        #4.定位链接元素，并点击
        self.driver.find_element_by_accessibility_id("i am a link").click()  #uiautomatorviewer中的content-desc就是accessibility_id
        sleep(5)



