#coding:utf-8
#author by lianpengwei
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
import pytest
import requests
from config import config
from utils import login
from utils.mysql import mysqldb

mydb = mysqldb()


class TestTagManagement(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "c_token=" + token

    # 标签列表
    @pytest.mark.getAPI
    def test_tag_list(self):
        url = config.gxpt_bk_host + '/admin/tag/list'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 标签详情
    @pytest.mark.getAPI
    def test_tag_info(self):
        url = config.gxpt_bk_host + '/admin/tag/info'
        id = mydb.exeSQL('select id from wm_sharing_platform.tags where deleted_at is null limit 1')['msg'][0][0]
        print(id)
        data = {
            "id": id
        }
        res = requests.get(url, params=data, headers=self.header)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_tag_management.py'])