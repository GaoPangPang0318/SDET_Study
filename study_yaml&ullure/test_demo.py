import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yaml"))) #参数使用list格式传入，如果是dict只能传入key
    def test_demo(self,env):
        if 'test' in env:
            print("这个是一个测试环境")
            print(env)
        elif "dev" in env:
            print("这是一个开发环境")

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))