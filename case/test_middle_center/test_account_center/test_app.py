#微淼-业务中台/账户中心/6.业务线维护
import requests, pytest
from config import config
from utils import login,baseData

class TestAPP(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    #获取所有应用业务线
    @pytest.mark.getAPI
    def test_metadata_get_list(self):
        Url = config.host + "/api/auth/metadata/app/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0

    # #新增业务线
    # @pytest.mark.postAPI
    # def metadata_app_add(self):
    #     Url = config.host + "/api/auth/metadata/app/add"
    #     body = {
    #         "name":"auto_test_app",
    #         "homeUrl":"http://www.baidu.com",
    #         "remark":"auto test app",
    #         "type":1,
    #         "iconUlr":"http://www.baidu.com",
    #         "appID":"101"
    #     }
    #     res = requests.post(url=Url,data=body,headers= self.header)
    #     return res.json()
    #
    # # 更新业务线
    # @pytest.mark.postAPI
    # def test_metadata_app_edit(self):
    #     id = TestAPP().metadata_app_add["data"]["id"]
    #     Url = config.host + "/api/auth/metadata/app/edit"
    #     body = {
    #         "id":id,
    #         "name": "auto_test_app",
    #         "homeUrl": "http://www.baidu.com",
    #         "remark": "auto test app"
    #     }
    #     res = requests.post(url=Url, data=body, headers=self.header)
    #     assert res.json()["code"] == 0

if __name__=="__main__":
     pytest.main(["-s","test_app.py"])