import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list=[]
    _error_count=0
    _error_max=10
    _params={}
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    def find(self,by,locator:None):
        try:
            # find_elements 和 find_element的却别?
            # find_elements 返回匹配元素的list  ； find_element返回匹配的元素
            el=self._driver.find_elements(*by) if isinstance(by,tuple) else self._driver.find_elements(by,locator)
            self._error_count=0
            return el   #返回找到的element
        except Exception as e:
            self._error_count =+1
            if self._error_count>=self._error_count:
                raise  e
            for black in self._black_list:
                b_els=self._driver.find_elements(*black)
                if len(b_els)>0:
                    b_els[0].click()
                    return self.find(by,locator)
            raise e

    def send(self,value,by,locator=None):
        try:
            self.find(by,locator).send_keys(value)
        except Exception as e:
            self._error_count =+1
            if self._error_count>=self._error_count:
                raise  e
            for black in self._black_list:
                b_els=self._driver.find_elements(*black)
                if len(b_els)>0:
                    b_els[0].click()
                    return self.find(by,locator)
            raise e
    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps:list[dict]=yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    element=self.find(step['by'],step['locator'])
                if 'action' in step.keys():
                    if 'click' ==step['action']:
                        element.click()
                    if 'send' ==step['action']:
                        content:str=step['value']
                        for param in self._params:
                            content=content.replace("{%s}"%param,self._params[param])
                        self.send(content,step['by'],step['locator'])




