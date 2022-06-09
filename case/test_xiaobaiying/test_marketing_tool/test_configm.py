# -*- coding: utf-8 -*-



import pytest,requests
from config import config
from  utils import baseData,login,stamp

extra_data= '{"autoAddFriend":true,"autoSayHello":true,"frequency":[50,80],"helleMsgList":[{"msg_type":1,"msg":"wehub/test/6010phpzAVOci201204.jpg","customid":""},{"msg_type":3,"msg":"http://cdn-xiaobai-class.weimiaocaishang.com/wehub/test/6010phpzAVOci201204.jpg","customid":""},{"msg_type":1,"msg":"wehub/test/6010phpzAVOci201204.jpg","customid":""}],"autoAddremark":true,"autoAddTag":true,"remarkType":["nickname","sex","city"],"tagList":["分组1","分组2"]}',
wxid= 'wxid_fivc7mxmzkqp22',


#配置
class Test_Configm(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    # #保存微信配置
    # @pytest.mark.postAPI
    # def test_setWxConfig(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/setWxConfig'
    #     body = {
    #         "extra_data": extra_data,
    #         "wxid": wxid
    #
    #     }
    #     res = requests.post(url=Url, params=body, headers=self.header)
    #     #print("保存微信配置:",res.json())
    #     assert res.json()['code'] == 200

    # #获取配置
    # @pytest.mark.postAPI
    # def test_getWxConfig(self):
    #     Url = config.marketing_host + '/api/marketing_tools/admin/wechat/getWxConfig'
    #     body = {
    #         "wxid": wxid
    #     }
    #     res = requests.get(url=Url, params=body, headers=self.header)
    #     #print("获取配置:",res.json())
    #     assert res.json()['code'] == 200







if __name__ == '__main__':
    pytest.main(["-s", "test_configm.py"])


