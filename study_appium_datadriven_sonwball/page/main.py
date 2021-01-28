from asyncio import sleep

from study_appium_datadriven_sonwball.page.basepage import BasePage
from study_appium_datadriven_sonwball.page.market import Market



class Main(BasePage):
    def goto_market(self):
        #使用steps函数，
        self.steps("../page/main.yaml")
        return Market(self._driver)