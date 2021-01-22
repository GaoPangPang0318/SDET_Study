from  selenium import webdriver

class Base():
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
