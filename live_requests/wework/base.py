import requests


class Base:
    def __init__(self):
        self.s = requests.Session()  #声明一个request是的seesion
        self.token = self.get_token()  #初始化，获取token值
        self.s.params = {"access_token": self.token} #将获取的token值给这个Session对象的params，后续使用测不需要反复调用get_token，提高测试速度

    def send(self, *args, **kwargs):  #TCP层面的：scoket、串口、网口
        return self.s.request(*args, **kwargs)

    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe653983e4c732493&corpsecret=T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc')
        token = r.json()['access_token']
        return token
