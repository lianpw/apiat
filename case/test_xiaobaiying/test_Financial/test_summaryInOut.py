#coding:UTF-8


import pytest,requests,json
from config import config
from utils import login


class Test_SummaryInOut():
    def setup_class(self):
        token=login.login()
        self.header =config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'


    #月日维度列表
    @pytest.mark.getAPI
    def test_summaryInOut_list(self):
        Url = config.financial_host +'/api/summaryInOut/list'
        res=requests.get(url=Url,headers=self.header)
        #print("月日维度列表:",res.json())
        assert res.json()['code']==20000


    #年的维度
    @pytest.mark.getAPI
    def test_summaryInOut_year(self):
        Url =config.financial_host +'/api/summaryInOut/year'
        res=requests.get(url=Url,headers=self.header)
        #print("年的维度:",res.json())
        assert res.json()['code']==20000


if __name__ =='__main__':
    pytest.main(["-s","test_summaryInOut.py"])
