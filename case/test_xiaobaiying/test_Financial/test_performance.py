# #coding:UTF-8
#
import pytest,requests,json
from config import config
from utils import login

# #绩效管理
class Test_Performance(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

#     #绩效管理列表
#     @pytest.mark.getAPI
#     def test_list(self):
#         Url = config.financial_host + '/api/performance/list'
#         res = requests.get(url= Url,headers =self.header)
#         print(Url)
#         print(res.content)
#         print("绩效管理列表:",res.json())
#         assert res.json()['code'] == 20000
#
#     #获取选项配置
#     @pytest.mark.getAPI
#     def test_changeList(self):
#         Url = config.financial_host +'/api/performance/changeList'
#         res = requests.get(url=Url,headers =self.header)
#         print(res.content)
#         print(Url)
#         print("获取选项配置:",res.json())
#         assert res.json()['code'] == 20000
#
#     #绩效管理详情
#     @pytest.mark.getAPI
#     def test_details(self):
#         Url = config.financial_host +'/api/performance/details'
#         body ={
#             "id":1,
#             "type":1
#         }
#         print(Url)
#         res = requests.get(url = Url,params=body,headers=self.header)
#         print(res.content)
#         print("绩效管理详情:",res.json())
#         assert res.json()['code'] ==20000
#
#
if __name__ =='__main__':
    pytest.main(["-s","test_performance.py"])
