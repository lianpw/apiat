#coding:utf-8
#author by wangyunbao

import pytest,requests
from utils import login

class TestDing():
    def setup_class(self):
        self.header = login.xby_login()
        self.header["Content-Type"]="application/json"

    #获取天津钉钉access token
    @pytest.mark.getAPI
    def test_dingtalk_token(self):
        Url = 'http://ad.weimiaocaishang.com/dingtalk/token'
        body={"type":1}
        res = requests.get(url=Url,params=body,headers=self.header)
        assert 1000==res.json()['code']

if __name__ == '__main__':
	pytest.main(["-s", "test_get_ding.py"])