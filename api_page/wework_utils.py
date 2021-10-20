import requests

from api_page.base_api import BaseApi


class WeworkUtils(BaseApi):
    def get_token(self, corpSecret, corpId='ww104361170cc6c31c'):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            "params": {
                "corpid": corpId,
                "corpsecret": corpSecret
            }
        }
        response = self.send_api(data)
        return response['access_token']
