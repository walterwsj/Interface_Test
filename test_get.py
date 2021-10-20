import requests

corpId = 'ww104361170cc6c31c'
corpSecret = 'zfl28QBqGpRaVvt8SdCvGqPkbbMLag7o_reI39Hh7jI'


def get_token():
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpId}&corpsecret={corpSecret}'
    response = requests.get(url).json()
    return response['access_token']


def test_get_user():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=cathy'
    res = requests.get(url).json()
    print(res)


def test_create_user():
    token = get_token()
    data = {
        "userid": "makefoxrush",
        "name": "令狐冲",
        "alias": "fox",
        "mobile": "+8613812341234",
        "department": [2]
    }
    url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}'
    res = requests.post(url, json=data).json()
    print(res)
