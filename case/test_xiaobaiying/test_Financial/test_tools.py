#coding:UTF-8

import pytest,requests,json
from config import config
from utils import login



class Test_Tools():
    def setup_class(self):
        token =login.login()
        self.header = config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'



    #转介绍学员查询,获取用户第一周考试时间
    @pytest.mark.getAPI
    def test_referralSearch(self):
        Url = config.financial_host +'/api/tools/referralSearch'
        body ={
            "mid":100527
        }
        res = requests.get(url =Url,params=body,headers=self.header)
        assert res.json()['code'] == 20000


if __name__ =='__main__':
    pytest.main(["-s","test_tools.py"])
