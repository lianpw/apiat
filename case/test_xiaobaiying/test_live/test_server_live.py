# # -*- coding: utf-8 -*-
# # Auth:guoxiaohua
# # Time:2020/11/5 12:50
#
# #微淼-小白营/直播项目/后端业务
#
import requests,pytest,json
from config import config
from utils import stamp,mysql
# import requests
#
class TestServerLive(object):
	mobile = '18613836301'
	mobile_old = '13683645980'
	# 查找老师
	# res = mysql.mysqldb().fetch(table='wm_live.mh_live_teacher',col='auth_uid , wx_nickname, real_name,type,auth_username,qrcode,class_num,mid,employee_id',relation='and', conditions={"status": 1}, limitd=1)
	# #查找班级
	# res_class = mysql.mysqldb().fetch(table='wm_live.mh_live_class',col='id',relation='and', conditions={"status": 1}, limitd=1)
	def setup_class(self):
		self.start_time = stamp.timeday(0)
		self.end_time = stamp.timeday(+1)
		self.header = config.header
		self.header["Cookie"] = 'mid=10006787'

# 直播admin---------------------------------------------------------------------------------------------------------------------------
	#直播admin-老师列表
	@pytest.mark.getAPI
	def test_teacher_list(self):
		Url = config.live_host + '/api/admin/teacher/list?page=%d&page_size=%d' %(1,10)
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 200

	#直播admin-拉取指定用户的财务流水
	@pytest.mark.getAPI
	def test_query_orderList(self):
		mid = mysql.mysqldb().fetch(table='wm_live.mh_live_fineorder', col='mid', relation='and', conditions={"pay_status": 1}, limitd=1)
		Url = config.live_host + '/api/live/finance/queryOrderList?mid=%d' % (mid['msg'][0])
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 0 or res.json()['code'] == 360033

	#直播admin-批量获取总支付价格
	@pytest.mark.getAPI
	def test_totalprice_batch(self):
		mids= mysql.mysqldb().fetch(table='wm_live.mh_live_finance', col='mid', relation='and', conditions={"examine_status":2}, limitd=9)
		for i in mids['msg']:
			Url = config.live_host + '/api/live/finance_summary/totalprice_batch?mids[]=%d '%(i[0])
			res = requests.get(url=Url,headers=self.header)
			assert res.json()['code'] == 200


	# 直播admin-学员作业数据
	@pytest.mark.getAPI
	def test_student_list(self):
		res = mysql.mysqldb().fetch(table='wm_live.mh_live_class',col='id',relation='and', conditions={"status": 1}, limitd=1)
		Url = config.live_host + '/api/admin/work/student_list'
		data = {
			"class_id": res['msg'][0][0],
			"page": 1,
			"page_size": 20
		}
		res = requests.get(url=Url, headers=self.header, params=data)
		assert res.json()['code'] == 200

	# 直播admin-作业数据
	@pytest.mark.getAPI
	def test_work_list(self):
		period_id = mysql.mysqldb().fetch(table='wm_live.mh_live_period_room_ids', col='period_id', relation='and', conditions={ "id": 10}, limitd=1)
		Url = config.live_host + '/api/admin/work/list'
		data = {
			"periods_id":period_id['msg'][0][0],
		}
		res = requests.get(url=Url, headers=self.header, params=data)
		assert res.json()['code'] == 200

	# #直播admin-期数数据
	#找不到接口，可能已删除拆分
	# @pytest.mark.getAPI
	# def test_room_list(self):
	# 	# res = mysql.mysqldb().fetch(table='wm_live.mh_live_assistant', col='period_id,type', relation='and',
	# 	# 							conditions={"is_deleted": 0}, limitd=1)
	# 	Url = config.live_host + '/api/admin/room/list'
	# 	data = {
	# 		"period_id": 6 ,#res['msg'][0][0]
	# 		"class_id": 2 #self.res_class['msg'][0][0]
	# 	}
	#
	# 	res = requests.get(url=Url, headers=self.header, params=data)
	# 	print(res.text)
	# 	assert res.json()['code'] == 200

	# 直播admin-获取发送信息按钮数据
	@pytest.mark.getAPI
	def test_get_bottoninfo(self):
		res = mysql.mysqldb().fetch(table='weimiao.mh_wxorder', col='qid,bid', relation='and',conditions={"otype": 2}, limitd=1)
		Url = config.live_host + '/api/admin/class/student/getBottonInfo'
		data = {
			"qid": res['msg'][0][0],
			"bid": res['msg'][0][0]
		}
		res = requests.get(url=Url, headers=self.header, params=data)
		assert res.json()['code'] == 200

	# # 直播admin-获取标准班级人数
	@pytest.mark.getAPI
	def test_get_real_num(self):
		Url = config.live_host + '/api/admin/teacher/real_num'
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 200

	# # 直播admin-获取学员统计实时数据->观看人数、进入人数、离开人数
	#还未上线，等上线后再取消注释20201214
	# @pytest.mark.getAPI
	# def test_get_real_time_data(self):
	# 	res = mysql.mysqldb().fetch(table='wm_live.mh_live_period_chapter', col='id,period_id', relation='and',conditions={"status": 1}, limitd=1)
	# 	Url = config.live_host + '/api/admin/room/real_time_data'
	# 	data = {
	# 		"period_id": res['msg'][0][1],
	# 		"chapter_id": res['msg'][0][0],
	# 		"start_time": self.start_time,
	# 		"end_time": self.end_time
	# 	}
	# 	res = requests.get(url=Url, headers=self.header, params=data)
	# 	print('获取发送信息按钮数据 :', res.json())
	# 	assert res.json()['code'] == 200

	# 直播admin-创建老师
	@pytest.mark.postAPI
	def test_add_techer(self):
		Url = config.live_host + '/api/admin/teacher/add'
		header = {
			"User-Agent": "PostmanRuntime/7.26.3",
			"Content-Type" : "application/x-www-form-urlencoded"
		}
		data = {
			"auth_uid":self.res['msg'][0][0],
			"wx_nickname":self.res['msg'][0][1],
			"real_name":self.res['msg'][0][2],
			"type":self.res['msg'][0][3],
			"auth_username":self.res['msg'][0][4],
			"qrcode":self.res['msg'][0][5],
			"class_num" :self.res['msg'][0][6],
			"mid":self.res['msg'][0][7],
			"employee_id":self.res['msg'][0][8],
			"wechat_id":123456
		}
		res = requests.post(url=Url, headers=header,data=data)
		assert res.json()['code'] == 200 or res.json()['code'] == 390001  or res.json()['code'] == 310001

	# 直播admin-修改老师
	@pytest.mark.postAPI
	def test_edit_teacher(self):
		Url = config.live_host + '/api/admin/teacher/edit'
		header = {
			"User-Agent": "PostmanRuntime/7.26.3",
			"Content-Type" : "application/x-www-form-urlencoded"
		}
		data = {
			"auth_uid":self.res['msg'][0][0],
			"wx_nickname":self.res['msg'][0][1],
			"real_name":self.res['msg'][0][2],
			"type":self.res['msg'][0][3],
			"auth_username":self.res['msg'][0][4],
			"qrcode":self.res['msg'][0][5],
			"class_num" :self.res['msg'][0][6],
			"mid":self.res['msg'][0][7],
			"employee_id":self.res['msg'][0][8]
		}
		res = requests.post(url=Url, headers=header,data=data)
		assert res.json()['code'] == 200 or  res.json()['code'] == 390001 or res.json()['code'] == 310002

	# 直播admin-分班管理-预选
	@pytest.mark.postAPI
	def test_distribute_class(self):
		# 查找班级学员
		res = mysql.mysqldb().fetch(table='wm_live.mh_live_order',col='mid',relation='and', conditions={"order_status": 2}, limitd=1)
		Url = config.live_host + '/api/admin/bigcourse/class/distribute'
		payload = "{\"mobile\":\"18313836301\",\"mobile_old\":\"\",\"prefer_time\":1,\"remark\":\"\",\"mid\":1597322841487541}"
		res = requests.post(url=Url, headers=self.header, data=payload)
		assert res.json()['code'] == 200 or  res.json()['code'] == 10001 or res.json()['code'] == 360012


	# 直播admin-发送模板消息     /api/admin/class/student/sendMsg   有问题？？？？？？？？？？？？
	# @pytest.mark.getPOST
	# def test_sendmsg(self):
	# 	# 查找班级学员
	# 	mids= mysql.mysqldb().fetch(table='wm_live.mh_live_finance', col='mid', relation='and', conditions={"examine_status":2}, limitd=9)
	# 	# print(mids['msg'][0][0])
	# 	Url = config.live_host + '/api/admin/class/student/sendMsg'
	# 	header = {
	# 	 	"User-Agent": "PostmanRuntime/7.26.3",
	# 		"Content-Type":"application/json"
	# 			}
	# 	data = {
	# 		"bid": 405,
	# 		"qid": 1000000005,
	# 		"mids": [
	# 			mids['msg'][0][0]
	# 		],
	# 		"title": '5554',
	# 		"message_content":'要上课了'
	# 	}
	# 	res = requests.post(url=Url, headers=header, data=json.dumps(data))
	# 	print(res.text)
	# 	print('发送模板消息:', res.status_code)
		# assert res.json()['code'] == 200 or  res.json()['code'] == 10001 or res.json()['code'] == 360012

	# 获取学员点击商品次数详情与汇总收银台跳转次数接口
	@pytest.mark.postAPI
	def test_student_click_info(self):
		# 查找班级学员
		mid = mysql.mysqldb().fetch(table='wm_live.mh_live_order',col='mid',relation='and', conditions={"order_status": 2}, limitd=1)
		res = mysql.mysqldb().fetch(table='wm_live.mh_live_assistant', col='period_id,type', relation='', conditions={ "id": 501,"is_deleted":0}, limitd=1)
		Url = config.live_host + '/api/admin/room/student_click_info'
		header = {
			"User-Agent": "PostmanRuntime/7.26.3",
			"Content-Type": "application/x-www-form-urlencoded"
			}
		data = {
			"period_id":res['msg'][0][0],
			"mid": mid['msg'][0][0],
			"type":1
		}
		res = requests.post(url=Url, headers=header, data=data)
		assert res.json()['code'] == 200
