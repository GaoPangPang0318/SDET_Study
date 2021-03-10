from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestToast:
    def setup(self):
        desired_caps={
            "platformName":"Android",
            "platformVersion":"6.0",
            "deviceName":"emulator-5554",
            "appPackage":"com.example.android.apis",
            "appActivity":".view.PopupMenu1",  #直接进入Views/PopupMenu界面,如是正规APP不可以正常使用
            "automationName":"uiautomator2"  #捕获toast的话，一定要在初始化说明使用uiautomator2
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        """
        软件：android api study_httprunner
        定位工具：uiautomatorviewer
        操作：获取toast的text
             1.进入Views/PopupMenu，点击MAKE A POPUP
             2.点击search
             3.出现toast，只能通过xpath定位，其他定位方式不正确，获取text
        """
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.Button').click()
        self.driver.find_element(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.TextView').click()
        #print(self.driver.page_source)  #打印出page_sourcce 才能查看到toast相关信息，然后使用xpaath定位
        #定位方式一
        #print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        #定位方式二,text属性中包含内容来查找
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text)

