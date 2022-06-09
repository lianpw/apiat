# -*- coding: utf-8 -*-
# Auth:guoxiaohua


import pytest,requests
from config import config
from  utils import baseData,login,stamp


page = 1
page_size = 20
group_name = '112'
group_owner_nickname = '生如夏花'
owner_nickname = '222'
auth_uid = '1000000005'
wxid = 'wxid_3pwmc76c81si22'
wechat_id = '11111'
keyword = 'w'
room_wxid = '22739706259@chatroom'
wechat_wxuser_wxid = 'wxid_qhj3kntwbmj022'
# 群管理
class TestWechat(object):


    def setup_class(self):
        token = login.login()
        self.start_time = stamp.timeday(0)
        self.end_time = stamp.timeday(+1)
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    # # 微信群列表
    # @pytest.mark.getAPI
    # def test_get_group_list(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/group/list'
    #     res = requests.get(url=Url,headers=self.header)
    #     print('微信群列表:', res.json())
    #     assert res.json()['code'] == 200

    # 微信群成员列表(包括excel导出功能)
    @pytest.mark.getAPI
    def test_get_group_member(self):
        Url = config.marketing_host + '/api/marketing_tools/admin/wechat/group_member/list'
        body = {
            "room_wxid": room_wxid
        }
        res = requests.get(url=Url,params=body, headers=self.header)
        assert res.json()['code'] == 200

    # 获取某个微信号待导入的群列表
    @pytest.mark.getAPI
    def test_get_export_group(self):
        Url = config.marketing_host + '/api/marketing_tools/admin/wechat/to_export_group/list'
        body = {
            "wxid": wxid
        }
        res = requests.get(url=Url,params=body, headers=self.header)
        assert res.json()['code'] ==200

    # # 导入群
    # @pytest.mark.postAPI
    # def test_post_export_group(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/to_export_group/export'
    #     body ={
    #         "room_wxid":room_wxid,
    #         "wechat_wxuser_wxid":wechat_wxuser_wxid
    #     }
    #     res = requests.post(url=Url,params=body,headers=self.header)
    #     #print('导入群',res.json())
    #     assert res.json()['code'] ==200
    #
    # # 更改群成员类型
    # @pytest.mark.postAPI
    # def test_post_change_member_type(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/group_member/change_member_type'
    #     body ={
    #         "wxid":wxid,
    #         "member_type":1
    #     }
    #     res = requests.post(url=Url,params=body,headers=self.header)
    #     #print('更改群成员类型',res.json())
    #     assert res.json()['code'] ==200

if __name__ == '__main__':
    pytest.main(["-s", "test_group_management.py"])
