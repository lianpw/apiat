#coding:utf-8
#author by wangyunbao
import time

import pytest,requests,json
from config import config
from utils import stamp

class TestXbyWorkFlow(object):

    def setup_class(self):
        self.session = requests.session()
        self.openid = "o6wQe0v5gi6vmcVSuTLdAMsLU4go"
        self.header = {
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.03.2009301 MicroMessenger/7.0.4 Language/zh_CN webview/16032523954072958 webdebugger port/57517 token/b0492a8256e6be0effc7381a1487b7dc",
            "If-None-Match":"A8EF1853E4325FF5326AFE808B1E0D84",
            "Content-Type":"application/x-www-form-urlencoded"
        }

        Url = config.xby_host + "/api/user/doLogin"
        body = {
            "openId": self.openid
        }
        res = self.session.post(url=Url, data=body)
        self.header["Set-Cookie"] = res.headers["Set-Cookie"]

    # # 校验验证码--未完成
    # @pytest.mark.onlineTest
    # def test_check_code(self):
    #     body = {
    #         "phone":stamp.phoneNum(),
    #         "code":123456
    #     }
    #     res = requests.post( config.xby_host+"/Home/DshApi/checkMobileCode",data=json.dumps(body),headers = self.header)
    #     print(res.text)

    # 获取分班后二维码
    @pytest.mark.onlineTest
    def test_get_teacher_code(self):
        body = {
            "mid": "1597842789499492"
        }
        res = requests.get(config.xby_host + "/Home/DshApi/getTeacherQrcode",params=body,headers=self.header)
        assert type(res.text) is str

if __name__=="__main__":
    pytest.main(["-s","test_xby_workflow.py"])