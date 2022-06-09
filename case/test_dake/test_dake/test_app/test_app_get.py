#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class TestPC(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    #用户合同详情
    @pytest.mark.getAPI
    def test_Contracts_info(self):
        Url = config.sjy_host_loign + "/api/Contracts/getContractInfo"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #合同列表
    @pytest.mark.getAPI
    def test_Contracts_list(self):
        Url = config.sjy_host_loign + "/api/Contracts/getContractLIst"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # #上传签名
    # @pytest.mark.getAPI
    # def test_Contracts_list(self):
    #     Url = config.sjy_host + "/api/Contracts/uploadContractSign?file="
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 0



if __name__=="__main__":
     pytest.main(["-s","test_app_get.py"])