# -*- coding: utf-8 -*-



import pytest,requests
from config import config
from  utils import baseData,login,stamp

room_wxid= '22739706259@chatroom',
data= '2020-11-19 12:46:36',
essence_name= '123',
essence_intro= '123',
essence_image_url= 'http://dev-tool.weimiaocaishang.com/api/marketing_tools/admin/wechat/getEssence?id=1'
effective_time= '2020-11-19 12:46:36',
essence_title= '测试'

#精华
class Test_Essence(object):


    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = config.wm_user
        self.header['Content-Type'] = 'application/json'

    # #保存 更新精华
    # @pytest.mark.postAPI
    # def test_setEssence(self):
    #     Url=config.marketing_host +'/api/marketing_tools/admin/wechat/setEssence'
    #     body={
    #         "room_wxid":room_wxid,
    #         "data":data,
    #         "essence_name":essence_name,
    #         "essence_intro":essence_intro,
    #         "essence_image_url":essence_image_url,
    #         "effective_time":effective_time,
    #         "essence_title":essence_title
    #     }
    #     res=requests.post(url=Url,params=body,headers=self.header)
    #     #print("保存 更新精华:",res.json())
    #     assert res.json()['code']== 200

    #获取精华
    @pytest.mark.getAPI
    def test_getEssence(self):
        Url=config.marketing_host +'/api/marketing_tools/admin/wechat/getEssence'
        body={"page":"1"}
        res=requests.get(url=Url,params=body,headers=self.header)
        #print("获取精华",res.json())
        assert res.json()['code']== 200

    #精华列表
    @pytest.mark.getAPI
    def test_essenceList(self):
        Url=config.marketing_host +'/api/marketing_tools/admin/wechat/essenceList'
        body={"room_wxid":room_wxid}
        res=requests.get(url=Url,params=body,headers=self.header)
        #print("精华列表",res.json())
        assert res.json()['code']== 200

    #编辑 展示 获取精华
    @pytest.mark.getAPI
    def test_getEssenceEdit(self):
        Url=config.marketing_host +'/api/marketing_tools/admin/wechat/getEssenceEdit'
        body = {"room_wxid": room_wxid}
        res = requests.get(url=Url, params=body, headers=self.header)
        #print("编辑 展示 获取精华", res.json())
        assert res.json()['code']== 200

    # #预览精华
    # @pytest.mark.postAPI
    # def test_setPreviewEssence(self):
    #     Url=config.marketing_host+'/api/marketing_tools/admin/wechat/setPreviewEssence'
    #     body = {
    #         "room_wxid": room_wxid,
    #         "data": data,
    #         "essence_name": essence_name,
    #         "essence_intro": essence_intro,
    #         "essence_image_url": essence_image_url,
    #         "effective_time": effective_time,
    #         "essence_title": essence_title
    #     }
    #     res = requests.post(url=Url, params=body, headers=self.header)
    #     #print("预览精华:", res.json())
    #     assert res.json()['code']== 200

if __name__ == '__main__':
    pytest.main(["-s", "test_essence.py"])
