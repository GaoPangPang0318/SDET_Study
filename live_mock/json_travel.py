# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File         : json_travel
# @Time         : 2021/3/23 22:21
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
import json
import sys

from mitmproxy import http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" \
                in flow.request.pretty_url:
        # 打开文件，读取文件数据，作为响应，给返回
            data = json.loads(flow.response.text)
            flow.response.text = json.dumps(self.json_travel(data))


    def json_travel(self, data):
        """
        遍历响应数据，对不同类型的数据进行批量操作
        :param data: json格式数据
        :return: json格式数据
        """
        # 判断传入的数据类型{"a": {"b":{"c":1}}}
        if isinstance(data, dict):
            # 遍历字典的数据
            # 当字典格式，递归value值
            for key, value in data.items():
                data[key] = self.json_travel(value)

        elif isinstance(data, list):
            # 当数据类型 为 list 的时候， 添加到结构内，并继续递归遍历，
            # 当数据类型不为可迭代对象时停止遍历
            data = [self.json_travel(value) for value in data]

        #对不同的数据类型进行不同的操作
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, int) or isinstance(data, float):
            data = data * 2
        elif isinstance(data, str):
            data = data
        else:
            data = data
        return data

addons = [
    Counter()
]

