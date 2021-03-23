# -*- -*- coding: utf-8 -*-  -*-  -*-
# @Author       : Gaopangpang
# @Project Name : MyStudy
# @File         : map_local
# @Time         : 2021/3/23 21:53
# @Email        : 719453296@qq.com
# -*- -*- -*- -*- -*- -*- -*- -*- -*-
"""Send a reply from the proxy without sending any data to the remote server."""
import json
from mitmproxy import http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def response(self, flow:http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:

        # 读取文件数据，作为响应返回
            with open("quote.json", encoding="utf-8") as f:
                data = json.load(f)
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]