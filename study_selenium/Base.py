from  selenium import webdriver
import os
class Base():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)

        browser=os.getenv("browser")  #参数从哪儿来，怎么来呢？？？
        print("broswer",browser)
        if browser=="firefox":
            self.driver=webdriver.Firefox()
        elif browser =='headless':
            self.driver=webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome(options=option)
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
