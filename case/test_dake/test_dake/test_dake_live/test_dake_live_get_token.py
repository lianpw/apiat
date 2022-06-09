#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,mysql,baseData

mysqld = mysql.mysqldb()

import json
class Testlive(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.appid = baseData.account_app_list()["data"][0]["appID"]
        self.header["h-app-id"] = self.appid


    # # #母班列表进入助教端(待开发重新提测)
    # @pytest.mark.getAPI
    # def test_motherclass_into_zhujiao(self):
    #     motherclass_id = mysqld.fetch(table="wm_live_class.wl_mother_class_teacher", col="mother_class_id", relation="", limitd=1)["msg"][0][0]
    #     Url = config.dkzb_host + "/api/advanced-backend/live/mother/live/info?m_class_id=%s" % (motherclass_id)
    #     print("url:",Url)
    #     res = requests.get(url=Url, headers=self.header)
    #     print("res1:", res.json())
    #     assert res.json()["code"] == 100000

    # # #回放列表
    @pytest.mark.getAPI
    def test_replay_list(self):
        replayroom_id = mysqld.fetch(table="wm_live_class.wl_live_room_replay", col="live_room_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/room/replay/list?room_id=%s" % (replayroom_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

if __name__=="__main__":
     pytest.main(["-s","test_dake_live_get_token.py"])