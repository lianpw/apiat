#coding:utf-8
#author by wangyunbao

#钉钉配置
#自动化机器人的token
at_token = "dad95c0c82fbf8528989ca3f504982d83ec512c6bfbbb7f50b4293eb9cc4ade4"
#自动化机器人的secret
secret = "SEC3342a8627892482d688cbe88c88a7e01c0fbaf28b1e195cb15ad500c003211df"

#header
header = {
            "User-Agent":"PostmanRuntime/7.26.3",
            "Content-Type":"application/json; charset=utf-8",
        }

# #测试环境配置
# host_login="https://test-auth-dashboard.weimiaocaishang.com"
# host_open = "https://test-open.weimiaocaishang.com"
# host = "https://test-internal-open.weimiaocaishang.com"
# sjy_host="http://test-m.weimiao.cn"
# sjy_host_loign="http://test-m.weimiao.cn"
# sjy_host_three = "http://test-m3.weimiao.cn"
# sjy_host_pc = "http://test-course-api.weimiao.cn"
# sjy_host_wxinfo="http://test-internal-sms-center.weimiaocaishang.com"
# sjy_host_backend="http://test4-course-backend.weimiaocaishang.com"
# sjy_host_contract="http://test-contract-center.weimiaocaishang.com"
# sjy_host_course="http://test-internal-schedule-center.weimiaocaishang.com"
# spzx_host="http://test-internal-product-center.weimiaocaishang.com"
# xby_host="http://test-m.weimiaocaishang.com"
# dkzb_host="http://test-advanced-backend.weimiaocaishang.com"
# dkzb_host_fro="http://test-live-m.weimiao.cn"
# live_host = "https://test-live-api.weimiaocaishang.com"
# analysis_host="https://test-traffic-dashboard.weimiaocaishang.com"
# gxpt_bk_host = 'http://test-open.weimiaocaishang.com/api/wm-sharing-platform'
# gxpt_fb_host = 'http://test-splat-api.weimiaochina.com/api'
# sjy_host_homework = "http://test-internal-practice-backend.weimiaocaishang.com"
# marketing_host='http://test-marketing-tools.weimiaocaishang.com/'
# fission_host = "https://test-fission-api.weimiaocaishang.com"
# financial_host = 'http://test-financial-api.weimiaocaishang.com'
# referer_host = 'https://test-m3.weimiaoshangxueyuan.cn/'
# dushuhui_bk_host = "http://test-cswxapi.weimiaocaishang.com"
# dushuhui_bjnews_host = 'http://test-csapi.weimiaocaishang.com'
# #测试环境账户密码
# user = "wangyunbao"
# passwd = "821173WybCr"
# wm_user = 'wm_user={%22sn%22:%22%E6%9D%8E%E6%95%AC%22%2C%22cn%22:%22lijing%22%2C%22mail%22:%22lijing@weimiao.cn%22%2C%22token%22:%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJURVNULlNTTy5JTkZSQS5XRUlNSUFPLkNPTSIsImV4cCI6MTYwNzQyMDMwNywiaWF0IjoxNjA3MzMzOTA3LCJ1c2VyaWQiOjEwMDAwMDAxNDgsInVzZXJuYW1lIjoibGlqaW5nIn0.EaS_vtFmC4DSvr6HI08pHqxjar_wHZnrG321JSVRC68%22}'
# #测试环境数据库配置
# db_order_promotion_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_goods_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_auth_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_dk_live_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_xby_live_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_weimiao_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_class_host= "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_user_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_sharing_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_infoflow_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_subject_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_dushuhui_host = "rm-2zeti0v9e6940n93p.mysql.rds.aliyuncs.com"
# db_port = int(3306)
# db_user = "web_user"
# db_passwd = "l%meFN!Z88yRgrjz"
# db_name = "wm_authority_center"
# #xby测试参数
# #用户mid
# mid = [1598267537355565, 1601029228363241]
# #直播房间号
# room_id = '20102633858014'
# #openId
# openId = 'o6wQe0v5gi6vmcVSuTLdAMsLU4go'       #test1073
# sharing_platform_cookie="zttifLBrNzt5dMUzVIUJaWrB1Pf3nnGMH6l5IDma"
# #dushuhui
# dushuhui="1d75c676ee0bf70a209e9789e28d8959"
# dushuhui_h5="PHPSESSID=o7itm25n7qtc5m63fbgc2rb3av"
#
# #大课直播房间号
# class_room_id = '120'   #待修正
# # stage环境配置
# host = "http://172.17.208.95:8082"

