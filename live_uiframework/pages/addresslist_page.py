"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/12 8:17 下午'
"""
from live_uiframework.pages.addcontact_page import AddContactPage
from live_uiframework.pages.basepage import BasePage




class AddressListPage(BasePage):
    def click_addcontact(self):
        # 点击添加成员
        self.parse_action("../pages/addresslist_page.yaml", "click_addcontact")
        return AddContactPage(self.driver)