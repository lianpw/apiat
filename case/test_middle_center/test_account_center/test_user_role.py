#coding:utf-8
#author by wangyunbao

import requests, json,pytest
from config import config
from utils import login,baseData

class TestUserAuth(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    # #获取用户在业务线业务权限
    # @pytest.mark.postAPI
    # def test_account_permission_function(self):
    #     Url = config.host + "/api/auth/account/permission/function"
    #     body = {
    #         "appId":self.appid
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0
    #
    # # 获取用户在业务线的数据权限
    # @pytest.mark.postAPI
    # def test_account_permission_data(self):
    #     Url = config.host + "/api/auth/account/permission/data"
    #     body = {
    #         "appId":self.appid
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0
    #
    # #获取用户是否有权限访问该资源
    # @pytest.mark.postAPI
    # def test_account_permission_has(self):
    #     Url = config.host + "/api/auth/account/permission/has"
    #     body = {
    #         "resId":self.appid
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0 or res.json()["code"] == 100607
    #
    # # 获取用户授权的业务线
    # @pytest.mark.postAPI
    # def test_account_app_list(self):
    #     Url = config.host + "/api/auth/account/app/list"
    #     body = {
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

# if __name__ == "__main__":
#     pytest.main(["-s", "test_user_role.py"])