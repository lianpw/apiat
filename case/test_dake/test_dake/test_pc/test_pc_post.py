#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Testpc_post(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    # #用户登录
    # @pytest.mark.postAPI
    # def test_user_login(self):
    #     Url = config.sjy_host_pc + "/api/user/login"
    #     body = {
    #         "mobile": '13261922481',
    #         "password": '123456',
    #         "source": 'pc'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #短信发送验证码
    # @pytest.mark.postAPI
    # def test_user_sendMessage(self):
    #     Url = config.sjy_host_pc + "/api/user/sendMessage"
    #     body = {
    #         "mobile": '13261922481',
    #         "time": '',
    #         "class_token": '',
    #         "source": 'pc'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #更改用户信息
    # @pytest.mark.postAPI
    # def test_user_updateInfo(self):
    #     Url = config.sjy_host_pc + "/api/user/updateInfo"
    #     body = {
    #         "userId": '10001727',#用户id
    #         "sex": '男',#性别
    #         "degree": '本科',#学位
    #         "income": '10000-50000',#薪资范围
    #         "uname": '少年',#用户名称
    #         "address": '',#地址
    #         "job": '',#职位
    #         "trade": '',#职位
    #         "source": 'pc',#来源：pc/wap
    #         "time": '',#当前时间戳
    #         "class_token": '',
    #         "province": '北京',#省份
    #         "city": '北京'#城市
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #退出登录
    # @pytest.mark.postAPI
    # def test_user_LoginOut(self):
    #     Url = config.sjy_host_pc + "/api/user/userLoginOut"
    #     body = {
    #         "userId": '1604919470530908',
    #         "source": 'pc',
    #         "time": '',
    #         "class_token": ''
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #用户信息
    # @pytest.mark.postAPI
    # def test_user_info(self):
    #     Url = config.sjy_host_pc + "/api/user/getUserInfo"
    #     body = {
    #
    #         "userId": '10001727'#用户id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #提交章节测试
    # @pytest.mark.postAPI
    # def test_user_submitChapter(self):
    #     Url = config.sjy_host_pc + "/api/chapter/submitChapter"
    #     body = {
    #
    #         "categoryId": '1',
    #         "version": '3',
    #         "content": '{  "single": {    "1": 2,    "2": 2,    "3": 1,    "4": 1  },  "judge": {    "1": 1,    "2": 1,    "3": 2  }}'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #获取提交金额获取订单信息
    # @pytest.mark.postAPI
    # def test_user_doOrder(self):
    #     Url = config.sjy_host_pc + "/api/payment/doOrder"
    #     body = {
    #
    #         "payType": '1',#支付方式：1，微信扫码支付；2，支付宝支付
    #         "price": '2998',
    #         "payFrom": 'pc'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    #提交答案


    # #微信绑定手机号
    # @pytest.mark.postAPI
    # def test_user_bindMobile(self):
    #     Url = config.sjy_host_pc + "/api/weixin/bindMobile"
    #     body = {
    #
    #         "mobile": '13400001000',
    #         "code": '111111',
    #         "openId": 'o6wQe0g5EJfrB4y8Lp0q3e0MxT14'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    # #校验用户是否扫码(需要一个获取sceneid的接口)
    # @pytest.mark.postAPI
    # def test_user_checkLogin(self):
    #     Url = config.sjy_host_pc + "/weixin/checkLogin"
    #     body = {
    #
    #         "sceneId": '1605092822967463DD48F52FD7D5948BD7C0A8968ACF8B1E'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()



if __name__=="__main__":
     pytest.main(["-s","test_pc_post.py"])