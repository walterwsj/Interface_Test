import requests

from api_page.base_api import BaseApi
from api_page.wework_utils import WeworkUtils


class AddressPage(BaseApi):
    """
    Members CURD
    """

    def __init__(self):
        _corpSecret = 'zfl28QBqGpRaVvt8SdCvGqPkbbMLag7o_reI39Hh7jI'
        utils = WeworkUtils()
        self.token = utils.get_token(_corpSecret)

    def get_user(self):
        data = {
            "method": "get",
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/user/get?',
            "params": {
                "access_token": self.token,
                "userid": "cathy"
            }
        }
        return self.send_api(data)

    def create_user(self):
        data = {
            "method": "post",
            "url": f'https://qyapi.weixin.qq.com/cgi-bin/user/create?',
            "params":{
                "access_token":self.token
            },
            "json": {
                "userid": "makefoxrush1",
                "name": "令狐冲1",
                "alias": "fox",
                "mobile": "+8613812341235",
                "department": [2]
            }
        }
        return self.send_api(data)
