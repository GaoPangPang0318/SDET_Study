"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/2/26 8:31 下午'
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 首页的PO
from live_selenium_po.podemo.login_page import LoginPage
from live_selenium_po.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        '''
        进入登录页面
        :return:
        '''
        # click login button
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return LoginPage
        return LoginPage(self.driver)     #把首页初始的self.driver传参给loginPage， #返回一个RegisterPage实例

    def goto_register(self):
        '''
        进入到注册页面
        :return:
        '''
        # click register button
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # return RegisterPage
        return RegisterPage(self.driver)  #返回一个RegisterPage实例
