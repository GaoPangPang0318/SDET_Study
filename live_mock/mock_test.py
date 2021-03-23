# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File         : mock_test
# @Time         : 2021/3/23 16:01
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import json

from mitmproxy import ctx
from mitmproxy import http


class Counter:
    def __init__(self):
        self.num = 0

    #注意：事件名称是固定明确的，必须按照要求写正确
    def request(self,flow:http.HTTPFlow):
        """
        请求下发需要的操作
        """
        self.num = self.num + 1

        #日志输出至终端显示
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        """
        响应时需要的操作
        """

        #判断是否存在我们想要的请求内容，存在的话就进行我们要向进行的操作
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            #修改响应的原始数据

            #获取响应数据的text，由于获取的text是str类型，所以需要对数据进行转换操作，转换成json类型
            data=json.loads(flow.response.text)

            #参照我们抓取的响应数据进行修改
            #使用jsonpath进行替换会更加简单方便
            data["data"]["items"][0]["quote"]["name"]="贵州茅台——高胖胖"

            #再把data数据从Jason格式转换成原来的格式，并赋值给响应信息
            flow.response.text=json.dumps(data)

addons = [
    Counter()
]
