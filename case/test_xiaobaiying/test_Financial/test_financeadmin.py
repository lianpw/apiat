# coding:UTF-8
import json

import pytest,requests

from config import config
from utils import  login, stamp




# 手动添加财务流水审核
class Test_Financeadmin(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    # # 获取配置
    # @pytest.mark.postAPI
    # def test_configsp(self):
    #     Url = config.financial_host + '/api/financeadmin/manualSummary/configs'
    #     body = {
    #         "app_key": "xiaobai",
    #         "sign": "90ae665ed99d8743ff21195517e29f16"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     #print("获取配置:", res.json())
    #     assert res.json()['code'] == 20000
    #
    # # 添加财务流水
    # @pytest.mark.postAPI
    # def test_add(self):
    #     Url = config.financial_host + '/api/financeadmin/manualSummary/add'
    #     body = {
    #         "app_key": "xiaobai",
    #         "sign": "50d55448532eaa193863428d1e41f89b",
    #         "mid": "1607137424951972",
    #         "mobile": "18601921332",
    #         "channel": "4",
    #         "company_id":"1",
    #         "admin_id": "9001",
    #         "admin_name": "123",
    #         "real_name": "123",
    #         "pay_picture": "123",
    #         "pay_time":"2020-12-01 16:01:10",
    #         "price": "6998",
    #         "admin_employee_number": "1000"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     #print("添加财务流水:", res.json())
    #     assert res.json()['code'] == 20000
    #
    # # 流水查询列表
    # @pytest.mark.postAPI
    # def test_list(self):
    #     Url = config.financial_host + '/api/financeadmin/manualSummary/list'
    #     body = {
    #         "app_key": "xiaobai",
    #         "sign": "9b2bd50866b698ad7d19041928c675b8",
    #         "auditor_name": "ceshi",
    #         "audit_time": "2020-12-01 17:01:10",
    #         "audit_desc": "ceshi"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     #print("流水查询列表:", res.json())
    #     assert res.json()['code'] == 20000


if __name__ == '__main__':
    pytest.main(["-s", "test_financeadmin.py"])
