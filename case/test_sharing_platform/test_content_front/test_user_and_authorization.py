#coding:utf-8
#author by lianpengwei

import pytest
import requests
from config import config
from utils import login
from utils.mysql import mysqldb

mydb = mysqldb()


class TestUserAndAuthorization(object):

    def setup_class(self):
        token = login.sharing_platform_login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "laravel_session=" + token

    # 微信授权
    @pytest.mark.getAPI
    def test_wechat_auth(self):
        url = config.gxpt_fb_host + '/wechat/auth'
        res = requests.get(url, headers=self.header)
        assert res.status_code == 200

    # 个人中心 - 我的
    @pytest.mark.getAPI
    def test_user_my(self):
        url = config.gxpt_fb_host + '/user/my'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 是否关注"微淼实战训练营"
    @pytest.mark.getAPI
    def test_is_follow(self):
        url = config.gxpt_fb_host + '/is/follow'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 是否可参加活动
    @pytest.mark.getAPI
    def test_activit_can_join(self):
        url = config.gxpt_fb_host + '/activity/can/join'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_user_and_authorization.py'])