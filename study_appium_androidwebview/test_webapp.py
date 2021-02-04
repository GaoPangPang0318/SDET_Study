"""
课堂演示：
    1.打开手机浏览器。请求百度
    2.输入“appium”，点击搜索
说明：使用mumu自带浏览器
      uc devtools进行web元素分析
      SDK自带浏览器会自动打开默认google页面，因此导致appium无法正常geturl，问题怎么解决？？暂时不知，已经发帖求助
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBroswer:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            #"deviceName": "emulator-5554", #SDK模拟器
            "noReset":True,
            "skipDeviceInitialization":True,
            "browserName":"Browser",   #纯网页需要使用内置浏览器或者chrome，第三方不可以，因此需要表明浏览器
                                      #没有 apppackage 和appactivity
            "chromedriverExcutable":"E:\Android\chromedriver\chromedriver_2.240"  #mumu模拟器
            #"chromedriverExcutable":"E:/Android/chromedriver/chromedriver_2.20"  #android自带模拟器
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # No Chromedriver found that can automate Chrome '44.0.2403'
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        self.driver.find_element(MobileBy.XPATH,'//*[@type="search"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@type="search"]').send_keys("appium")

        # 报错：selenium.common.exceptions.ElementNotVisibleException: Message: element not visible
        #添加显示等待
        el_submit=(MobileBy.XPATH,'//*[@class="se-bn  se-bn-new"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(el_submit))

        #el_submit是元祖，find_element使用的时候得解构，因此得加*
        self.driver.find_element(*el_submit).click()
        sleep(10)
