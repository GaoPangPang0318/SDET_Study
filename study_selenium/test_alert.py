from time import sleep

from selenium.webdriver import ActionChains

from study_selenium.Base import Base


class TestAlert(Base):
    def test_alert(self):
        #打开网址
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        #切换frame
        self.driver.switch_to.frame('iframeResult')

        #定位元素
        el_drag=self.driver.find_element_by_id('draggable')
        el_drop=self.driver.find_element_by_id('droppable')

        #定义actionchains动作
        action=ActionChains(self.driver)
        #进行拖拽操作
        action.drag_and_drop(el_drag,el_drop).perform()
        sleep(5)

        #切换到alert页面，并同意alert内容
        self.driver.switch_to.alert.accept()
        #alert的其他功能
        #self.driver.switch_to.alert.send_keys()  # - keysToSend: The text to be sent to Alert.
        #self.driver.switch_to.alert.dismiss()   #Dismisses the alert available.

        #切换至默认rframe
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(5)