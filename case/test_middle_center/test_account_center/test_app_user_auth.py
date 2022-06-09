#微淼-业务中台/账户中心/5.业务线用户角色维护
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

    # #业务线角色用户绑定
    # @pytest.mark.postAPI
    # def test_user_role_bind(self):
    #     Url = config.host + "/api/auth/metadata/user/role/bind"
    #     body = {
    #         "appId":"100",
    #         "uids":[11],
    #         "roleIds":[11]
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()['code'] == 0

    # #业务线角色用户解绑
    # @pytest.mark.postAPI
    # def test_user_role_unbind(self):
    #     Url = config.host + "/api/auth/metadata/user/role/unbind"
    #     body = {
    #         "appId": "100",
    #         "uid": 11
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()['code'] == 0

    #查询业务线用户
    @pytest.mark.getAPI
    def test_user_list(self):
        Url = config.host + "/api/auth/metadata/user/list?appId=%s" % ("100")
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #查询用户角色
    @pytest.mark.getAPI
    def test_user_role_list(self):
        data = mysql.mysqldb().fetch(col = 'app_id,uid',relation='',table='wm_authority_center.t_user_app')
        data = data['msg'][0]
        Url = config.host + "/api/auth/metadata/user/role/list?appId=%s&uid=%s" % (data[0], data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

#
if __name__=="__main__":
    pytest.main(["-s","test_app_user_auth.py"])