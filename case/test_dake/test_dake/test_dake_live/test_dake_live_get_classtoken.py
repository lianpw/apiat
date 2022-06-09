#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Testlive(object):
    def setup_class(self):
        self.mysqld =mysql.mysqldb()
        self.header = config.header
        self.header["Cookie"] = login.course_login()

    #用户信息
    @pytest.mark.getAPI
    def test_live_uesr_info(self):
        Url = config.dkzb_host + "/api/live-m/live/user/info"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取直播间信息
    @pytest.mark.getAPI
    def test_obtain_live_info(self):
        Url = config.dkzb_host_fro + "/api/live-m/live/room/info?room_id=%s" % (config.class_room_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取直播间回放列表
    @pytest.mark.getAPI
    def test_obtain_replay_list(self):
        Url = config.dkzb_host_fro + "/api/live-m/live/replay/list?room_id=%s" % (config.class_room_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取直播间回放详情
    @pytest.mark.getAPI
    def test_obtain_replay_info(self):
        liveroom_id = mysqld.fetch(table="wm_live_class.wl_live_room,wm_live_class.wl_live_room_replay", col="room_id,session_id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/live-m/live/replay/info?room_id=%s&session_id=%s" % (liveroom_id[0],liveroom_id[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000
    #
    #获取直播间当前上课状态
    @pytest.mark.getAPI
    def test_obtain_live_status(self):
        liveroom_id = mysqld.fetch(table="wm_live_class.wl_live_room", col="room_id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host_fro + "/api/live-m/live/room/status?room_id=%s" % (liveroom_id[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000 or res.json()["code"] == 130000

if __name__=="__main__":
     pytest.main(["-s","test_dake_live_get_classtoken.py"])
