from study_appium_datadriven_sonwball.page.app import App


class TestSearch:
    def test_search(self):
        App().setup().main().goto_market().goto_search().search("jd")