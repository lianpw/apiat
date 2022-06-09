# -*- coding: utf-8 -*-
# Auth:guoxiaohua


import pytest, requests


from config import config
from utils import baseData, login, stamp


group_name = '112'
owner_nickname = '222'
auth_uid = '1000000005'
wechat_id = 'WeiMiao688'
wxid = 'wxid_3pwmc76c81si22'
name = '测试'


# 微信号管理
class TestWechat(object):


    def setup_class(self):
        token = login.login()
        self.start_time = stamp.timeday(0)
        self.end_time = stamp.timeday(+1)
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    # 微信号列表（下拉列表）
    # @pytest.mark.getAPI
    # def test_get_wechat_wxuser(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/wxuser/all'
    #     res = requests.get(url=Url, headers=self.header)
    #     #print('微信号列表（下拉列表） :', res.json())
    #     assert res.json()['code'] == 200


    # # 更改微信号启用/禁用状态
    # @pytest.mark.postAPI
    # def test_post_change_enable_status(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/wxuser/change_enable_status'
    #     body = {
    #         "wxid": wxid,
    #         "enable_status": 2
    #     }
    #     res = requests.post(url=Url,params=body, headers=self.header)
    #     #print('更改微信号启用/禁用状态 :', res.json())
    #     assert res.json()['code'] == 200
    #
    # 根据关键词搜索用户的下属列表
    @pytest.mark.getAPI
    def test_get_user_search(self):
        Url = config.marketing_host + '/api/marketing_tools/admin/auth/user_search'
        body = {
            "name":name
        }
        res = requests.get(url=Url,params=body, headers=self.header)
        #print('根据关键词搜索用户的下属列表 :', res.json())
        assert res.json()['code'] == 200 or res.json()['code'] == 100619

    # # 微信号列表(翻页展示)
    # @pytest.mark.getAPI
    # def test_get_wxuser_list(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/wxuser/list'
    #     res = requests.get(url=Url, headers=self.header)
    #     #print('微信号列表(翻页展示):', res.json())
    #     assert res.json()['code'] == 200

    # 微信号归属老师列表(筛选群使用)
    # @pytest.mark.getAPI
    # def test_get_authuser_list(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/authuser/list'
    #     res = requests.get(url=Url, headers=self.header)
    #     #print('微信号归属老师列表:', res.json())
    #     assert res.json()['code'] == 200
    #
    # # 添加/修改微信号(老师账号与微信号做关联)
    # @pytest.mark.postAPI
    # def test_post_bind_authuser_list(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/wxuser/bind_authuser'
    #     body = {
    #         "auth_uid":auth_uid,
    #         "wechat_id":wechat_id
    #     }
    #     res = requests.post(url=Url,params=body, headers=self.header)
    #     #print('添加/修改微信号:', res.json())
    #     assert res.json()['code'] == 200
    #
    # 微信号联想搜索
    @pytest.mark.getAPI
    def test_wxuser_search(self):
        Url = config.marketing_host + '/api/marketing_tools/admin/wechat/wxuser/search'
        body = {
            "keyword": "w"
        }
        res = requests.get(url=Url,params=body, headers=self.header)
        #print('微信号联想搜索:', res.json())
        assert res.json()['code'] == 200

if __name__ == '__main__':
    pytest.main(["-s", "test_wechat_management.py"])
