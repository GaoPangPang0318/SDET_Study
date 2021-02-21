import yaml
"""
多环境那节课中用到的
dict 转换成yaml 以免手动建立出错
"""

def test_dictoyaml():
    env = {
        "default": "dev",
        "gao_pang_pang": {
            "dev": "127.0.0.1",
            "test": "127.0.0.2"
        }
    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)