import requests,pytest
from config import config
from utils import login,mysql,baseData
mysqld = mysql.mysqldb()

import json
class Testlive(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = "c_token="+token
        self.appid = '102'

    # 全部资料列表
    @pytest.mark.getAPI
    def test_search_alldata(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/material/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #课程关联的资料列表
    @pytest.mark.getAPI
    def test_datalist_class(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/material/course-material/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #周关联的资料列表
    @pytest.mark.getAPI
    def test_datalist_week(self):
        week_id = mysqld.fetch(table="wm_live_class.wl_course_stage", col="id", relation="", limitd=1)["msg"][0][0]
        ziban_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/material/stage-material/list?stage_id=%s&sub_class_id=%s" % (week_id,ziban_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #指定周-可添加的资料名称列表
    @pytest.mark.getAPI
    def test_datalist_add_zhidingweek(self):
        week_id = mysqld.fetch(table="wm_live_class.wl_course_stage", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/material/can-add/list?stage_id=%s" % (week_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #日历列表
    @pytest.mark.getAPI
    def test_calendar_list(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/calendar/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    # #获取日历信息,确认已废弃
    # @pytest.mark.getAPI
    # def test_obtain_calendarinfo(self):
    #     week_id = mysqld.fetch(table="wm_live_class.wl_calendar", col="id", relation="", limitd=1)["msg"][0][0]
    #     Url = config.dkzb_host + "/api/advanced-backend/live/calendar/info?id=%s" % (week_id)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 100000

    #母班列表
    @pytest.mark.getAPI
    def test_mother_class_list(self):
        tname = mysqld.fetch(table="wm_live_class.wl_teacher", col="auth_username", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/mother/class/list?real_name=%s&calendar_id=%s&page=1" % (tname[0],1)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取母班信息
    @pytest.mark.getAPI
    def test_obtain_mother_class_info(self):
        mom_id = mysqld.fetch(table="wm_live_class.wl_mother_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/mother/class/info?id=%s" % (mom_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #子班列表
    @pytest.mark.getAPI
    def test_child_class_list(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/child/class/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    # 获取子班信息
    @pytest.mark.getAPI
    def test_obtain_child_class_info(self):
        childclass_id = mysqld.fetch(table="wm_live_class.wl_mother_class", col="id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/child/class/info?id=%s" % (childclass_id[0])
        #print(class_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #直播间列表
    @pytest.mark.getAPI
    def test_live_room_list(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/room/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #从权限中心获取老师信息
    @pytest.mark.getAPI
    def test_obtain_teacher_info(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/account/info"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #课程列表
    @pytest.mark.getAPI
    def test_class_list(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/mother/class/course/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #课程-周题目数统计信息
    @pytest.mark.getAPI
    def test_weektimu_data_info(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/exam/all-question/list?course_id=%s" %(1)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #子班学员信息
    @pytest.mark.getAPI
    def test_childclass_user_info(self):
        childclass_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/child/class/user/info?sub_id=%s" % (childclass_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #预选分班排名信息
    @pytest.mark.getAPI
    def test_distribute_info(self):
        distribution = mysqld.fetch(table="wm_live_class.wl_distribution", col="stu_id,item_num",relation="", limitd=5)["msg"][4]
        Url = config.dkzb_host + "/api/advanced-backend/live/class/distribute/rank?stu_id=%s&item_num=%s" % (distribution[0],distribution[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000 or res.json()["code"] == 250101

    # #小组列表
    @pytest.mark.getAPI
    def test_group_list(self):
        childclass_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/group/list?sub_class_id=%s" % (childclass_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #通过子班id获取周的列表
    @pytest.mark.getAPI
    def test_obtain_weeklist(self):
        childclass_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/unit/list?sub_class_id=%s" % (childclass_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #成绩统计列表
    @pytest.mark.getAPI
    def test_achievement_list(self):
        childclass_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/achievement/list?sub_class_id=%s" % (childclass_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #学员成绩明细列表
    @pytest.mark.getAPI
    def test_achievement_student_list(self):
        achievement = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="sub_class_id,stu_id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/achievement/student/list?sub_class_id=%s&stu_id=%s" % (achievement[0],achievement[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #小组成绩明细列表
    @pytest.mark.getAPI
    def test_achievement_group_list(self):
        achievement = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="sub_class_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/achievement/list?sub_class_id=%s" % (achievement)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #后台评分列表(可不带参数)
    @pytest.mark.getAPI
    def test_backend_evaluation_list(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/evaluation/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取未关注公众号学员
    @pytest.mark.getAPI
    def test_obtain_weiguanzhu_stu(self):
        childclass_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/evaluation/stu/info?class_id=%s" % (childclass_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #后台评分详情
    @pytest.mark.getAPI
    def test_evaluation_info(self):
        evaluation_id = mysqld.fetch(table="wm_live_class.wl_teacher_evaluation", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/evaluation/info?id=%s" % (evaluation_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #学员未添加老师微信模板
    @pytest.mark.getAPI
    def test_no_add_wechat(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/un-add-template/info"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #通过用户id获取直播班级及可查看的资料id
    @pytest.mark.getAPI
    def test_material_show(self):
        student_id = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="stu_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/material/show?user_id=%s" % (student_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #通过用户id获取学员考试列表
    @pytest.mark.getAPI
    def test_obtain_exam_info(self):
        student_id = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="stu_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/exam/show?user_id=%s" % (student_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #根据单元id生成答卷（获取随机单/多选题的题目id）
    @pytest.mark.getAPI
    def test_exam_answering(self):
        answer_id = mysqld.fetch(table="wm_live_class.wl_exam_answer", col="current_unit_id,user_id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/exam/answering?unit_id=%s&user_id=%s" % (answer_id[0],answer_id[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #根据单元id获取答题记录
    @pytest.mark.getAPI
    def test_obtain_answer_notes(self):
        answer_id = mysqld.fetch(table="wm_live_class.wl_exam_answer", col="current_unit_id,user_id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/exam/info?unit_id=%s&user_id=%s" % (answer_id[0], answer_id[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #通过用户id获取直播班级信息
    @pytest.mark.getAPI
    def test_obtain_liveroom_infomation(self):
        student_id = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="stu_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/class/student/info?user_id=%s" % (student_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #老师列表
    @pytest.mark.getAPI
    def test_live_teacher_list(self):
        teacher_name = mysqld.fetch(table="wm_live_class.wl_teacher", col="auth_username", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/teacher/list?name=%s&page=%s&page_size=%s" % (teacher_name,1,10)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #某周单选题或多选题列表
    @pytest.mark.getAPI
    def test_exam_unit_question_list(self):
        Url = config.dkzb_host + "/api/advanced-backend/live/exam/unit-question/list?unit_id=%s&type=%s" % (201,1)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #查询分班详情_批量
    @pytest.mark.getAPI
    def test_reach_distribute_info_batch(self):
        student_id = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="stu_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/class/distribute/info-batch?stu_list[]=%s" % (student_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取老师信息
    @pytest.mark.getAPI
    def test_obtain_teacher_infomations(self):
        teacher_id = mysqld.fetch(table="wm_live_class.wl_teacher", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/teacher/info?id=%s" % (teacher_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #查询分班详情
    @pytest.mark.getAPI
    def test_reach_distribute_info(self):
        xueyuan_id = mysqld.fetch(table="wm_live_class.wl_distribution", col="stu_id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/class/distribute/info?stu_id=%s" % (xueyuan_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    #获取课程下的考试信息列表
    @pytest.mark.getAPI
    def test_obtain_exam_infomations(self):
        ziban_id = mysqld.fetch(table="wm_live_class.wl_sub_class", col="id", relation="", limitd=1)["msg"][0][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/exam/list?course_id=%s&sub_class_id=%s" % (1,ziban_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000

    @pytest.mark.getAPI
    def test_classlist_change(self):
        s_id = mysqld.fetch(table="wm_live_class.wl_sub_class_stu", col="stu_id,sub_class_id", relation="", limitd=1)["msg"][0]
        Url = config.dkzb_host + "/api/advanced-backend/live/student/change/class/list?stu_id=%s&old_class_id=%s" %(s_id[0],s_id[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 100000 or res.json()["code"] == 250012#该学员不在此班级

if __name__=="__main__":
     pytest.main(["-s","test_dake_live_get_ctoken.py"])
