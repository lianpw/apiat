#coding:utf-8
#author by lianpengwei
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
import pytest
import requests
from config import config
from utils import login


class TestFreeTools(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "c_token=" + token

    # 免费工具列表
    @pytest.mark.getAPI
    def test_tools_optionList(self):
        url = config.gxpt_bk_host + '/admin/tools/optionList'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 获取免费工具列表
    @pytest.mark.getAPI
    def test_tools_list(self):
        url = config.gxpt_bk_host + '/admin/tools/list'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_free_tools.py'])