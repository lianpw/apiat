#coding:utf-8
#author by wangyunbao

import requests, json,pytest
from config import config
from utils import login,stamp

class TestAccount(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = "c_token="+token

    # #LDAP账户名称查询
    # @pytest.mark.postAPI
    # def test_search_user(self):
    #     Url = config.host+"/api/auth/account/search"
    #     body = {
    #         "name": config.user
    #     }
    #     res = requests.post(url=Url,data=json.dumps(body),headers=self.header)
    #     assert res.json()["code"] == 0
    #
    # #Token验证
    # @pytest.mark.postAPI
    # def test_token_verify(self):
    #     Url = config.host+"/api/auth/account/verify"
    #     body = {}
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    # #退出登陆--未完成
    # def test_logout(self):
    #     Url = config.host+"/api/auth/account/logout"
    #     body = {}
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0
    #
    # #创建账户
    # @pytest.mark.postAPI
    # def test_create_account(self):
    #     st = stamp.timeStamp()
    #     phone = stamp.phoneNum()
    #     Url = config.host+"/api/auth/account/create"
    #     body = {
    #         "name":"test"+st,
    #         "password":"123456",
    #         "chineseName":"ceshi",
    #         "employeeNumber":"",
    #         "mail":"",
    #         "phone":phone,
    #         "uid":"",
    #         "appId":"100",
    #         "roleIds":[1]
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    # #修改密码--未完成
    # def test_modify_passwd(self):
    #     Url = config.host + "/api/auth/account/modifyPassword"
    #     body = {
    #         "name": config.user,
    #         "password":config.passwd,
    #         "newPassword":config.passwd
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    # #根据员工编号获取员工信息
    # @pytest.mark.postAPI
    # def find_user(self):
    #     Url = config.host + "/api/auth/account/findUserByEmployeeNo"
    #     body = {
    #         "employeeNumber": "11",
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     return res.json()

    # #重置密码
    # @pytest.mark.postAPI
    # def test_reset_password(self):
    #     Url = config.host + "/api/auth/account/password/reset"
    #     body = {
    #         "name":config.user,
    #         "password":config.passwd
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     assert  res.json()["code"] == 0

    #更新账户信息
    # @pytest.mark.postAPI
    # def test_modify_account(self):
    #     user = TestAccount().find_user()
    #     Url = config.host + "/api/auth/account/modify"
    #     body = {
    #         "name": user["data"]["name"],
    #         "chineseName":user["data"]["realName"],
    #         "phone": "13800100501",
    #         "employeeNumber":user["data"]["employeeNumber"],
    #         "mail":user["data"]["mail"]
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    #批量查询账户信息
    # @pytest.mark.postAPI
    # def test_query_account(self):
    #     Url = config.host + "/api/auth/account/queryAccountByUserIds"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0
