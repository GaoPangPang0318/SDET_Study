from asyncio import sleep

from appium import webdriver
from study_appium_datadriven_sonwball.page.basepage import BasePage
from study_appium_datadriven_sonwball.page.main import Main


class App(BasePage):
    def setup(self):
        _package='com.xueqiu.android'
        _activity='.view.WelcomeActivityAlias'
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = _package
            desired_caps['appActivity'] = _activity
            desired_caps['noResrt'] = True
            # 首次运行APP后不对APP进行重置操作
            desired_caps['dontStopAppOnReset'] = True
            # 跳过app初始化需要获取权限的操作
            desired_caps['skipDeviceInintialization'] = True
            # send_keys的值为中文的话得有以下两个条件
            desired_caps['unicideKeyBoard'] = True
            desired_caps['resetKeyBoard'] = True
            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            # 隐式等待
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package,_activity)

        return self


    def teardown(self):
        self._driver.quit()


    def main(self):
        return Main(self._driver)  #跳转到哪个界面 就return那个类并实例化