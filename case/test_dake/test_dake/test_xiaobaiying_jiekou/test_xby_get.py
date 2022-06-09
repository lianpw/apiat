#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Testxby(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    #获取预选班通知消息
    @pytest.mark.getAPI
    def test_class_splitNotice(self):
        Url = config.sjy_host_pc + "/class/splitNotice"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 200


    #预选星期
    @pytest.mark.getAPI
    def test_class_prepareWeek(self):
        Url = config.sjy_host_pc + "/class/prepareWeek"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 200


    #获取用户订单详情
    @pytest.mark.getAPI
    def test_class_splitNotice(self):
        Url = config.sjy_host_pc + "/userManage/getUserFullInfo?id=10001727"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #批量获取学员开课信息接口
    @pytest.mark.getAPI
    def test_queryUsers_Kind(self):
        Url = config.sjy_host_pc + "/userManage/queryUsersKind?mids=10001727"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0



if __name__=="__main__":
     pytest.main(["-s","test_xby_get.py"])