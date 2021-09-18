from appium import webdriver
from live_appium_po.pages.information_page import InformationPage

class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return InformationPage(self.driver)  #因为要复用一个driver，所以要传递driver
                                             #为何使用return？ 通过return实现链式调用
