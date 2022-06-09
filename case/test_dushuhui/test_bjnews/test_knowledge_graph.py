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


class TestKnowledgeGraph(object):
    def setup_class(self):
        # self.token = login.dushuhui_login()
        self.header = config.header
        self.header["h-app-id"] = "111"

    # 理财知识图谱首页
    @pytest.mark.getAPI
    def test_WxBookTopic_index(self):
        url = config.dushuhui_bjnews_host + '/WxBookTopic/index'
        res = requests.get(url, headers=self.header)
        assert res.json()['statusCode'] == 200

    # 获取专题 书单列表
    @pytest.mark.getAPI
    def test_WxBookTopic_show(self):
        url = config.dushuhui_bjnews_host + '/WxBookTopic/show'
        res = requests.get(url, headers=self.header)
        assert res.json()['statusCode'] == 200

    # 书单详情
    @pytest.mark.getAPI
    def test_WxBookCollection_show(self):
        url = config.dushuhui_bjnews_host + '/WxBookCollection/show'
        collection_id = mydb.fetch('dushuhui.mh_dsh_wxbook_collection', 'id', relation='')['msg'][0][0]
        data = {
            'collection_id': collection_id
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['statusCode'] == 200


if __name__ == '__main__':
    pytest.main(['-s', 'test_knowledge_graph.py'])