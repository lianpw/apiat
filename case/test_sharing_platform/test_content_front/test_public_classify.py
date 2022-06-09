#coding:utf-8
#author by lianpengwei

import pytest
import requests
from config import config
from utils import login


class TestPublicClassify(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "c_token=" + token

    # banner
    @pytest.mark.getAPI
    def test_banner(self):
        url = config.gxpt_fb_host + '/banner'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 获取微信jssdk配置
    @pytest.mark.getAPI
    def test_wechat_jssdk_config(self):
        url = config.gxpt_fb_host + '/wechat/jssdk/config'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_public_classify.py'])