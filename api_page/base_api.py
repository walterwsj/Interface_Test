import requests


class BaseApi:
    """
    API 的接口类
    """
    def send_api(self,data:dict):
        return requests.request(**data).json()