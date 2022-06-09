#coding:utf-8
#author by lianpengwei
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
import pytest
import requests
from config import config
from utils import login


class TestBjnews(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        # self.header["Cookie"] = "c_token=" + token

    # 判断会员vip状态
    @pytest.mark.getAPI
    def test_manage_isVip(self):
        self.header["Cookie"] = login.dushuhui_h5_login()
        url = config.dushuhui_bk_host + '/api/manage/isVip'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == '200'

    # 购买会员订单滚动接口
    @pytest.mark.getAPI
    def test_manage_vipOrderReport(self):
        url = config.dushuhui_bk_host + '/api/manage/vipOrderReport'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == '200'


if __name__ == '__main__':
    pytest.main(['-s', 'test_bjnews.py'])