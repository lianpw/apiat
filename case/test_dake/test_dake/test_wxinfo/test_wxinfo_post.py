
#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_WxInfo_post(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()



    # #添加短信模板(返回结果有问题)
    # @pytest.mark.postAPI
    # def test_add_template(self):
    #     Url = config.sjy_host_wxinfo + "/api/sms_template/add_template"
    #     body = {
    #         "template_type": 1,#短信类型：1验证码，2短信通知，3推广短信
    #         "international": 1,#是否国际/港澳台短信：1国内，2国际/港澳台
    #         "template_name": "test",#模板名称
    #         "template_content": "test测试",#模板内容
    #         "remark": 1,#短信模板申请说明
    #         "template_key": 1#微淼端短信模板标识(与模板一一对应)wm_login_sms
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()




    # #短信模板列表
    # @pytest.mark.postAPI
    # def test_get_template_list(self):
    #     Url = config.sjy_host_wxinfo + "/api/sms_template/get_template_list"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    #发送模板消息
    #发送短信消息




    # #发送钉钉消息
    # @pytest.mark.postAPI
    # def test_send_dingding(self):
    #     Url = config.sjy_host_wxinfo + "/api/sms/dingding/send"
    #     body = {
    #         "app_name": 'advanced',#app名称：primary 小白营，advanced大课
    #         "mobile": '13261922481',
    #         "content": "测试内容"#内容
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()


    # #添加签名
    # @pytest.mark.postAPI
    # def test_add_sign(self):
    #     Url = config.sjy_host_wxinfo + "/api/backend/sms/sign/add"
    #     body = {
    #         "name": 1,#签名名称
    #         "supplier_ids": 1#供应商id,多个以英文逗号分隔
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #添加供应商
    # @pytest.mark.postAPI
    # def test_add_supplier(self):
    #     Url = config.sjy_host_wxinfo + "/api/backend/sms/supplier/add"
    #     body = {
    #         "name": 1
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #添加短信模板
    # @pytest.mark.postAPI
    # def test_add_tpl(self):
    #     Url = config.sjy_host_wxinfo + "/api/backend/sms/tpl/add"
    #     body = {
    #                 "business_id": 1,#所属业务方ID
    #                 "tpl_type": 1,#模板类型
    #                 "tpl_name": "test",#模板名称
    #                 "tpl_content": "test测试",#模板内容
    #                 "remark": 1,#短信模板申请说明
    #                 "supplier_ids": 1#审核渠道，多个以英文逗号分隔
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #提交模板审核数据
    # @pytest.mark.postAPI
    # def test_modify_tpl(self):
    #     Url = config.sjy_host_wxinfo + "/api/backend/sms/tpl/modify"
    #     body = {
    #                 "tpl_id": 1,#所属业务方ID
    #                 "tpl_content": "test测试",#模板内容
    #                 "remark": 1,#短信模板申请说明
    #                 "supplier_ids": 1#审核渠道，多个以英文逗号分隔
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #添加规则
    # @pytest.mark.postAPI
    # def test_add_rule(self):
    #     Url = config.sjy_host_wxinfo + "/api/backend/sms/rule/add"
    #     body = {
    #         "tpl_id": '1',#所属业务方ID
    #         "sign_id": '1',#签名id
    #         "business_id": "1",#业务方id
    #         "supplier_weight": '1|30',#权重。格式：1|30,2|69,4|1 ；说明：供应商id|权重,供应商id|权重,供应商id|权重
    #         "remark": 1#备注
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



if __name__=="__main__":
     pytest.main(["-s","test_wxinfo_post.py"])