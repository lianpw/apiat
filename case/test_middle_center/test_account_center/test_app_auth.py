#coding:utf-8
#author by wangyunbao

import requests, json,pytest
from config import config
from utils import login,baseData

class TestRoleAuth(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    # #新增角色接口
    # @pytest.mark.postAPI
    # def role_add(self):
    #     Url = config.host + "/api/auth/metadata/role/add"
    #     body = {
    #         "appId":self.appid,
    #         "roleName": config.user,
    #         "roleType":1
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     return res.json()
    #
    # # #编辑角色接口
    # @pytest.mark.postAPI
    # def test_role_add(self):
    #     role_id= TestRoleAuth().role_add()['data']['id']
    #     Url = config.host + "/api/auth/metadata/role/add"
    #     body = {
    #         "appId":self.appid,
    #         "roleName":config.user,
    #         "id":role_id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    #删除角色接口--未完成
    # @pytest.mark.postAPI
    # def test_role_del(self):
    #     role_id= TestRoleAuth().role_add()['data']['id']
    #     Url = config.host + "/api/auth/metadata/role/delete"
    #     body = {
    #         "appId":self.appid,
    #         "id":role_id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     assert res.json()["code"] == 0

    # #角色权限绑定接口
    # @pytest.mark.postAPI
    # def test_role_del(self):
    #     role_id= TestRoleAuth().role_add()['data']['id']
    #     Url = config.host + "/api/auth/metadata/role/bind"
    #     body = {
    #         "appId":self.appid,
    #         "roleId":role_id,
    #         "premIds":[11]
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0
    #
    # #角色分页查询接口--未完成
    # # @pytest.mark.postAPI
    # # def test_role_list(self):
    # #     Url = config.host + "/api/auth/metadata/role/list"
    # #     body = {
    # #         "appId":self.appid
    # #     }
    # #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    # #     print(res.json())
    # #     assert res.json()["code"] == 0
    #
    #
    # #角色权限查询接口
    # @pytest.mark.postAPI
    # def test_role_permission(self):
    #     role_id = TestRoleAuth().role_add()['data']['id']
    #     Url = config.host + "/api/auth/metadata/role/permission"
    #     body = {
    #         "appId":self.appid,
    #         "roleId":role_id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     # assert res.json()["code"] == 0

if __name__=="__main__":
    pytest.main(["-s","test_app_auth.py"])
