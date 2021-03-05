from study_appium_po.page.basepage import BasePage
from study_appium_po.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)