#coding:utf-8
#author by wangyunbao

import pytest,requests,json
from config import config
from utils import login,aes,getsign

class TestLiving():
    def setup_class(self):
        self.header= {}
        self.header["Content-Type"]="application/json"
        self.header["Cookie"]="userid=1585597; mid=21279"
        self.header["PHPSESSID"]="1o4lak7pn353q1o59hbu1ml20k"

    # @pytest.mark.getAPI
    # def test_getUserInfo(self):
    #     Url = config.xby_host+'/Live/Api/getUserInfo'
    #     res = requests.get(url=Url,headers=self.header)
    #     print(res.json())
    #     assert 100000==res.json()['code']

    # @pytest.mark.getAPI
    # def test_WxpayBefore(self):
    #     Url = config.xby_host + '/Live/Api/WxpayBefore'
    #     body={
    #         "mid":"21279",
    #         "num":"1"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert 100000 == res.json()['code']

    @pytest.mark.getAPI
    def test_getPayConfig(self):
        Url = config.xby_host + '/Live/Api/getPayConfig'
        res = requests.get(url=Url,headers=self.header)
        assert 100000 == res.json()['code']

    @pytest.mark.getAPI
    def test_getWxSignPackage(self):
        Url = config.xby_host + '/Live/Api/getWxSignPackage'
        body= {"url":"https%3a%2f%2fwww.baidu.com1"}
        res = requests.get(url=Url, params=body,headers=self.header)
        assert 100000 == res.json()['code']

    @pytest.mark.getAPI
    def test_getPlaybackList(self):
        Url = config.xby_host + '/Live/Api/getPlaybackList'
        body = {"room_id": "20072494277283"}
        res = requests.get(url=Url, params=body, headers=self.header)
        assert 100000 == res.json()['code']

    @pytest.mark.getAPI
    def test_getSign(self):
        Url = config.xby_host + '/Live/Api/getSign'
        body = {"room_id": "20072494277283"}
        res = requests.get(url=Url, params=body, headers=self.header)
        assert 100000 == res.json()['code']

    @pytest.mark.getAPI
    def test_liveStatus(self):
        Url = config.xby_host + '/index.php/Live/Api/liveStatus'
        body = {"room_id": "20072494277283"}
        res = requests.get(url=Url, params=body, headers=self.header)
        assert 100002 == res.json()['code']


if __name__ == '__main__':
	pytest.main(["-s", "test_living.py"])