from selenium import webdriver

class TestHogwards():
    def setup(self):   #测试用例初始前条件   Pytest  有setup和teardown
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

        #点击事件依赖CSS代码，因此当页面为加载好就无法正常定位，因此点击事件中间最好加上页面加载时间
        #比在测试用例中添加sleep（）更加好用
        self.driver.implicitly_wait(5)   #隐式等待只能查找到元素，无法判断元素类型，如果想判断元素得使用其他方法
        # 隐式等待，打开新界面会动态等待时间，如果未找到定位元素会一直等待，直到找到定位元素
        # 隐式等待属于全局变量

    def teardown(self): #测试用例结束后操作
        self.driver.quit()   #不添加的话，页面不会自动退出，影响资源回收

    def test_hogwards(self): #测试用例
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_css_selector("area").click()

        '''窗口切换'''
        #获取打开窗口的handle，返回list
        handle=self.driver.window_handles
        print("handle type:",type(handle),handle)
        self.driver.switch_to.window(handle[-1]) #切换到最后一个窗口

        self.driver.find_element_by_link_text("今日新鲜事搜索热点_百度搜索风云榜").click()


