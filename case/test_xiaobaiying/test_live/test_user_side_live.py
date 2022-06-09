#微淼-小白营/直播项目/C端
import requests,pytest
from config import config
from utils import login,baseData


class TestLive(object):
    url = 'https%3a%2f%2fwww.baidu.com1'
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = 'mid=10006787'

    #获取当前登录用户信息
    @pytest.mark.getAPI
    def test_get_UserInfo(self):
        Url = config.xby_host + "/Live/Api/getPayConfig"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 100000

    #获取支付参数
    @pytest.mark.getAPI
    def test_get_PayConfig(self):
        Url = config.xby_host + "/Live/Api/getPayConfig"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 100000

    # 获取微信jssdk数据
    @pytest.mark.getAPI
    def test_get_WxSignPackage(self):
        Url = config.xby_host + "/Live/Api/getWxSignPackage?url=%s" % (self.url)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 100000

    #获取回放信息
    @pytest.mark.getAPI
    def test_get_PlaybackList(self):
        Url = config.xby_host + "/Live/Api/getPlaybackList?room_id=%s" % (config.room_id)
        res = requests.get(url=Url,headers=self.header)
        assert res.json()['code'] == 100000

    #获取直播间签名
    @pytest.mark.getAPI
    def test_get_Sign(self):
        Url = config.xby_host + "/Live/Api/getSign?room_id=%s" % (config.room_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 100000

    #获取直播教室当前上课状态
    @pytest.mark.getAPI
    def test_get_liveStatus(self):
        Url = config.xby_host + "/index.php/Live/Api/liveStatus?room_id=%s" % (config.room_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 100000



if __name__=="__main__":
    pytest.main(["-s", "test_user_side_live.py"])