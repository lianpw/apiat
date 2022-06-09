
#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_Contract(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()



    # #注册个人用户(用户唯一标识&合同签署服务商类型)
    # @pytest.mark.postAPI
    # def test_user_personalReg(self):
    #     Url = config.sjy_host_contract + "/contract/personalReg"
    #     body = {
    #         "name": "请勿删除",
    #         "identity": "110102200201015920",
    #         "mobile": "18610316439",
    #         "account": "740975301564760064",
    #         "providerType": 1,
    #         "random": 1
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



if __name__=="__main__":
     pytest.main(["-s","test_contract_all.py"])