#  ------------------------------------------------------------------------------------------------------------------------

# 内部服务---------------------------------------------------------------------------------------------------------------------------
	# 内部服务-获取0元直播报名列表
	@pytest.mark.getAPI
	def test_get_live_order_list(self):
		Url = config.live_host + '/api/live/user/get_live_order_list?start_time=%s&end_time=%s' %(self.start_time,self.end_time)
		res = requests.get(url=Url,headers=self.header)
		assert res.json()['code'] == 200
	#
	# 内部服务-获取小白营直播大课报名列表
	@pytest.mark.getAPI
	def test_summary_list(self):
		Url = config.live_host + '/api/live/finance/summary_list?start_time=%s&end_time=%s' %(self.start_time,self.end_time)
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 200


	# 内部服务-直播间生成回放
	@pytest.mark.getAPI
	def test_stop_and_trans_cloud_record(self):
		Url = config.live_host + '/api/live/periods/stop_and_trans_cloud_record?room_id=%s' %(1)
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 200 or res.json()['code'] == 390001

	# 内部服务-直播课程列表
	@pytest.mark.getAPI
	def test_get_course_list(self):
		mid = mysql.mysqldb().fetch(table='wm_subject.mh_work', col='mid', relation='and', conditions={"id": 26}, limitd=1)
		Url = config.live_host + '/api/live/course/list?mid=%d' % (mid['msg'][0][0])
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 200

	#内部服务-试卷详情
	@pytest.mark.getAPI
	def test_get_paper_info(self):
		mid = mysql.mysqldb().fetch(table='wm_subject.mh_work', col='mid,paper_id', relation='and', conditions={"id": 26},limitd=1)
		Url = config.live_host + '/api/live/paper/info?mid=%d&paper_id=%d' % (mid['msg'][0][0], mid['msg'][0][1])
		res = requests.get(url=Url, headers=self.header)
		assert res.json()['code'] == 200

	#内部服务-直播间状态
	@pytest.mark.getAPI
	def test_get_live_room_status(self):
		Url = config.live_host + '/api/live/live_room/status?room_id=%s' % (config.room_id)
		res = requests.get(url=Url, headers= self.header)
		assert res.json()['code'] == 200

	# 批量获取小白营直播大课学员信息     有问题，暂时忽略?????
	# @pytest.mark.getPOST
	# def test_batch_user_info(self):
	# 	# 查找班级学员
	# 	res_mid= mysql.mysqldb().fetch(table='wm_live.mh_live_finance', col='mid', relation='and', conditions={"examine_status":2}, limitd=9)
	# 	print(res_mid['msg'][3][0])
	# 	Url = config.live_host + '/api/live/user/batch_user_info'
	# 	data = {
	# 		"mids": [
	# 			res_mid['msg'][0][0],res_mid['msg'][3][0]
	# 		]
	# 	}
	# 	print(data)
	# 	res = requests.post(url=Url, headers=self.header, data=data)
	# 	print('批量获取小白营直播大课学员信息:', res.json())
		# assert res.json()['code'] == 200

	# 试卷提交
	@pytest.mark.postAPI
	def test_submit(self):
		# 查找班级学员
		res = mysql.mysqldb().fetch(table='wm_subject.mh_work', col='mid,paper_id,result', relation='and',conditions={"is_del":0},limitd=9)
		Url = config.live_host + '/api/live/paper/submit'
		data = {
			"mid":res['msg'][0][0],
			"paper_id":1,
			"answer_list":[
				{"seq": 1, "answer": "B"}, {"seq": 2, "answer": "C"},{"seq": 3, "answer": "C"},{"seq": 4, "answer": "C"},{"seq": 5, "answer": "C"}
			]
		}
		data = json.dumps(data)
		res = requests.post(url=Url, headers=self.header, data=data)
		assert res.json()['code'] == 200

	# 直播创建用户
	@pytest.mark.postAPI
	def test_create_user(self):
		# 查找班级学员
		res = mysql.mysqldb().fetch(table='wm_subject.mh_work', col='mid,paper_id,result', relation='and',conditions={"is_del":0},limitd=9)
		Url = config.live_host + '/api/live/user/create'
		header = {
			"User-Agent": "PostmanRuntime/7.26.3",
			"Content-Type": "application/x-www-form-urlencoded"
		}
		data = {
			"mid":res['msg'][0][0],
			"source":1
		}
		res = requests.post(url=Url, headers=header, data=data)
		assert res.json()['code'] == 200

	#点击上报接口   /api/live/data/report
	@pytest.mark.postAPI
	def test_create_user(self):
		# 查找班级学员
		res = mysql.mysqldb().fetch(table='wm_subject.mh_work', col='mid,paper_id,result', relation='and',conditions={"is_del":0},limitd=9)
		Url = config.live_host + '/api/live/data/report'
		data={"services_name":"livexby","header":{"device_no":0,"os":"IOS","client_ip":0,"tourist_id":0,"sdkVersion":"1.0.5"},"body":{"uid":1597199608009413,"openid":"oTAUPt_tO0L-tgl3oAO-dgalV5lE","unionid":"oDptewwKNrmfTiDB1PtorJPc1Jys","event":"chat-timeout","pre_page":0,"current_page":"/not-auth","module_ori":"xby-zb","module_part":"xby-zb-im-cs","event_time":1606968768536,"origin_channel":0,"visit_channel":0,"follow_channel":0,"version":0,"userstatus":0}}
		res = requests.post(url=Url, headers=self.header,data=data)
		assert res.json()['code'] == 200

if __name__ == '__main__':
	pytest.main(["-s", "test_server_live.py"])





