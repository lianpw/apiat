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
product_no = mydb.fetch('wm_sharing_platform.article_sku', 'product_no', relation='')['msg'][0][0]


class TestContentManagement(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "c_token=" + token

    # 文章列表
    @pytest.mark.getAPI
    def test_article_list(self):
        url = config.gxpt_bk_host + '/admin/article/list'
        data = {
            'is_published': 1
        }
        res = requests.get(url, params=data, headers=self.header)
        assert res.json()['code'] == 0

    # 作者列表
    @pytest.mark.getAPI
    def test_authors(self):
        url = config.gxpt_bk_host + '/admin/authors'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 类目列表
    @pytest.mark.getAPI
    def test_article_categories(self):
        url = config.gxpt_bk_host + '/article/categories'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 文章详情
    @pytest.mark.getAPI
    def test_article_info(self):
        url = config.gxpt_bk_host + '/admin/article/info'
        data = {
            "product_no": product_no
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_content_management.py'])