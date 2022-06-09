#微淼-业务中台/账户中心/7.业务组织结构维护

import requests, pytest,json
from config import config
from utils import login,baseData,stamp,mysql

class TestOrganization(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    #获取应用所有组织结构节点
    @pytest.mark.getAPI
    def test_organization_get_list(self):
        data = mysql.mysqldb().fetch(col = 'app_id,uid',relation='',table='wm_authority_center.t_organizational_member')
        data = data['msg'][0]
        Url = config.host + "/api/auth/metadata/app/organization/list?appId=%s&uid=%s" % (data[0], data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #获取组织结构节点所有绑定用户
    @pytest.mark.getAPI
    def test_organization_account_list(self):
        data = mysql.mysqldb().fetch(col='app_id,parent_org_id,name',relation='', table='wm_authority_center.t_organizational_member', limitd=3)
        data = data['msg'][2]
        Url = config.host + "/api/auth/metadata/app/organization/list?appId=%s&parentOrgId=%s&name=%s" % (data[0], data[1], data[2])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0

    # #新增业务组织结构节点
    # def organization_add(self):
    #     Url = config.host + "/api/auth/metadata/app/organization/add"
    #     body = {
    #         "appId":self.appid,
    #         "name":"autotest"+stamp.timeStamp(),
    #         "level":1,
    #         "parentId":0,
    #         "uids":11
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body),headers=self.header)
    #     return res.json()
    #
    # # 修改业务组织结构节点
    # @pytest.mark.postAPI
    # def test_organization_edit(self):
    #     id = TestOrganization().organization_add()["data"]["id"]
    #     Url = config.host + "/api/auth/metadata/app/organization/edit"
    #     body = {
    #         "id":id,
    #         "appId": self.appid,
    #         "name": "autotest"+stamp.timeStamp(),
    #         "level": 1,
    #         "parentId": 0,
    #         "uids": 11
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()['code'] == 0 and res.json()['data']["id"] == id
    #
    # # 下线业务组织结构节点
    # @pytest.mark.postAPI
    # def test_organization_del(self):
    #     id = TestOrganization().organization_add()["data"]["id"]
    #     Url = config.host + "/api/auth/metadata/app/organization/del"
    #     body = {
    #         "id": id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()['code'] == 0 and res.json()['desc'] == "OK"
    #
    # # 业务组织结构节点用户绑定
    # @pytest.mark.postAPI
    # def organization_account_bind(self):
    #     data = TestOrganization().organization_add()["data"]
    #     Url = config.host + "/api/auth/metadata/app/organization/account/bind"
    #     body = {
    #         "appId":self.appid,
    #         "parentOrgId":data["id"],
    #         "level":1,
    #         "uid":11,
    #         "name":data["creater"]
    #     }
    #     res = requests.post(url=Url,data=json.dumps(body),headers = self.header)
    #     return res.json()
    #
    # #业务组织结构节点用户解除绑定
    # @pytest.mark.postAPI
    # def test_organization_account_unbind(self):
    #     id =  TestOrganization().organization_account_bind()["data"]["id"]
    #     print(id)
    #     Url = config.host + "/api/auth/metadata/app/organization/account/unbind"
    #     body = {
    #         "appId":self.appid,
    #         "id":id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0 and res.json()["desc"]=="OK"
    #


if __name__=="__main__":
    pytest.main(["-s","test_organization.py"])