#线上环境配置
host_login="https://auth-dashboard.weimiaocaishang.com"
host_open="http://internal-open.weimiaocaishang.com"
host="http://internal-open.weimiaocaishang.com"
dkzb_host="http://advanced-backend.weimiaocaishang.com"
dkzb_host_fro="http://live-m.weimiao.cn"
sjy_host="http://m.weimiao.cn"
sjy_host_loign="https://m.weimiao.cn"
sjy_host_three = "http://m.weimiao.cn"
sjy_host_pc = "https://course-api.weimiao.cn"
sjy_host_wxinfo="http://internal-sms-center.weimiaocaishang.com"
sjy_host_backend="http://course-backend.weimiaocaishang.com"
sjy_host_contract="http://contract-center.weimiaocaishang.com"
sjy_host_course="http://internal-schedule-center.weimiaocaishang.com"
spzx_host="http://internal-product-center.weimiaocaishang.com"#商品中心
xby_host="http://m2.weimiaocaishang.com"
live_host = "http://internal-live-api.weimiaocaishang.com"
analysis_host="https://traffic-dashboard.weimiaocaishang.com"
gxpt_bk_host = 'http://open.weimiaocaishang.com/api/wm-sharing-platform'
gxpt_fb_host = 'https://splatform.weimiaochina.com/api'
sjy_host_homework = "http://internal-practice-backend.weimiaocaishang.com"
marketing_host='http://marketing-tools.weimiaocaishang.com'
fission_host = "https://m.tougebiao.cn"
financial_host = "http://financial-dashboard.weimiaocaishang.com"
referer_host = 'https://m.jingmeizhengxingmeirongyiyuan.com'
dushuhui_bk_host = "http://cswxapi.weimiaocaishang.com"
dushuhui_bjnews_host = 'http://csapi.weimiaocaishang.com'
#线上账户密码
user = "ceshi5"
passwd = "HbCd98VKEciraw"
wm_user = '{%22sn%22:%22%E6%B5%8B%E8%AF%95%E4%BA%91%E4%BF%9D%22%2C%22cn%22:%22ceshi5%22%2C%22mail%22:%22ceshi5@weimiao.cn%22%2C%22token%22:%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJTU08uSU5GUkEuV0VJTUlBTy5DT00iLCJleHAiOjE2MDgwMTkzMzQsImlhdCI6MTYwNzkzMjkzNCwidXNlcmlkIjoxMDAwMDAzMjIwLCJ1c2VybmFtZSI6ImNlc2hpNSJ9.u3zMu2c99waF2Z_H1QXY6gmR02BEd28HKed-g8X-b2s%22}'
# 线上环境数据库配置
db_order_promotion_host = "rr-2ze43m738r06yl88f.mysql.rds.aliyuncs.com"
db_goods_host = "rm-2ze96jaff4g38q532.mysql.rds.aliyuncs.com"
db_auth_host = "rm-2zev8x83n634f0d83.mysql.rds.aliyuncs.com"
db_dk_live_host = "rm-2ze3uodhd0ns20a6o.mysql.rds.aliyuncs.com"
db_xby_live_host = "rm-2ze38f7730f64835d.mysql.rds.aliyuncs.com"
db_weimiao_host = "rr-2ze9r2819w7xy6ov0.mysql.rds.aliyuncs.com"
db_class_host = "rr-2zekxytwgn9cubfcj.mysql.rds.aliyuncs.com"
db_user_host = "rr-2zekasfv3qz4532ww.mysql.rds.aliyuncs.com"
db_infoflow_host = "rm-2ze06je8gwsiq1o95.mysql.rds.aliyuncs.com"
db_sharing_host = "rr-2ze2biec4ixiv0dg2.mysql.rds.aliyuncs.com"
db_subject_host = "rm-2ze86hrnr1668p5b7.mysql.rds.aliyuncs.com"
db_infoflow_host = "rm-2ze06je8gwsiq1o95.mysql.rds.aliyuncs.com"
db_dushuhui_host = "rr-2zeoq60105c4n5lbk.mysql.rds.aliyuncs.com"
db_port = int(3306)
db_user = "auto_testuser"
db_passwd = "HbCd98VKEcirawYG"
#xby线上参数
#用户mid
mid = [1597379883522974, 1598250159951837]
#直播房间号
room_id = '20102641970399'
#openId
openId = 'o4V6n0sCUOfJoWYhcZH3WeUO7awI'
sharing_platform_cookie="UZcFy3nrDQJ7avhBx0zAyoRvCOkN68CCtqr6G9jX"

#大课直播房间号
class_room_id = '20092877761940'
#各平台app_key:
wm_class = 'f8sYE88t07Gzqw8BHxBBsAg76sLTRJLB'
xiaobai = 'bvWXsNllkr20DHqv3IjMd2yAVd9JslLr'
opening = 'XC2mPdhcjZpn5Bhc0XoMbRvJKGhRtiIW'

#dushuhui
dushuhui="1d75c676ee0bf70a209e9789e28d8959"
dushuhui_h5="PHPSESSID=vnclgn7akbib9k2kh1li5afosh"

#测试报告配置
report_ip = "172.17.208.18:8081"

