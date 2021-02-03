from time import sleep

from appium import webdriver


class TestBroswer:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "noReset":True,
            "browserName":"Browser"   #纯网页需要使用内置浏览器，第三方不可以，因此需要表明浏览器
                                      #没有 apppackage 和appactivity
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  #模拟器6.0 版本有点低 找不到对应的driver：No Chromedriver found that can automate Chrome '44.0.2403'
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)