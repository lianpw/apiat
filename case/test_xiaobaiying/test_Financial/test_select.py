#coding:UTF-8

import pytest,requests,json
from config import config
from utils import login


class Test_Select():
    def setup_class(self):
        token=login.login()
        self.header =config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    #公司账户编号
    @pytest.mark.getAPI
    def test_accountNums(self):
        Url = config.financial_host + '/api/select/accountNums'
        res = requests.get(url =Url,headers=self.header)
        #print("公司账户编号:",res.json())
        assert res.json()['code'] == 20000

    #资金来源
    @pytest.mark.getAPI
    def test_fundSources(self):
        Url = config.financial_host +'/api/select/fundSources'
        res =requests.get(url = Url,headers=self.header)
        #print("资金来源:",res.json())
        assert res.json()['code'] == 20000


    #公司账户名称
    @pytest.mark.getAPI
    def test_accountTitles(self):
        Url =config.financial_host + '/api/select/companyNames'
        res =requests.get(url=Url,headers=self.header)
        #print("公司账户名称:",res.json())
        assert res.json()['code']==20000

    #商户号
    @pytest.mark.getAPI
    def test_mchIds(self):
        Url =config.financial_host + '/api/select/mchIds'
        res =requests.get(url=Url,headers=self.header)
        #print("商户号；",res.json())
        assert res.json()['code']==20000

    #支付渠道
    @pytest.mark.getAPI
    def test_payChannels(self):
        Url =config.financial_host + '/api/select/payChannels'
        res =requests.get(url=Url,headers=self.header)
        #print("支付渠道:",res.json())
        assert res.json()['code']==20000



if __name__ =='__main__':
    pytest.main(["-s","test_select.py"])

