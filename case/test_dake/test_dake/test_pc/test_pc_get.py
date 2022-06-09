#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class TestPC(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    #地级市联动
    @pytest.mark.getAPI
    def test_user_getRegion_pc(self):
        Url = config.sjy_host_pc + "/api/user/getRegion"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000 or res.json()["code"] == 10034


    #视频列表
    @pytest.mark.getAPI
    def test_video_list_pc(self):
        Url = config.sjy_host_pc + "/api/video/getVideoList?level=1&userId=1603940717807987&status=2&version=4&pid=4"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #章节试题列表
    @pytest.mark.getAPI
    def test_Chapter_list_pc(self):
        Url = config.sjy_host_pc + "/api/chapter/getChapterList?categoryId=1&userId=1603940717807987&version=4"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000\


    #视频小结测试
    @pytest.mark.getAPI
    def test_QuestionInfo_pc(self):
        Url = config.sjy_host_pc + "/api/video/getQuestionInfo?vid=1&version=4&userId=1603940717807987&pid=4"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #根据金额获取商品信息
    @pytest.mark.getAPI
    def test_checkPrice_pc(self):
        Url = config.sjy_host_pc + "/api/payment/checkPrice?price=2998"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #检测订单
    @pytest.mark.getAPI
    def test_checkOrder_pc(self):
        order_No = mysqld.fetch(table="wm_class.wm_order", col="ordernum", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_pc + "/api/payment/checkOrder?tradeNo=%s" %(order_No)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #用户中心当前视频地址
    @pytest.mark.getAPI
    def test_AuditionLessonInfo_pc(self):
        Url = config.sjy_host_pc + "/api/user/getAuditionLessonInfo?pid=4&version=4&level=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #生成试卷
    @pytest.mark.getAPI
    def test_createJuan_pc(self):
        Url = config.sjy_host_pc + "/api/Answer/createJuan?unitId=201"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #答题系统首页
    @pytest.mark.getAPI
    def test_Answer_index_pc(self):
        Url = config.sjy_host_pc + "/api/Answer/index"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # #获取单元题目
    #线上数据有问题，等待江兵解决
    # @pytest.mark.getAPI
    # def test_juanHistory_pc(self):
    #     Url = config.sjy_host_pc + "/api/Answer/juanHistory?unitId=201"
    #     print(Url)
    #     res = requests.get(url=Url, headers=self.header)
    #     print(res.json())
    #     assert res.json()["code"] == 10000 or res.json()["code"] == 10106

    #微信获取二维码
    @pytest.mark.getAPI
    def test_getChatQrImage_pc(self):
        Url = config.sjy_host_pc + "/api/weixin/getChatQrImage"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #视频连接列表
    @pytest.mark.getAPI
    def test_videoLink_pc(self):
        Url = config.sjy_host_pc + "/api/videoLink/index?userId=1603940717807987&page=1&source=pc"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #视频连接详情
    @pytest.mark.getAPI
    def test_videoLinkInfo_pc(self):
        Url = config.sjy_host_pc + "/api/videoLink/linkInfo?userId=1603940717807987&videoId=1&source=pc"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000 or res.json()["code"] == 10036


    #视频列表--V3 临时版本
    @pytest.mark.getAPI
    def test_videoList_v3_pc(self):
        Url = config.sjy_host_pc + "/api/video/getVideoListV3?level=1&userId=1603940717807987&status=2&version=3&pid=4"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000 or res.json()["code"] == 10501


    #学习资料列表
    @pytest.mark.getAPI
    def test_MaterialList_pc(self):
        Url = config.sjy_host_pc + "/api/Material/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #资料详情
    @pytest.mark.getAPI
    def test_Materialdetail_pc(self):
        Url = config.sjy_host_pc + "/api/Material/detail?id=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #解绑菜单是否展示
    @pytest.mark.getAPI
    def test_showExchangeMenu_pc(self):
        Url = config.sjy_host_pc + "/api/wxExchange/showExchangeMenu"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # #直播间信息
    # @pytest.mark.getAPI
    # def test_liveroominfo_pc(self):
    #     Url = config.sjy_host_pc + "/api/live-m/live/room/info"
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 100000 or res.json()["code"] == 130001


    # #直播间回放列表
    # @pytest.mark.getAPI
    # def test_replaylist_pc(self):
    #     liveroom_id = mysqld.fetch(table="wm_live_class.wl_live_room", col="room_id", relation="", limitd=1)["msg"][0]
    #     Url = config.sjy_host_pc + "/api/live-m/live/replay/list?room_id=%s" %(liveroom_id)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 100000


    # #回放详情
    # @pytest.mark.getAPI
    # def test_obtain_replay_info(self):
    #     liveroom_id = mysqld.fetch(table="wm_live_class.wl_live_room,wm_live_class.wl_live_room_replay", col="room_id,session_id", relation="", limitd=1)["msg"][0]
    #     Url = config.sjy_host_pc + "/api/live-m/live/replay/info?room_id=%s&session_id=%s" % (liveroom_id[0],liveroom_id[1])
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 100000



if __name__=="__main__":
     pytest.main(["-s","test_pc_get.py"])

     # 10000 = > 'ok',
     # 10001 = > '参数有问题',
     # 10002 = > '请求超时',
     # 10003 = > '您稍微登录',
     # 10004 = > '请求返回数据为空',
     # 10005 = > '抱歉，您没有任何内容操作',
     # 10006 = > '抱歉，验证码超时',
     # 10007 = > '抱歉,您尚未提交数据',
     # 10008 = > '验证码有问题',
     # 10009 = > '发送验证码失败',
     # 10010 = > '手机号已经存在',
     # 10011 = > '没有对应的版本',
     # 10012 = > '校验token成功',
     # 10013 = > '校验token签名不正确',
     # 10014 = > '校验时间过期,请重新登录',
     # 10015 = > '抱歉,请先做完小结测试',
     # 10016 = > '抱歉,您输入的密码有误',
     # 10017 = > '抱歉,您上一节的小结测试没有做完',
     # 10106 = > '考试信息不存在!',
     # 10036 = > '抱歉,该视频连接不存在',
     # 10501 = > '抱歉，异常数据',
     #
     # 11015 = > '订单生成失败，请重试',
     # 11016 = > '输入金额异常',
     # 11017 = > '订单支付中，请稍后',
     # 11018 = > '订单异常，请重试',
     # 11019 = > '请复制订单到其他浏览器中进行支付',
     # 11020 = > '此订单只可以在微信客户端中进行支付',
     #
     # 10018 = > '抱歉,您今天发送短信已超出限制条数',
     # 10019 = > '抱歉，验证码有误',
     # 10020 = > '抱歉，请您发送验证码',
     # 10021 = > '抱歉,发送短信太频繁了，请晚些使用',
     # 10022 = > '抱歉,请重新设置新密码',



     # 10034 = > '抱歉，您的账号在PC其他浏览器登陆，您被强制退出，请您尽快更改密码'