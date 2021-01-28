from study_appium_datadriven_sonwball.page.basepage import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"]=value
        self.steps("../page/search.yaml")