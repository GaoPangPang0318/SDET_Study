from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://ceshiren.com')
        #self.driver.implicitly_wait(3)  #第二种wait：隐式等待

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@id="ember41"]/a').click()
        #sleep(3)   #第一种wait：直接等待
        #自定义等待函数
        # def wait():
        #     return len(self.driver.find_elements(By.XPATH,'//*[@id="ember411"]/div[1]'))>=1
        #selenium自带等待函数
        WebDriverWait(self.driver,50).until( expected_conditions.invisibility_of_element_located((By.XPATH,'//*[@id="ember427"]/div[1]')))  #第三种方法：显示等待
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
