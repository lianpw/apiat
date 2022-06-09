#coding:utf-8
#author by yangxi

import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
import random

class TestPC(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.mysqld = mysql.mysqldb()
        self.header["h-app-id"] = "114"
        self.header["Cookie"] = "c_token="+token


    #代理团队(备注：多选 代理公司团队)
    @pytest.mark.getAPI
    def test_agent_teamMultiple(self):
        parent_ids_count = mysqld.fetch(table="wm_infoflow.mh_agent", col="count('agent_num')" ,relation="level=1")["msg"][0][0]
        parent_ids = random.sample(range(parent_ids_count), 5)
        Url = config.analysis_host + "/api/agent/teamMultiple?parent_ids[]=%s&parent_ids[]=%s&parent_ids[]=%s&parent_ids[]=%s&parent_ids[]=%s"%(parent_ids[0],parent_ids[1],parent_ids[2],parent_ids[3],parent_ids[4])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    #账户管理列表
    @pytest.mark.getAPI
    def test_adManage_list(self):
        Url = config.analysis_host + "/api/adManage/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    #媒体名称
    @pytest.mark.getAPI
    def test_analysis_enum_queryMedias(self):
        Url = config.analysis_host + "/api/analysis/enum/queryMedias"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    #代理商列表
    @pytest.mark.getAPI
    def test_agent_list(self):
        Url = config.analysis_host + "/api/agent/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    #代理团队列表
    @pytest.mark.getAPI
    def test_team_list(self):
        Url = config.analysis_host + "/api/team/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

if __name__=="__main__":
     pytest.main(["-s","test_putManage_get.py"])