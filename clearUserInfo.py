import pymysql,requests
import re
# from log.logger import loggerTest
# from utils import stamp
def clear(mid,role):
    #connect to db
    conn = pymysql.connect(host='rm-2zeti0v9e6940n93p2o.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='web_user',
                           passwd='l%meFN!Z88yRgrjz',
                           # db='wm_class',
                           charset='utf8')
    cur = conn.cursor()  # 使用cursor()方法获取操作游标
    # loggerTest.info("connect to mysql success")
    ##sql list
    ##大课

    dk = [
        "delete from wm_order_center.t_order where member_id= %s",
        "delete from wm_class.wm_order where uid = %s",
        "delete from wm_class.wm_order_batch where user_id = %s",
        "delete from wm_class.wm_user where id = %s",
        "delete from wm_class.wm_class_apply where uid = %s",
        "delete from wm_class.wm_contract where uid = %s",
        "delete from wm_contract_center.wm_contract where uid = %s",
        "delete from wm_contract_center.wm_up_sign_ext where account = %s",

        "delete from  wm_class.wm_user_property where user_id =%s ",
        "delete from wm_class.wm_class_apply where uid=%s ",
        "delete from wm_class.wm_class_apply_api where uid=%s",
        # "delete from wm_class.wm_class_sys_divide where uids like  '%s'",
        "delete from wm_class.wm_class_divide_detail where uid=%s"


    ]

    ## 大课直播
    dklive = [
        "delete from wm_live_class.wl_exam_answer where user_id = %s",
        "delete from wm_live_class.wl_distribution where stu_id = %s",
        "delete from wm_live_class.wl_distribution_queue where stu_id = %s",
        "delete from wm_live_class.wl_sub_class_group_stu where stu_id = %s",
        "delete from wm_live_class.wl_stu_modify_log where stu_id = %s",
        "delete from wm_live_class.wl_sub_class_stu where stu_id = %s",
        "update wm_class.wm_user set class_type = 2 where id = %s",
        "delete from wm_live_class.wl_exam_answer where user_id = %s",
    ]
    ## 小白营
    xby = [
        # "delete from wm_class.wm_order where uid = "
        # "delete from wm_class.wm_user where id = "
        "delete from wm_order_center.t_order where  member_id= %s",
        "delete from weimiao.mh_wxuser where mid = %s",
        "delete from weimiao.mh_wxorder where mid = %s",
        "delete from weimiao.mh_finance where mid = %s",
        "delete from weimiao.mh_finance_summary where mid = %s",
        "delete from weimiao.mh_fineorder where mid = %s",
        "delete from weimiao.mh_order_relation where mid = %s",
        "delete from weimiao.mh_live_signup_log where mid = %s",
        "delete from wm_live.mh_live_order where mid = %s",
        "delete from wm_live.mh_live_order_relation where mid = %s"
    ]
    ## 小白营直播
    xbylive = [
        "delete from weimiao.mh_live_signup_log where mid = %s",   # 小白营用户直播报名记录表
        "delete from wm_live.mh_live_answer_people where mid = %s", # 用户已答题表
        "delete from wm_live.mh_live_finance where mid = %s",   # 财务流水表
        "delete from wm_live.mh_live_finance_summary where mid = %s", # 财务流水表
        "delete from wm_live.mh_live_order where mid = %s" , # 直播0元订单表
        "delete from wm_live.mh_live_order_relation where mid = %s", # 直播用户关联订单表
        "delete from wm_live.mh_live_pay_for_another where mid = %s",# 代付订单表
        "delete from wm_live.mh_live_room_user_action_log where mid = %s" , # 学员进出直播间日志
        "delete from wm_live.mh_live_room_user_click_detail where mid = %s", # 学员点击详情表
        "delete from wm_live.mh_live_room_user_item where mid = %s",  #直播间统计学员数据
        "delete from wm_live.mh_live_special_users where mid = %s" ,#直播间特殊用户表
        "delete from wm_live.mh_live_user where mid = %s" #直播用户表
    ]
    # 信息流
    xxl = [
        "delete from weimiao.mh_infoflow_order where mid = %s", # 信息流订单表
        "delete from weimiao.mh_infoflow_order_item where mid = %s", # 信息流订单表
        "delete from weimiao.mh_infoflow_repeated_register where mid = %s", # 重复报名流水表
        "delete from weimiao.mh_infoflow_test_reset where mid = %s", # 信息流测试单重置
        "delete from weimiao.mh_infoflow_tuikuan_flow where mid = %s", # 信息流退款流水表
        "delete from weimiao.mh_infoflow_tuikuan_flow_item where mid = %s",# 信息流退款流水表
        "delete from weimiao.mh_infoflow_user where auth_uid = %s"  # 信息流用户表
    ]

    xxlphone = [
        "delete from weimiao.mh_infoflow_order where phone = %s",  # 信息流订单表
        "delete from weimiao.mh_infoflow_order_item where phone = %s",  # 信息流订单表
        "delete from weimiao.mh_infoflow_phone_order where phone = %s",  # 信息流分班表
    ]

    user = [
        "delete from wm_user_center.wu_user_third where unionid = (select unionid from wm_user_center.wu_user_main WHERE id = %s)",
        "delete from wm_user_center.wu_user_main where id = %s",
        "delete from wm_ucenter_secret.uc_user_map where user_id = %s",

    ]
    # 读书会
    dsh = [
        "delete from dushuhui.mh_dsh_wxuser where mid = %s",
        "delete from dushuhui.mh_dsh_wxuser_subscribe_log where mid = %s",
        "delete from dushuhui.mh_dsh_wxuser_subscribe where openid = (select openid from dushuhui.mh_dsh_wxuser where mid = %s)",
        "delete from dushuhui.mh_dsh_wxuser_invitation where be_inv_mid = %s",
        "delete from dushuhui.mh_dsh_sp_log where mid = %s"
    ]
    #try
    test = [
        "delete from wm_live_class.wl_distribution where stu_id=%s",
        "delete from wm_live_class.wl_sub_class_stu where stu_id=%s"
        # "delete from weimiao.mh_dv_order where mid=%s",
        # "delete from weimiao.mh_dv_order_activity where mid=%s",
        # "delete from weimiao.mh_infoflow_order where mid=%s"
        # "update wm_drp.drp_user set lock_from=0 where  mid = %s",
        # "update wm_drp.drp_invite_code set mid="+str(100)+stamp.timeStamp()+" where  mid = %s "
        # "delete from wm_marketing_tools.mh_user_conversion where mid = %s",
        # "delete from wm_marketing_tools.mh_tmp_user where mid = %s"
    ]
    fenban = [
        "delete from wm_live_class.wl_distribution where stu_id=%s",
        "delete from wm_live_class.wl_sub_class_stu where stu_id=%s",
        "delete from wm_class.wm_class_apply where uid = %s",
        "delete from wm_class.wm_class_apply_api where uid = %s",
        "update wm_class.wm_user set bid=0 where id = %s",
        "update wm_class.wm_user_property set status = 3 where user_id = %s"
    ]

    ssfine = [
        "delete from weimiao.mh_ssfineorder where mid = %s",
        "delete from wm_order_center.t_order where member_id = %s"
    ]
    if role == 'all':
        all = dk + dklive +xby +xbylive+xxl+dsh

    for i in role:
        print("delete role %s" % i)
        for j in locals()[i]:
            print("sql: ",j)
            result=cur.execute(j, mid)
            if result==1:
                print("affact line: ", result)
                # table = re.search('delete from\s(.*?)\s',j, re.I|re.M).group(1)
                # loggerTest.info("delete user from %s" % (table))
            conn.commit()  # 提交请求

    # for i in locals()[role]:
    #     print(i)
    #     print(mid)
    #     cur.execute(i, mid)
    #     table = re.search('delete from\s(.*?)\s',i, re.I|re.M).group(1)
    #     loggerTest.info("delete user from %s" % (table))
    #     conn.commit()  # 提交请求
    #
    result = cur.fetchall()
    print("result:",result)
    #
    # 关闭数据库连接
    cur.close()
    conn.close()
    # url = 'https://test-m.weimiaocaishang.com/index.php/Home/UserCenterNew/Index.html'
    # res = requests.get(url=url,headers=config.header)
    # print(res.content)
    # print(res.json())





clear('1608721574678402',['xxl','xby','xbylive','dk','dklive'])
# clear('15655817590',['xxlphone'])
#

