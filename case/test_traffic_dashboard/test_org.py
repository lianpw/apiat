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


    #获取组织架构
    @pytest.mark.getAPI
    def test_org_list(self):
        level = random.choice([2,3])
        Url = config.analysis_host + "/api/org/list?level=%s"%(level)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    #获取组织架构下用户
    @pytest.mark.getAPI
    def test_org_user_list(self):
        org_id = mysqld.fetch(table="wm_authority_center.t_organizational_member", col="parent_org_id",relation="level=3")
        Url = config.analysis_host + "/api/org/user/list?org_id=%s&level=3" %(org_id["msg"][0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    # #获取组织架构-用户权限
    # @pytest.mark.getAPI
    # def test_org_auth_list(self):
    #     level_num = random.choice([2,3])
    #     parent_id = mysqld.fetch(table="wm_authority_center.t_organizational_member", col="parent_org_id",
    #                              relation="level='level_num'-1")["msg"][0][0]
    #     if level_num == 2:
    #         Url = config.analysis_host + "/api/org/auth_list?level=%s" % (level_num)
    #     else:
    #         Url = config.analysis_host + "/api/org/auth_list?parent_id[]=%s&level=%s" % (parent_id, level_num)
    #
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 1000
    #
    # #获取组织架构下用户-用户权限
    # @pytest.mark.getAPI
    # def test_org_user_auth_list(self):
    #     org_id = mysqld.fetch(table="wm_authority_center.t_organizational_member", col="parent_org_id",
    #                           relation="level=3")
    #     Url = config.analysis_host + "/api/org/user/auth_list?org_id[]=%s" % (org_id)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 1000

if __name__=="__main__":
     pytest.main(["-s","test_org.py"])