#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Testwap(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()

    #答题系统首页
    @pytest.mark.getAPI
    def test_Answer_index(self):
        Url = config.sjy_host_loign + "/api/Answer/index"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000

    #地级市联动
    @pytest.mark.getAPI
    def test_user_getRegion(self):
        Url = config.sjy_host_loign + "/api/user/getRegion"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000
    #

    # #获取单元题目
    # @pytest.mark.getAPI
    # def test_timu_unit(self):
    #     units_id = mysqld.fetch(table="wm_class.wm_class_juan", col="unit_id", relation="", limitd=1)["msg"][0][0]
    #     Url = config.sjy_host_loign + "/api/Answer/juanHistory?unitId=%s" %(units_id)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    #生成试卷
    @pytest.mark.getAPI
    def test_create_Juan(self):
        units_id = mysqld.fetch(table="wm_class.wm_class_juan", col="unit_id", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_loign + "/api/Answer/createJuan?unitId=%s" %(units_id)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000 or res.json()["code"] == 10104

    # #上传签名
    # @pytest.mark.getAPI
    # def test_upload_Contract_Sign(self):
    #     Url = config.sjy_host_loign + "/api/Contracts/uploadContractSign"
    #     print(Url)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    #合同列表
    @pytest.mark.getAPI
    def test_Contract_LIst(self):
        Url = config.sjy_host_loign + "/api/Contracts/getContractLIst"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000

    #用户合同详情
    @pytest.mark.getAPI
    def test_user_Contracts_info(self):
        Url = config.sjy_host_loign + "/api/Contracts/Index?id=398319"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # #授权缓存用户微信信息
    # @pytest.mark.getAPI
    # def test_WxAuth_query_User(self):
    #     Url = config.sjy_host_loign + "/api/WxAuth/queryUser?code=%s&url=%s" %(10000,"http://test-m.weimiao.cn/")
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    #首页
    @pytest.mark.getAPI
    def test_shouye(self):
        Url = config.sjy_host_loign + "/api/Index/index"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # #是否更换手机号
    # @pytest.mark.getAPI
    # def test_isChange_iphone(self):
    #     Url = config.sjy_host_loign + "/api/isChangeOpenid"
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    # #视频详情
    # @pytest.mark.getAPI
    # def test_get_Video_Info(self):
    #     vioeo_info = mysqld.fetch(table="wm_class.wm_video", col="v_id,id,category_id,version_id", relation="", limitd=1)["msg"][0]
    #     Url = config.sjy_host_loign + "/api/video/getVideoInfo?vId=%s&id=%s&c_id=%s&version=%s&pid=%s" %(vioeo_info[0],vioeo_info[1],vioeo_info[2],vioeo_info[3],12)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000

    # 授权获取jsticket
    @pytest.mark.getAPI
    def test_query_JsTicket(self):
        Url = config.sjy_host_loign + "/api/WxAuth/queryJsTicket?url='http://www.weimiao.cn'"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 查询商品详情
    @pytest.mark.getAPI
    def test_query_Goods_Info(self):
        Url = config.sjy_host_loign + "/api/Pay/queryGoodsInfo?price=2998"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 查询订单结果
    @pytest.mark.getAPI
    def test_query_Order_Result(self):
        order_No = mysqld.fetch(table="wm_class.wm_order", col="ordernum", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_loign + "/api/Pay/queryOrder?tradeNo=%s" %(order_No)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 微信体系外支付宝/京东订单请求接口
    @pytest.mark.getAPI
    def test_query_payOrder_zhifubao(self):
        order_No = mysqld.fetch(table="wm_class.wm_order", col="ordernum", relation="", conditions={"paytype":2 },limitd=1)["msg"][0][0]
        Url = config.sjy_host_loign + "/api/Pay/payOrder?tradeNo=%s" %(order_No)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 展示奖状(个人奖+小组奖)
    @pytest.mark.getAPI
    def test_jiangzhuang_show(self):
        Url = config.sjy_host_loign + "/api/Prize/show"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000 or res.json()["code"] ==20026


    # # 获取评分记录的标题
    # @pytest.mark.getAPI
    # def test_pingfen_name(self):
    #     pingfen_id = mysqld.fetch(table="wm_class.wm_teacher_grade_detail", col="id", relation="and", conditions={"uid": 10001727}, limitd=1)["msg"][0][0]
    #     Url = config.sjy_host_loign + "/api/TeacherGrade/getGradeName?id=%s" %(pingfen_id)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000 or res.json()["code"] ==20030 or res.json()["code"] ==20029


    # # 获取详情(需指定uid)
    # @pytest.mark.getAPI
    # def test_Reflections(self):
    #     ganwu_id = mysqld.fetch(table="wm_class.wm_student_reflections", col="id", relation="and", conditions={"uid": 10001727}, limitd=1)["msg"][0][0]
    #     Url = config.sjy_host_loign + "/api/StudentReflections/getDetail?id=%s" %(ganwu_id)
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    # 分页数据
    @pytest.mark.getAPI
    def test_fenye_data(self):
        Url = config.sjy_host_loign + "/api/StudentReflections/getList?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # m站进阶课_进阶课详情查询
    @pytest.mark.getAPI
    def test_landing_Products(self):
        Url = config.sjy_host_loign + "/api/Pay/landingProducts?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # m站进阶课_查询用户购买情况
    @pytest.mark.getAPI
    def test_getUser_Status(self):
        user_phone = mysqld.fetch(table="wm_class.wm_order_address", col="phone", relation="",limitd=1)["msg"][0][0]
        Url = config.sjy_host_loign + "/api/pay/getUserStatus?phone=%s" %(user_phone)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 检测用户是否可购买中财课程
    @pytest.mark.getAPI
    def test_cearch_ispay(self):
        Url = config.sjy_host_loign + "/api/user/declareUser"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 支付成功后获取中财课程&用户听课账号
    @pytest.mark.getAPI
    def test_pay_zcinfo(self):
        Url = config.sjy_host_loign + "/api/pay/zcInfo"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 视频目录列表_优化
    @pytest.mark.getAPI
    def test_video_list2(self):
        Url = config.sjy_host_loign + "/api/video/getVideoListV2"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000

    # # 视频列表_优化
    # @pytest.mark.getAPI
    # def test_video_Category(self):
    #     #user_phone = mysqld.fetch(table="wm_class.wm_order_address", col="phone", relation="", limitd=1)["msg"][0][0]
    #     Url = config.sjy_host_loign + "/api/video/getVideosByCategory?cid=19"
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    # 课程资料列表
    @pytest.mark.getAPI
    def test_Material_list(self):
        Url = config.sjy_host_loign + "/api/Material/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #资料详情
    @pytest.mark.getAPI
    def test_material_info(self):
        matid = mysqld.fetch(table="wm_class.wm_material_info", col="mat_id", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_loign + "/api/Material/detail?id=%s" %(matid)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # #切换清晰度
    # @pytest.mark.getAPI
    # def test_qiehuan_qingxidu(self):
    #     Url = config.sjy_host_loign + "/api/Material/definition?videoId=19&definition=SD"
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    #视频目录列表_优化_v3
    @pytest.mark.getAPI
    def test_video_category_v3(self):
        Url = config.sjy_host_loign + "/api/v3/category?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #视频列表_优化_v3
    @pytest.mark.getAPI
    def test_video_list_v3(self):
        Url = config.sjy_host_loign + "/api/v3/category?cid=19"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #微信用户是否注册
    @pytest.mark.getAPI
    def test_register_Status(self):
        oid = mysqld.fetch(table="wm_class.wm_user", col="opid", relation="", limitd=1)["msg"][0][0]
        Url = config.sjy_host_loign + "/api/user/registerStatus?openid=%s" %(oid)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #视频目录列表_优化_v3_public
    @pytest.mark.getAPI
    def test_category_public(self):
        canshu = mysqld.fetch(table="wm_class.wm_user", col="version_id", relation="", limitd=1)["msg"][0]
        Url = config.sjy_host_loign + "/api/v3/category-public?version=%s&type=%s" %(canshu[0],1)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #视频列表_优化_v3_public
    @pytest.mark.getAPI
    def test_videolist_public(self):
        Url = config.sjy_host_loign + "/api/v3/video-public?cid=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #最新版本视频入口_v3
    @pytest.mark.getAPI
    def test_video_into(self):
        Url = config.sjy_host_loign + "/api/v3/latest-entrance"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    # 章节测试_v3
    # 小节测试_v3
    #章节测试试题_v3
    # @pytest.mark.getAPI
    # def test_chapter_test_v3(self):
    #     Url = config.sjy_host_three + "/api/v3/chapter-test/list?&c_id=19"
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    # #小节测试试题_v3
    # @pytest.mark.getAPI
    # def test_video_test_v3(self):
    #     Url = config.sjy_host_three + "/api/v3/video-test/list?&v_id=1"
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 10000


    #是否实人通过
    @pytest.mark.getAPI
    def test_contracts_isVerified(self):
        Url = config.sjy_host_loign + "/api/contracts/isVerified"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000


    #用户是否能使用好大课计算器
    @pytest.mark.getAPI
    def test_canUse_Counter(self):
        Url = config.sjy_host_loign + "/api/User/canUseCounter"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 10000




if __name__=="__main__":
     pytest.main(["-s","test_wap_get.py"])