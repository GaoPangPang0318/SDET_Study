from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from study_selenium.Base import Base  #导入自己模块的方法

class TestAction(Base):
    def test_actionchains(self):
        self.driver.get("https://www.baidu.com/")

        action=ActionChains(self.driver)
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
        sleep(20)

        element_userlogin=self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn")
        element_userlogin.click()
        #action.click(element_userlogin).perform()

        element_userloginname = self.driver.find_element_by_id('TANGRAM__PSP_11__userName')
        element_userloginname.send_keys("孤寂づ白")

        element_userloginpassword = self.driver.find_element_by_id('TANGRAM__PSP_11__password')
        element_userloginpassword.send_keys("gjj19920318")

        element_loginbutton = self.driver.find_element_by_id('TANGRAM__PSP_11__submit')
        action.click(element_loginbutton).perform()

        sleep(30)



        #action.send_keys_to_element(element_username,"user").perform()  #使用这个方法报错无法正常输入值
        #action.send_keys(Keys.SPACE).perform()  # 报错内容: selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
        # action.send_keys("Tom").perform()




