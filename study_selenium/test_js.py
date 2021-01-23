from study_selenium.Base import Base
import time
import pytest

class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")

        #定位搜索框，传入搜索内容
        self.driver.find_element_by_id("kw").send_keys("selenium")

        #使用JS定位搜索按钮，点击搜索
        ele_search=self.driver.execute_script('return document.getElementById("su")')
        ele_search.click()

        #将搜索页面滑动至最下方
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(3)

        #点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        time.sleep(3)
        #这样做至打印出前面一条命令返回值
        # for code in {
        #     'return document.title','return JSON.stringify(performance.timing)'
        # }:
        #   print(self.driver.execute_script(code))
        print(self.driver.execute_script('return document.title'))
        print(self.driver.execute_script('return JSON.stringify(performance.timing)'))

    def test_js_datetime(self):
        #打开网址
        self.driver.get('https://www.12306.cn/')
        time.sleep(10)

        #定位时间元素；进行readonly属性去除操作；赋值新日期
        #注意：可以合并执行JS方法的写法
        #self.driver.execute_script('document.getElementById("train_date");document.getElementById("train_date").removeAttribute("readonly")')
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="2021-1-20"')
        time.sleep(10)

"""
JS:课后扩展学习相关JS的命令
"""