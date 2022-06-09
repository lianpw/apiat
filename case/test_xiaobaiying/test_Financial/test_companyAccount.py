#coding:UTF-8

import pytest,requests,json
from config import config
from utils import login



class Test_CompanyAccount():
    def setup_class(self):
        token=login.login()
        self.header=config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'


    #列表
    @pytest.mark.getAPI
    def test_companyAccount_list(self):
        Url =config.financial_host+'/api/companyAccount/list'
        res=requests.get(url=Url,headers=self.header)
        #print("列表:",res.json())
        assert res.json()['code'] ==20000


    #子账户详情
    @pytest.mark.getAPI
    def test_companyAccount_subAccount(self):
        Url=config.financial_host +'/api/companyAccount/subAccount'
        body={
            "num":"A_0001"
       }
        res=requests.get(url=Url,params=body,headers=self.header)
        #print("子账户详情:",res.json())
        assert res.json()['code']==20000


if __name__ == '__main__':
    pytest.main(["-s", "test_companyAccount.py"])