"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/2/26 8:32 下午'
"""
from selenium.webdriver.common.by import By

# 登录页面的PO
#selenium.webdriver.remote.webdriver：最底层的webdriver，导入此WebDriver对象类型
from selenium.webdriver.remote.webdriver import WebDriver

from live_selenium_po.podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver:WebDriver): #标记driver类型，方便链接操作
        self.driver = driver

    def scan(self):
        '''
        扫码
        :return:
        '''
        pass

    def goto_register(self):
        # click register link
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # return RegisterPage()
        return RegisterPage(self.driver)

