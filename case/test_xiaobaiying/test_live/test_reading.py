#coding:utf-8
#author by wangyunbao

import pytest,requests,json
from config import config
from utils import login,aes,getsign

class TestReading():
    def setup_class(self):
        self.header = login.xby_login()
        self.header["Content-Type"]="application/json"

    @pytest.mark.getAPI
    def test_isCompleted8Homework(self):
        Url = config.xby_host+'/Home/DshApi/isCompleted8Homework'
        res = requests.post(url=Url,data=aes.encrypt('{"mid":"21279"}'),headers=self.header)
        assert 20000==aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_isOpenCourse(self):
        Url = config.xby_host + '/Home/DshApi/isOpenCourse'
        res = requests.post(url=Url, data=aes.encrypt('{"mid":"21279"}'), headers=self.header)
        assert 20000 == aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_isXiaobai(self):
        Url = config.xby_host + '/Home/DshApi/isXiaobai'
        res = requests.post(url=Url, data=aes.encrypt('{"mid":"21279"}'), headers=self.header)
        assert 20000 == aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_isQudao(self):
        Url = config.xby_host + '/Home/DshApi/isQudao'
        res = requests.post(url=Url, data=aes.encrypt('{"unionid":"oDptew-aC8Nui5nGpj5DRYWJUmHk","qudao":[3364]}'), headers=self.header)
        assert 20000 == aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_getUserChannel(self):
        Url = config.xby_host + '/Admin/GetUnionId/getUserChannel'
        res = requests.get(url=Url, params=aes.encrypt('{"mid":"21279"}'),headers=self.header)
        assert '0' == res.text

    @pytest.mark.getAPI
    def test_getUserPaytime(self):
        Url = config.xby_host + '/Admin/GetUnionId/getUserPaytime'
        res = requests.get(url=Url, params=aes.encrypt('{"mid":"21279"}'), headers=self.header)
        assert '0' == res.text

    @pytest.mark.getAPI
    def test_getUserPaytime(self):
        Url = config.xby_host + '/Home/DshApi/WxpayBefore'
        res = requests.post(url=Url, data=aes.encrypt('{"mid":"1598438614395048","xcx_openid":"oFdJL5FQq_pvQBwzvgf5IrWWUsqg","type":"50001","typeId":"1"}'), headers=self.header)
        assert 10000 == aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_sendMobileCode(self):
        Url = config.xby_host + '/Home/DshApi/sendMobileCode'
        res = requests.post(url=Url, data=aes.encrypt('{"phone":"13800100500"}'),headers=self.header)
        assert 10000 == aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_checkMobileCode(self):
        Url = config.xby_host + '/Home/DshApi/checkMobileCode'
        res = requests.post(url=Url, data=aes.encrypt('{"phone":"13800100500","code":"1234"}'), headers=self.header)
        assert 10001 == aes.decrypt(res.text)['code']

    @pytest.mark.getAPI
    def test_getTeacherQrcode(self):
        Url = config.xby_host + '/Home/DshApi/getTeacherQrcode'
        res = requests.post(url=Url, data=aes.encrypt('{"mid":"21279"}'), headers=self.header)
        assert 10000 == aes.decrypt(res.text)['code'] or 10002 == aes.decrypt(res.text)['code']

if __name__ == '__main__':
	pytest.main(["-s", "test_reading.py"])