
#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_Course(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()



    # #班级注册课表(查询wm_schedule.wm_schedules)
    # @pytest.mark.postAPI
    # def test_banji_register(self):
    #     Url = config.sjy_host_course + "/api/banji/register"
    #     body = {
    #
    #             "bid": 21674081,#班级id
    #             "app_name": "laborum",#大课：SJY；小白营：XBY
    #             "start_course_week": 57149864.45596555,#开班时间,格式'2020-09-09'
    #             "class_type": "fugiat nostrud eu Lorem",#上课时间周几 1-7
    #             "class_time": "consequat enim amet non"#班级类型
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()




    # #修改课表
    # @pytest.mark.postAPI
    # def test_banji_changeSchedule(self):
    #     Url = config.sjy_host_course + "/api/banji/changeSchedule"
    #     body = {
    #
    #         "bid": -59716857,
    #         "app_name": "in",
    #         "carry_forward": "et in est sunt",
    #         "serial_num": "fugiat commodo enim tempor"
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



    # #获取课程列表
    # @pytest.mark.postAPI
    # def test_banji_getList(self):
    #     Url = config.sjy_host_course + "/api/schedule/getList"
    #     body = {
    #
    #         "bid": "Excepteur nulla",
    #         "appName": "sed"
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     return res.json()



if __name__=="__main__":
     pytest.main(["-s","test_course_all.py"])