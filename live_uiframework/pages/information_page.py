from live_uiframework.pages.addresslist_page import AddressListPage
from live_uiframework.pages.basepage import BasePage
from live_uiframework.pages.work_page import WorkPage





class InformationPage(BasePage):
    def goto_work_page(self):
        # self.find_click("//*[@text='工作台']")
        self.parse_action("../pages/information_page.yaml", "goto_work_page")
        return WorkPage(self.driver)

    def goto_addresslist(self):
        # 进入到通讯录
        self.parse_action("../pages/information_page.yaml", "goto_addresslist")
        return AddressListPage(self.driver)