# coding:UTF-8

import pytest, requests, json
from config import config
from utils import login



class Test_CompanyInOut():
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    # 日维度列表
    @pytest.mark.getAPI
    def testcompanyInOut_list(self):
        Url = config.financial_host + '/api/companyInOut/list'
        res = requests.get(url=Url, headers=self.header)
        #print("日维度列表:", res.json())
        assert res.json()['code'] == 20000

    # 年维度列表
    @pytest.mark.getAPI
    def test_companyInOut_year(self):
        Url = config.financial_host + '/api/companyInOut/year'
        res = requests.get(url=Url, headers=self.header)
        #print("年维度列表:", res.json())
        assert res.json()['code'] == 20000

    # 月维度列表
    @pytest.mark.getAPI
    def test_companyInOut_month(self):
        Url = config.financial_host + '/api/companyInOut/month'
        body = {
            "year": 2020

        }
        res = requests.get(url=Url, params=body, headers=self.header)
        #print("月维度列表:", res.json())
        assert res.json()['code'] == 20000


if __name__ == '__main__':
    pytest.main(["-s", "test_companyInOut.py"])
