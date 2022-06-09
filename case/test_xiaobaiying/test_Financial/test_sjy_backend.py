#coding:utf-8
#author by wangyunbao
import time

import pytest,requests,json
from config import config
from utils import stamp,login,aes

class TestSjyBackend():
    def setup_class(self):
        self.header = login.xby_login()
        self.header["Content-Type"]="application/json"

    # 接口有报错
    # def test_getUserInfoByMids(self):
    #     Url=config.xby_host+"/Api/User/getUserInfoByMids"
    #     body = '{"mid":"1601272477437100"}'
    #     ase_body = aes.encrypt(body)
    #     res = requests.post(url=Url,data=ase_body,headers=self.header)
    #     print(res.text)

if __name__ == '__main__':
	pytest.main(["-s", "test_sjy_backend.py"])
