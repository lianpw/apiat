#coding:utf-8
#author by yinjiangbing
import pytest,requests,json
from config import config
from utils import login,baseData,mysql
mysqld = mysql.mysqldb()

import json
class TestWXinfo(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.appid = '102'
        self.header["h-app-id"] = self.appid

    @pytest.mark.getAPI
    def test_backend_sms_comboboxdata(self):
        Url = config.sjy_host_wxinfo + "/api/backend/sms/tpl/combo_box_data"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #签名列表
    @pytest.mark.getAPI
    def test_backend_sms_signlist(self):
        Url = config.sjy_host_wxinfo + "/api/backend/sms/sign/pagelist?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #业务方列表
    @pytest.mark.getAPI
    def test_backend_sms_businesslist(self):
        Url = config.sjy_host_wxinfo + "/api/backend/sms/business/pagelist?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #供应商列表
    @pytest.mark.getAPI
    def test_backend_sms_supplierlist(self):
        Url = config.sjy_host_wxinfo + "/api/backend/sms/supplier/pagelist?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #短信模板详情
    @pytest.mark.getAPI
    def test_backend_sms_tplinfo(self):
        tp_id = mysqld.fetch(table="wm_sms_center.wm_sms_tpl", col="id", relation="", limitd=1)["msg"][0]
        Url = config.sjy_host_wxinfo + "/api/backend/sms/tpl/info?tpl_id=%s" %(tp_id[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0

if __name__=="__main__":
     pytest.main(["-s","test_wxinfo_get_ctoken.py"])