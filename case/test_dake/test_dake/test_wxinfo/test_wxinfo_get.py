#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class TestWXinfo(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    #模板消息查询
    @pytest.mark.getAPI
    def test_sms_info(self):
        sendid = mysqld.fetch(table="wm_sms_center.wm_template_202010", col="send_id", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_wxinfo + "/api/sms/tpl/info?send_id=%s" %(sendid)
        res = requests.get(url=Url, headers=self.header)
        # print("res:",res.json())
        assert res.json()["code"] == 0


    #短信息查询
    @pytest.mark.getAPI
    def test_sms_base_info(self):
        sendid = mysqld.fetch(table="wm_sms_center.wm_template_202010", col="send_id", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_wxinfo + "/api/sms/base/info?send_id=%s" %(sendid)
        res = requests.get(url=Url, headers=self.header)
        # print("res:",res.json())
        assert res.json()["code"] == 0


if __name__=="__main__":
     pytest.main(["-s","test_wxinfo_get.py"])