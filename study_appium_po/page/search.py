from study_appium_po.page.basepage import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"]=value  #相当于修改类BasePage的类变量_parama={"value":value}
        self.steps("../page/search.yaml")