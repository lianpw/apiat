#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_wap_post(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()



    # #更改用户信息(编辑数据库)
    # @pytest.mark.postAPI
    # def test_user_sendMessage_wap(self):
    #     Url = config.sjy_host + "/api/user/updateInfo"
    #     body = {
    #         "userId": '10001727',#用户id
    #         "sex": '男',#性别
    #         "degree": '本科',#学位
    #         "income": '10000-50000',#薪资范围
    #         "uname": '少年1',#用户名称
    #         "address": '',#地址
    #         "job": '',#职位
    #         "trade": '',#职位
    #         "source": 'pc',#来源：pc/wap
    #         "time": '',#当前时间戳
    #         "class_token": '',
    #         "province": '北京',#省份
    #         "city": '北京'#城市
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()


    # #用户信息
    # @pytest.mark.postAPI
    # def test_user_info_wap(self):
    #     Url = config.sjy_host + "/api/user/getUserInfo"
    #     body = {
    #
    #         "userId": '10001727'#用户id
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    # #用户登录
    # @pytest.mark.postAPI
    # def test_user_login_wap(self):
    #     Url = config.sjy_host + "/api/user/login"
    #     body = {
    #         "mobile": '13261922481',
    #         "password": '123456',
    #         "source": 'pc'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #短信发送验证码
    # @pytest.mark.postAPI
    # def test_user_sendMessage_wap(self):
    #     Url = config.sjy_host + "/api/user/sendMessage"
    #     body = {
    #         "mobile": '13261922481',
    #         "time": '',
    #         "class_token": '',
    #         "source": 'pc'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #退出登录
    # @pytest.mark.postAPI
    # def test_user_LoginOut_wap(self):
    #     Url = config.sjy_host + "/api/user/userLoginOut"
    #     body = {
    #         "userId": '1604919470530908',
    #         "source": 'pc',
    #         "time": '',
    #         "class_token": ''
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    #提交答案


    # #获取开课时间(预选班级或实体班级)
    # @pytest.mark.postAPI
    # def test_user_ClassWeekDays_wap(self):
    #     Url = config.sjy_host + "/api/SplitClass/getClassWeekDays"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()



    # #执行分班(编辑数据库)
    # @pytest.mark.postAPI
    # def test_user_splitClass_wap(self):
    #     Url = config.sjy_host + "/api/SplitClass/splitClass"
    #     body = {
    #             "weekDay": '1'
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #添加个人选项信息(需修改)
    # @pytest.mark.postAPI
    # def test_user_addInfos_wap(self):
    #     Url = config.sjy_host + "/api/Class/addInfos"
    #     body = {
    #         "age_range": '1',#年龄是否大于50岁 1是 2否 默认0
    #         "degree": '0',#学历是否低于高中 1是 2否 默认0
    #         "invest_experience": '0',#投资经验是否丰富 1是 2否 默认0
    #         "has_computer": '1'#有无电脑 1有 2无 默认0
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    # #取消预选班级
    # @pytest.mark.postAPI
    # def test_cancelPrepareClass_wap(self):
    #     Url = config.sjy_host + "/api/SplitClass/cancelPrepareClass"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    # #视频列表
    # @pytest.mark.postAPI
    # def test_VideoList_wap(self):
    #     Url = config.sjy_host + "/api/video/getVideoList"
    #     body = {
    #         "version": '4',
    #         "pid": '0'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    # #学员评分(写入数据库新数据)
    # @pytest.mark.postAPI
    # def test_addGradeContent_wap(self):
    #     #content_id = mysqld.fetch(table="wm_class.wm_teacher_grade_detail", col="teacher_grade_id", relation="", conditions={"uid":'1603940717807987'},limitd=1)["msg"][0]
    #     Url = config.sjy_host + "/api/TeacherGrade/addGradeContent"
    #     body = {
    #         "id": '150',#content_id[0],#被评论的记录主键
    #         "isRepush": '0',#是否为重新推送(1重新推送 0第一次推送)
    #         "content": 'hao',#评价内容
    #         "score": '95'#评论分数
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()



    # #m站进阶课_创建收货地址
    # @pytest.mark.postAPI
    # def test_saveAddress_m3_wap(self):
    #     Url = config.sjy_host + "/api/pay/saveAddress"
    #     body = {
    #         "user_name": '123',
    #         "phone": '13261922481',
    #         "address": '111'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #购买中财课程后采集用户信息
    # @pytest.mark.postAPI
    # def test_updateUser_wap(self):
    #     Url = config.sjy_host + "/api/Zhc/updateUser"
    #     body = {
    #         "name": '',
    #         "sex": '',#1,男；2，女
    #         "phone": '',
    #         "card": '',#身份证号
    #         "card_local": '',#身份证所属地区1大陆2台湾3香港4澳门5国外
    #         "area_id": ''#手机号所属地区86中国
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #新登录/接口
    # @pytest.mark.postAPI
    # def test_doLogin_new_wap(self):
    #     open_id = mysqld.fetch(table="wm_class.wm_user", col="opid", relation="and",conditions={"id": 1603940717807987}, limitd=1)["msg"][0]
    #     Url = config.sjy_host + "/api/user/doLogin"
    #     body = {
    #         "openId": open_id[0]
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #绑定手机号（新）【需要获取验证码接口】
    # @pytest.mark.postAPI
    # def test_bindMobile_new_wap(self):
    #     open_id = mysqld.fetch(table="wm_class.wm_user", col="opid", relation="and",conditions={"id": 1604893344061259}, limitd=1)["msg"][0]
    #     Url = config.sjy_host + "/api/user/bindMobile"
    #     print(open_id)
    #     body = {
    #         "mobile": '18600001234',
    #         "openId": open_id[0],
    #         "code": '111111'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #修改用户信息
    # @pytest.mark.postAPI
    # def test_user_UpUserAct(self):
    #     Url = config.sjy_host + "/api/user/UpUserAct"
    #     body = {
    #         "username": 'yjb',#用户姓名
    #         "sex": '1',#性别1男 2女
    #         "trade": 'test',#行业
    #         "job": 'test1',#职务
    #         "jobnum": '4',#工作年限
    #         "study": '2',#学历 1(大专)2(本科)3(硕士)4(博士)5（小学）6（初中）7（高中）
    #         "pay": '',
    #         "address": 'beijing'#工作所在城市
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #中财证书快递地址(修改zcbyz表)
    # @pytest.mark.postAPI
    # def test_user_postAddress(self):
    #     Url = config.sjy_host + "/api/Address/postAddress"
    #     body = {
    #         "name": '',
    #         "phone": '',
    #         "address": ''
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #三要素验证接口（手机号&证件号&证件姓名）
    # @pytest.mark.postAPI
    # def test_user_verifyIdentity3(self):
    #     Url = config.sjy_host + "/api/contracts/verifyIdentity3"
    #     body = {
    #         "name": '尹江兵',
    #         "identity": '13220119930712557x',#证件号
    #         "mobile": '13261922481',
    #         "contractId": ''#合同id
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #创建合同模板并获取手签地址
    # @pytest.mark.postAPI
    # def test_user_createAndSignUrl(self):
    #     Url = config.sjy_host + "/api/contracts/createAndSignUrl"
    #     body = {
    #         "contractId": ''#合同id
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #是否签署成功
    # @pytest.mark.postAPI
    # def test_user_isSignedSuccess(self):
    #     contract_id = mysqld.fetch(table="wm_contract_center.wm_contract", col="serial_number", relation="and",conditions={"uid": 1603274174995806}, limitd=1)["msg"][0]
    #     Url = config.sjy_host + "/api/contracts/isSignedSuccess"
    #     body = {
    #         "contractId": contract_id[0]#合同id
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #学员关闭签订提醒
    # @pytest.mark.postAPI
    # def test_user_closeSignNotice(self):
    #     Url = config.sjy_host + "/api/contracts/closeSignNotice"
    #     body = {
    #         "close": '0'#1关闭0获取当日是否已关闭
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #校验3要素验证码
    # @pytest.mark.postAPI
    # def test_user_verifyCode(self):
    #     Url = config.sjy_host + "/api/contracts/verifyCode"
    #     body = {
    #         "code": '123456'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #视频版本升级
    # @pytest.mark.postAPI
    # def test_v3_upgrade(self):
    #     Url = config.sjy_host + "/api/v3/course/upgrade"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #记录添加老师二维码
    # @pytest.mark.postAPI
    # def test_v3_addWechat(self):
    #     Url = config.sjy_host + "/api/Teacher/addWechat"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #中财订单
    # @pytest.mark.postAPI
    # def test_v3_orderLanding(self):
    #     Url = config.sjy_host_backend + "/orderLanding/list.html"
    #     body = {
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()




    #生成订单接口





if __name__=="__main__":
     pytest.main(["-s","test_wap_post.py"])