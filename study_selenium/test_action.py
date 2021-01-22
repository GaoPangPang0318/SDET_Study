from time import sleep

import pytest
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys

from study_selenium.Base import Base  #导入自己模块的方法

class TestAction(Base):

    @pytest.mark.skip
    def test_actionchains(self):
        """
            联系一下以下内容：
            1.窗口切换
            2.ActionChains操作  click  movetoelement   sendtokeys(不好用，总是报错，我看不出原因)
            3.表单
        """
        self.driver.get("https://www.baidu.com/")

        action=ActionChains(self.driver)

        element_set=self.driver.find_element_by_id('s-usersetting-top')
        action.move_to_element(element_set).perform()
        sleep(5)


        element_login =self.driver.find_element_by_link_text("登录")
        action.click(element_login).perform() #点击百度“登录”
        # 立即执行action.click(element_login)
        # 注意：当操作后有新窗口或者浮层出现的话，不能吧所有操作做完之后一起preform  这样会导致窗口无法正常弹出，影响下一个步骤的元素查找

        element_register = self.driver.find_element_by_link_text("立即注册")
        action.click(element_register).perform() # 点击“立即注册”
        #会有新窗口呈现 因此立即perform

        windowsall=self.driver.window_handles #获取所有窗口句柄
        print(windowsall)
        self.driver.switch_to.window(windowsall[-1])  #切换到注册窗口，即最后一个打开的窗口


        element_username = self.driver.find_element_by_id('TANGRAM__PSP_4__userName')
        element_username.send_keys("username")

        self.driver.switch_to.window(windowsall[0])

        element_userlogin=self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn")
        element_userlogin.click()
        #action.click(element_userlogin).perform()

        element_userloginname = self.driver.find_element_by_id('TANGRAM__PSP_11__userName')
        element_userloginname.send_keys("孤寂づ白")

        element_userloginpassword = self.driver.find_element_by_id('TANGRAM__PSP_11__password')
        element_userloginpassword.send_keys("gjj19920318")

        element_loginbutton = self.driver.find_element_by_id('TANGRAM__PSP_11__submit')
        action.click(element_loginbutton).perform()

        sleep(5)

        #action.send_keys_to_element(element_username,"user").perform()  #使用这个方法报错无法正常输入值
        #action.send_keys(Keys.SPACE).perform()  # 报错内容: selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
        # action.send_keys("Tom").perform()

    def test_touchactions(self):
        """
            联系以下内容：
            1.TouchActions： scroll_from_element  tap操作
        """
        self.driver.get("http://www.baidu.com/")

        el_input=self.driver.find_element_by_id('kw')
        el_search=self.driver.find_element_by_id('su')
        #两个元素在同一个界面上，因此可以先找

        el_input.send_keys("selenium")
        sleep(5)
        action=TouchActions(self.driver)
        action.tap(el_search)
        action.perform() #不要忘记触发执行   Taps on a given element.
        action.scroll_from_element(el_search,0,10000).perform()
        """
        :Args:
         - on_element: The element where scroll starts.
         - xoffset: X offset to scroll to.
         - yoffset: Y offset to scroll to.
        """

    #还可以联系拖拽：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable











