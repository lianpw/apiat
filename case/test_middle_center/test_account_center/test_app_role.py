#微淼-业务中台/账户中心/3.业务线权限维护
#coding:utf-8
#author by wangyunbao

import requests, pytest,json
from config import config
from utils import login,baseData

class TestUserAuth(object):


    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    # 新增权限接口
    # @pytest.mark.postAPI
    # def test_metadata_right_add(self):
    #     Url = config.host+"/api/auth/metadata/right/add"
    #     body = {
    #         "appId":self.appid,
    #         "resName":config.user,
    #         "resType":0,
    #         "parentId":11,
    #         "permFlag":"1",
    #         "routeName":"1"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    #编辑权限接口--未完成
    # @pytest.mark.postAPI
    # def test_metadata_right_update(self):
    #     Url = config.host + "/api/auth/metadata/right/update"
    #     body = {
    #         "appId":self.appid,
    #         "resName":config.user,
    #         "resType":0,
    #         "parentId":11,
    #         "permFlag":"1",
    #         "routeName":"1",
    #         "id":1
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     # assert res.json()["code"] == 0

    #删除权限接口--未完成
    # @pytest.mark.postAPI
    # def test_metadata_right_delete(self):
    #     Url = config.host + "/api/auth/metadata/right/delete"
    #     body = {
    #         "appId": self.appid,
    #         "id": 281
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     # assert res.json()["code"] == 0

    #查询权限列表
    @pytest.mark.getAPI
    def test_metadata_right_list(self):
        Url = config.host + "/api/auth/metadata/right/list?appId=%s" % ("100")
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #查询父ID下一级节点--未完成
    # @pytest.mark.postAPI
    # def test_metadata_right_parent(self):
    #     Url = config.host + "/api/auth/metadata/right/parent"
    #     body = {
    #         "appId": self.appid,
    #         "resId":1
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print(res.json())
    #     # assert res.json()["code"] == 0
