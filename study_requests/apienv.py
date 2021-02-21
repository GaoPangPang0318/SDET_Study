"""
阶段十：接口测试框架——阶段十：接口测试框架
    原理：在请求之前对url进行替换
    1.需要二次封装requests，对请求进行定制化
    2.将请求的结构体的url从一个写死的IP地址改成一个（任意的）域名
    3.使用一个env配置文件，存放各个环境的配置信息
    4.然后将请求结构体中的url替换为‘env’配置文件中个人选择的url
    5.将env配置文件使用yaml进行管理
"""
import requests
import yaml


class ApiEnv:
    # data={
    #     "method":"get",
    #     "url":"http://gao_pang_pang:9999/demo.txt",
    #     "headers":None,
    #     "encoding":"base64"
    # }

    #3中的env配置
    # env={
    #     "dev":"127.0.0.1",
    #     "test":"127.0.0.2"
    # }

    #4中的env配置
    # env={
    #     "default":"dev",
    #     "gao_pang_pang":{
    #         "dev": "127.0.0.1",
    #         "test": "127.0.0.2"
    #     }
    # }

    #将env配置文件使用yaml进行管理
    env=yaml.safe_load(open("env.yaml"))

    def send(self,data:dict):
        #2.将请求的结构体的url从一个写死的IP地址改成一个（任意的）域名
        #data["url"]=str(data["url"]).replace("gao_pang_pang","127.0.0.1")

        #3.使用一个env配置文件，存放各个环境的配置信息
        #data["url"] = str(data["url"]).replace("gao_pang_pang", self.env["dev"])

        #4.将请求结构体中的url替换为‘env’配置文件中个人选择的url
        data["url"] = str(data["url"]).replace("gao_pang_pang", self.env["gao_pang_pang"][self.env["default"]])

        #1.对requests进行第二次封装
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        return res