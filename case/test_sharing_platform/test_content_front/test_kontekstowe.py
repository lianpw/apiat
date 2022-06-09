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

token1 = login.login()
class TestKontekstowe(object):

    def setup_class(self):
        token = login.sharing_platform_login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "laravel_session=" + token


    # 最近更新
    @pytest.mark.getAPI
    def test_recent(self):
        url = config.gxpt_fb_host + '/recent'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 精选推荐
    @pytest.mark.getAPI
    def test_recommends(self):
        url = config.gxpt_fb_host + '/recommends'
        data = {
            'page': 1,
            'size': 1
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0

    # 文章列表
    @pytest.mark.getAPI
    def test_articles(self):
        url = config.gxpt_fb_host + '/articles'
        data = {
            'page': 1,
            'size': 1,
            'category_id': 4
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0

    # 文章详情
    @pytest.mark.getAPI
    def test_article_get(self):
        url = config.gxpt_fb_host + '/article/get'
        cate_id = mydb.fetch('wm_product_center.wp_category', 'id', conditions={'category_name': '企业分析'}, limitd=1)['msg'][0][0]
        product_no = mydb.fetch('wm_product_center.wp_product', 'product_num', relation='and', conditions={'status': 1, 'category_id':cate_id}, limitd=10)['msg'][9][0]
        data = {
            'product_no': product_no
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0

    # 免费工具
    @pytest.mark.getAPI
    def test_tools_list(self):
        url = config.gxpt_fb_host + '/tools/list'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 判断是否订阅
    @pytest.mark.getAPI
    def test_category_is_subscribe(self):
        url = config.gxpt_fb_host + '/category/is/subscribe'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 企业资讯订阅数
    @pytest.mark.getAPI
    def test_enterprice_info(self):
        url = config.gxpt_fb_host + '/enterprice/info'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 获取key
    @staticmethod
    def get_key():
        header = {}
        header["Cookie"] = "c_token=" + token1
        url = config.gxpt_bk_host + '/admin/article/preview/save'
        data = {
            'title': '预览测试-001',
            'content': '预览测试'
        }
        res = requests.post(url, json=data, headers=header)
        return res.json()['data']['key']

    # 预览文章
    @pytest.mark.getAPI
    def test_article_preview(self):
        url = config.gxpt_fb_host + '/article/preview'
        data = {
            'key': self.get_key()
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_kontekstowe.py'])