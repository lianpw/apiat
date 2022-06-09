#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_backend(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()
        self.cla_id = mysqld.exeSQL("select class_id from wm_class.wm_homework_answer where class_id <> 0 limit 1")["msg"][0][0]

    #作业进度列表
    @pytest.mark.getAPI
    def test_homework_weeklist(self):
        Url = config.sjy_host_homework + "/api/practice/homework/week/list?class_id=%s" %(self.cla_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业进度列表
    @pytest.mark.getAPI
    def test_practice_clist(self):
        Url = config.sjy_host_homework + "/api/practice/class/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业信息列表
    @pytest.mark.getAPI
    def test_homework_list(self):
        Url = config.sjy_host_homework + "/api/practice/homework/list?class_id=%s" %(self.cla_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #小组作业统计
    @pytest.mark.getAPI
    def test_homework_summary(self):
        Url = config.sjy_host_homework + "/api/practice/homework/summary?class_id=%s" %(self.cla_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业详情
    @pytest.mark.getAPI
    def test_homework_info(self):
        Url = config.sjy_host_homework + "/api/practice/homework/info?id=%s" %(self.cla_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业成绩
    @pytest.mark.getAPI
    def test_homework_userlist(self):
        user_id = mysqld.fetch(table="wm_class.wm_homework_answer", col="user_id", relation="", conditions={"class_id":self.cla_id},limitd=1)["msg"][0][0]
        Url = config.sjy_host_homework + "/api/practice/homework/user/list?class_id=%s&user_id=%s" %(self.cla_id,user_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业提交状态列表
    @pytest.mark.getAPI
    def test_homework_answer_status_list(self):
        Url = config.sjy_host_homework + "/api/practice/homework/answer_status/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业批改状态列表
    @pytest.mark.getAPI
    def test_homework_check_status_list(self):
        Url = config.sjy_host_homework + "/api/practice/homework/check_status/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #作业统计
    @pytest.mark.getAPI
    def test_homework_class_summary(self):
        Url = config.sjy_host_homework + "/api/practice/summary/homework/class"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #每周作业率
    @pytest.mark.getAPI
    def test_homework_class_week_01(self):
        Url = config.sjy_host_homework + "/api/practice/summary/homework/class/week?class_id=%s" %(self.cla_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #班级列表页
    @pytest.mark.getAPI
    def test_banji_list(self):
        Url = config.sjy_host_homework + "/api/practice/teacher/class/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #课表列表页
    @pytest.mark.getAPI
    def test_schedule_list(self):
        Url = config.sjy_host_homework + "/api/practice/teacher/schedule/list?teacher_id=0&start_date=1604160000&end_date=1606751999"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #老师列表页
    @pytest.mark.getAPI
    def test_schedule_list(self):
        Url = config.sjy_host_homework + "/api/practice/teacher/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #总监列表
    @pytest.mark.getAPI
    def test_schedule_list(self):
        Url = config.sjy_host_homework + "/api/practice/director/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #经理列表
    @pytest.mark.getAPI
    def test_schedule_list(self):
        Url = config.sjy_host_homework + "/api/practice/manage/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #分组组列表(wm_homework_answer)
    @pytest.mark.getAPI
    def test_schedule_list(self):
        Url = config.sjy_host_homework + "/api/practice/class/group/list?class_id=2003"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


if __name__=="__main__":
    pytest.main(["-s","test_backend_center_get.py"])