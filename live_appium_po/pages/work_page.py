
from live_appium_po.pages.basepage import BasePage
from live_appium_po.pages.sign_page import SignPage


class WorkPage(BasePage):

    def goto_sign_page(self):
        # 滚动查找元素
        self.swip_click("打卡")
        return SignPage(self.driver)
