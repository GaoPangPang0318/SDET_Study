from appium.webdriver.common.mobileby import MobileBy

from live_uiframework.pages.basepage import BasePage
from live_uiframework.pages.sign_page import SignPage


class WorkPage(BasePage):

    def goto_sign_page(self):
        # 滚动查找元素
        self.swip_click("打卡")
        return SignPage(self.driver)
