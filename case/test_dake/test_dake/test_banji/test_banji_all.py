
#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_Banji(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()



    # #用户开课(接口有问题)
    # @pytest.mark.postAPI
    # def test_user_openCourse(self):
    #     Url = config.sjy_host_pc + "/classManage/openCourse"
    #     body = {
    #         "phone": "reprehenderit quis",
    #         "price": -96490214,
    #         "mid": "adipisicing voluptate in",
    #         "area": "Excepteur Ut est occaecat nisi",
    #         "realPayMoney": -72742462
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #用户升级课程(接口有问题)
    # @pytest.mark.postAPI
    # def test_user_upgradeLesson(self):
    #     Url = config.sjy_host_pc + "/classManage/upgradeLesson"
    #     body = {
    #         "mid": "ex",
    #         "orderNum": -36083358.06627907,
    #         "price": 58250034,
    #         "uid": -7913938,
    #         "area": 70402792.43519452
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #用户冻结
    # @pytest.mark.postAPI
    # def test_user_Frozen(self):
    #     Url = config.sjy_host_pc + "/classManage/userFrozenProcess"
    #     body = {
    #         "mid": "1604893344061259",
    #         "status": 1#状态：1解冻, 2冻结
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #大课分班
    # @pytest.mark.postAPI
    # def test_user_splitClass(self):
    #     Url = config.sjy_host_pc + "/classManage/splitClass"
    #     body = {
    #         "mid": 1604893344061259,#学号
    #         "price": 2998,#报名金额
    #         # "uName": "sunt esse",#学员姓名
    #         # "teacherWechat": "in anim mollit",#老师二维码
    #         # "teacherName": "aliqua mollit",#老师姓名
    #         # "zid": -75647562.3610128,#小组
    #         # "splitWeekDay": -94163047.03615306#星期几
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #取消分班
    # @pytest.mark.postAPI
    # def test_user_cancelSplitClass(self):
    #     Url = config.sjy_host_pc + "/classManage/cancelSplitClass"
    #     body = {
    #         "mid": 1604893344061259#学号
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #取消预选分班
    # @pytest.mark.postAPI
    # def test_user_cancelPrepareClass(self):
    #     Url = config.sjy_host_pc + "/ClassManage/cancelPrepareClass"
    #     body = {
    #         "mid": 1604893344061259#学号
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()




if __name__=="__main__":
     pytest.main(["-s","test_banji_all.py"])