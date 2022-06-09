#coding:utf-8
#author by lianpengwei
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
import pytest
import requests
from config import config
from utils import login


class TestPersonalCenter(object):
    def setup_class(self):
        # self.token = login.dushuhui_login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        # self.header["Cookie"] = "c_token=" + token

    # 购买会员订单滚动接口
    @pytest.mark.getAPI
    def test_MemberManage_vipOrderReport(self):
        url = config.dushuhui_bjnews_host + '/MemberManage/vipOrderReport'
        data = {
            "page": 1,
            "page_size": 1
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['statusCode'] == '200'


if __name__ == '__main__':
    pytest.main(['-s', 'test_personal_center.py'])
