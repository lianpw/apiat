#coding:utf-8
#author by wangyunbao

import pytest,requests,json
from config import config
from utils import login,aes,getsign

class TestOrder():
    def setup_class(self):
        self.header = login.xby_login()
        self.header["Content-Type"]="application/json"

    @pytest.mark.getAPI
    def test_query_order_list(self):
        Url = config.xby_host+'/Admin/FinanceApi/queryOrderList'
        body={
            "mid":"21279",
            "app_key":"wm_class",
            "sign":getsign.sign(Mid=21279,Appkey='wm_class')
        }
        res = requests.get(url=Url,params=body)
        assert 0==res.json()["code"] or 2==res.json()["code"]

    @pytest.mark.getAPI
    def test_is_sign_up(self):
        Url = config.xby_host+'/Home/DkApi/isSignUp'
        body = '{"mid":"21279"}'
        res = requests.post(url=Url,data=aes.encrypt(body))
        assert 20000==aes.decrypt(res.text)['code']

if __name__ == '__main__':
	pytest.main(["-s", "test_user_order_list.py"])