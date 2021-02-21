from study_requests import apienv


class TestApiEnv:
    data = {
        "method": "get",
        "url": "http://gao_pang_pang:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        ar = apienv.ApiEnv()
        print(ar.send(self.data).text)
