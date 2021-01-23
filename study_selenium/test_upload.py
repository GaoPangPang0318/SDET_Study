from study_selenium.Base import Base
from time import sleep

class TestUpload(Base):
    def testupload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()

        #如何使用相对路径呢？？？
        self.driver.find_element_by_id('stfile').send_keys('E:/Lagou/study_selenium/test.jpg')
        sleep(3)
