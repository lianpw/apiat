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

    #筛选枚举
    @pytest.mark.getAPI
    def test_analysis_enum_all(self):
        Url = config.analysis_host + "/api/analysis/enum/all"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    # #广告账号下拉列表
    # @pytest.mark.getAPI
    # def test_account_listByInvestor(self):
    #     Url = config.analysis_host + "/api/account/listByInvestor?keyword=1&advertiser="
    #     res = requests.get(url=Url, headers = self.header)
    #     assert res.json()["code"] == 1000

    #投放计划下拉列表
    @pytest.mark.getAPI
    def test_plan_listByInvestor(self):
        advertiser_id = mysqld.fetch(table="wm_infoflow.mh_infoflow_advertising_plan", col="advertiser_id", relation="", limitd=1)
        keyword = mysqld.fetch(table="wm_infoflow.mh_infoflow_advertising_plan", col="ad_plan_name", relation="advertiser_id", limitd=1)["msg"][0]
        Url = config.analysis_host + "/api/account/listByInvestor?keyword=%s"%(keyword)
        res = requests.get(url=Url, headers = self.header)
        assert res.json()["code"] == 1000

    #投放创意下拉列表
    @pytest.mark.getAPI
    def test_plan_listByInvestor(self):
        creative_id = mysqld.fetch(table="wm_infoflow.traffic_statistics", col="creative_id", relation="", limitd=1)
        keyword = mysqld.fetch(table="wm_infoflow.traffic_statistics", col="advertiser_name", relation="creative_id", limitd=1)["msg"][0]
        Url = config.analysis_host + "/api/creative/listByInvestor?keyword=%s"%(keyword)
        res = requests.get(url=Url, headers = self.header)
        assert res.json()["code"] == 1000

    #自定义指标
    @pytest.mark.getAPI
    def test_analysis_columns(self):
        Url = config.analysis_host + "/api/analysis/columns"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000

    #投放素材下拉列表
    @pytest.mark.getAPI
    def test_analysis_enum_materials(self):
        material_id = stamp.randomNum(19)
        Url = config.analysis_host + "/api/analysis/enum/materials?material_id=%s"%(material_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 1000


if __name__=="__main__":
     pytest.main(["-s","test_dataAnalysis_get.py"])