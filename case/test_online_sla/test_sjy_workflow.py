#coding:utf-8
#author by wangyunbao
import time

import pytest,requests
from config import config
from utils import stamp,baseData

class TestSjyWorkFlow(object):

    def setup_class(self):
        self.session = requests.session()
        self.openid = "o6wQe0v5gi6vmcVSuTLdAMsLU4go"
        self.header = {
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.03.2009301 MicroMessenger/7.0.4 Language/zh_CN webview/16032523954072958 webdebugger port/57517 token/b0492a8256e6be0effc7381a1487b7dc",
            "If-None-Match":"A8EF1853E4325FF5326AFE808B1E0D84",
            "Content-Type":"multipart/form-data"
        }

        Url = config.sjy_host + "/api/user/doLogin"
        body = {
            "openId": self.openid
        }
        res = self.session.post(url=Url, data=body)
        self.header["Set-Cookie"] = res.headers["Set-Cookie"]

    #授权登陆后，获取用户信息
    @pytest.mark.onlineTest
    def test_user_login(self):
        res = self.session.get( config.sjy_host+"/api/Index/index",headers = self.header)
        assert res.json()["msg"]=="ok"

    #获取已经付费的课程
    @pytest.mark.onlineTest
    def test_pay_zcinfo(self):
        res = self.session.get(config.sjy_host+"/api/pay/zcInfo",headers = self.header)
        assert  res.json()["msg"]=="success"

    #获取直播类目
    @pytest.mark.onlineTest
    def test_v3_category(self):
        res = self.session.get(config.sjy_host + "/api/v3/category", headers=self.header)
        assert res.json()["msg"]=="ok"

    #获取视频列表
    @pytest.mark.onlineTest
    def test_v3_video(self):
        body = {
            "cid":19
        }
        res = self.session.get(config.sjy_host + "/api/v3/video", params = body,headers=self.header)
        assert  res.json()["msg"]=="ok"

    # 获答题列表
    @pytest.mark.onlineTest
    def test_answer_index(self):
        res = self.session.get(config.sjy_host + "/api/Answer/index",headers=self.header)
        assert  res.json()["msg"]=="success"

    #查询商品详情
    @pytest.mark.onlineTest
    def test_query_goods_info(self):
        body = {
            "price":2998
        }
        res = self.session.get(config.sjy_host + "/api/Pay/queryGoodsInfo",params=body,headers=self.header)
        assert  res.json()["msg"]=="success"

    #m站进阶课_进阶课详情查询
    @pytest.mark.onlineTest
    def test_landing_products(self):
        self.header["Content-Type"] = "application/x-www-form-urlencoded"
        body = {
            "type":"1"
        }
        res = self.session.get(url=config.sjy_host + "/api/Pay/landingProducts",params=body,headers=self.header)
        assert  res.json()["msg"]=="success"


    # 发送验证码
    @pytest.mark.onlineTest
    def test_send_message(self):
        self.header["Content-Type"]="application/x-www-form-urlencoded"
        body = {
            "mobile":stamp.phoneNum(),
            "time":stamp.timeStamp(),
            "class_token":self.header["Set-Cookie"],
            "source":"miniProgram"
        }
        res = self.session.post(url=config.sjy_host + "/api/user/sendMessage", data=body, headers=self.header)
        assert res.json()["msg"]=='ok'

    # # 获取提交金额获取订单信息--系统错误
    # @pytest.mark.onlineTest
    # def test_payment_doorder(self):
    #     self.header["Content-Type"] = "application/x-www-form-urlencoded"
    #     body = {
    #         "payType":"1",
    #         "price":"6998",
    #         "payFrom":"android"
    #     }
    #     res = requests.post(url=config.sjy_host + "/api/payment/doOrder",data=json.dumps(body),headers=self.header)
    #     print(res.text)

    # #创建订单--系统错误
    # @pytest.mark.onlineTest
    # def test_create_order(self):
    #     self.header["Content-Type"] = "application/x-www-form-urlencoded"
    #     body = {
    #         "price":"0.01",
    #         "payType":"1",
    #         "type":"1"
    #     }
    #     res = self.session.post(url=config.sjy_host + "/api/Pay/createOrder",data=json.dumps(body),headers=self.header)
    #     print(res.text)

    #绑定手机号--需要设置验证码
    # @pytest.mark.onlineTest
    # def test_bind_mobile(self):
    #     body = {
    #         "mobile":stamp.phoneNum(),
    #         "openid":self.openid,
    #         "code":111111
    #     }
    #     res = self.session.post(url=config.sjy_host + "/user/bindMobile", data=body,headers=self.header)
    #     print(res.text)

    # 查询订单详情--需要订单id
    # @pytest.mark.onlineTest
    # def test_query_order(self):
    #     orderNo = baseData.create_order()["data"]
    #     body = {
    #         "tradeNo":orderNo["orderInfoList"][0]["order"]["orderNo"]
    #     }
    #     res = self.session.get(config.sjy_host + "/api/Pay/queryOrder",params=body,headers=self.header)
    #     print(res.text)


if __name__=="__main__":
    pytest.main(["-s","test_sjy_workflow.py"])