#coding:utf-8
#author by wangyunbao

import requests, json,pytest
from config import config
from utils import login,baseData,mysql

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
    #         "appId":"100",
    #         "roleName": config.user,
    #         "roleType":1
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     return res.json()

    #编辑角色接口
    # @pytest.mark.postAPI
    # def test_role_add(self):
    #     role_id= TestRoleAuth().role_add()['data']['id']
    #     Url = config.host + "/api/auth/metadata/role/add"
    #     body = {
    #         "appId":"100",
    #         "roleName":config.user,
    #         "id":role_id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    #删除角色接口--未完成
    # def test_role_del(self):
    #     role_id= TestRoleAuth().role_add()['data']['id']
    #     Url = config.host + "/api/auth/metadata/role/delete"
    #     body = {
    #         "appId":"100",
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
    #         "appId":"100",
    #         "roleId":role_id,
    #         "premIds":[11]
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    #角色分页查询接口
    @pytest.mark.getAPI
    def test_role_list(self):
        Url = config.host + "/api/auth/metadata/role/list?appId=%s" % ("100")
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #角色权限查询接口
    @pytest.mark.getAPI
    def test_role_permission(self):
        data = mysql.mysqldb().fetch(col='app_id,id',relation='', table='wm_authority_center.t_role')
        data = data['msg'][0]
        Url = config.host + "/api/auth/metadata/role/permission?appId=%s&roleId=%s" % (data[0], data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #数据字典项查询接口--未完成
    # def test_dic_list(self):
    #     Url = config.host + "/api/auth/metadata/dic/list/1001"
    #     body = {}
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     assert res.json()["code"] == 0

if __name__=="__main__":
    pytest.main(["-s","test_role_auth.py"])