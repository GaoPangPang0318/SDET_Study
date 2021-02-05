from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHybridapp:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True,
            "skipDeviceInitialization": True,
            #"chromedriverExcutable": "E:\Android\chromedriver\chromedriver_2.240"  # mumu模拟器
            "chromedriverExcutable":"E:/Android/chromedriver/chromedriver_2.20"  #android自带模拟器
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)

    def tearndown(self):
        self.driver.quit()

    def test_hybridapp(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="交易"]').click()
        app_context=self.driver.contexts
        print(app_context)
        self.driver.switch_to.context(app_context[-1])
        self.driver.find_element(MobileBy.XPATH,'//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/div').click()
        el_phone = (MobileBy.XPATH,'//*[@id="phone-number"]')

        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(el_phone))
        self.driver.find_element(*el_phone).send_keys("13800000001")

        self.driver.find_element(MobileBy.XPATH,'//*[@id="code"]').send_keys("1234")
        self.driver.find_element(MobileBy.XPATH,"/html/body/div/div/div[2]/div/div[2]/h1").click()
        print(self.driver.find_element(MobileBy.XPATH, '//*[@class="toast"]').text())
