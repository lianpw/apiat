# -*- coding: utf-8 -*-
# Auth:guoxiaohua
# Time:2020/12/19 15:46

# 裂变项目   get请求
import requests,pytest,json
from config import config
from utils import stamp,mysql

class TestFission(object):
	def setup_class(self):
		self.start_time = stamp.timeday(0)
		self.end_time = stamp.timeday(+1)
		self.header = config.header
		self.header['referer'] = config.referer_host
		self.mid = mysql.mysqldb().fetch(table='wm_order_center.t_order', col='member_id', relation='',
										 conditions={"order_status": 2}, limitd=1)['msg'][0][0]

	# 海报分享页面   /api/operating/posterShow
	@pytest.mark.getAPI
	def test_poster_show(self):
		Url = config.fission_host + '/api/operating/posterShow'
		params = {
			"mid":self.mid
			# "referer":'https://test-m3.weimiaoshangxueyuan.cn/'
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('海报分享页面', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002 or res.json()['code'] == 10003

	#获取用户基本信息
	@pytest.mark.getAPI
	def test_getUserInfo(self):
		Url = config.fission_host + '/api/index/getUserInfo'
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('获取用户基本信息', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	# 微信分享
	@pytest.mark.getAPI
	def test_wechatShare(self):
		Url = config.fission_host + '/api/index/wechatShare'
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('微信分享', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	# 获取微信分享地址
	@pytest.mark.getAPI
	def test_getShareUrl(self):
		Url = config.fission_host + '/api/index/getShareUrl'
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('获取微信分享地址', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	# 首次分享
	@pytest.mark.getAPI
	def test_getShareUrl(self):
		Url = config.fission_host + '/api/index/firstShare'
		header = {
			"Content - Type":"application/x-www-form-urlencoded",
		}
		params = {
			"mid":self.mid
		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('首次分享', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	# 领书页面
	@pytest.mark.getAPI
	def test_addressInfo(self):
		Url = config.fission_host + '/api/operating/addressInfo'
		header = {
			"Content - Type": "application/x-www-form-urlencoded",
		}
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('领书页面', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	# 活动首页
	@pytest.mark.getAPI
	def test_operating_index(self):
		Url = config.fission_host + '/api/operating/index'
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('活动首页', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	# #获取邀请好友人数及头像
	#开发确认已废除
	# @pytest.mark.getAPI
	# def test_invite_images(self):
	# 	Url = config.fission_host + '/api/operating/inviteImages'
	# 	header = {
	# 		"Content - Type": "application/x-www-form-urlencoded",
	# 	}
	# 	params = {
	# 		"show_num":5,
	# 		"mid": self.mid
	#
	# 	}
	# 	res = requests.get(url=Url, headers=header,params=params)
	# 	# print('获取邀请好友人数及头像', res.json())
	# 	assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	#获取邀请好友详情
	@pytest.mark.getAPI
	def test_invite_detail(self):
		Url = config.fission_host + '/api/operating/inviteDetail'
		header = {
			"Content - Type": "application/x-www-form-urlencoded",
		}
		params = {
			"status":1,
			"mid": self.mid

		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('获取邀请好友详情', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	#钱包首页
	@pytest.mark.getAPI
	def test_invite_detail(self):
		Url = config.fission_host + '/api/operating/walletList'
		header = {
			"Content - Type": "application/x-www-form-urlencoded",
		}
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('钱包首页', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	#钱包提现记录
	@pytest.mark.getAPI
	def test_withdraw_list(self):
		Url = config.fission_host + '/api/operating/withdrawList'
		header = {
			"Content - Type": "application/x-www-form-urlencoded",
		}
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('钱包提现记录', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	#好友学习进度
	@pytest.mark.getAPI
	def test_progress(self):
		Url = config.fission_host + '/api/operating/friendLearningProgress'
		header = {
			"Content - Type": "application/x-www-form-urlencoded",
		}
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('好友学习进度', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002
	#
	#报名页
	@pytest.mark.getAPI
	def test_index(self):
		Url = config.fission_host + '/api/xiaobai/index'
		header = {
			"Content - Type": "application/x-www-form-urlencoded",
		}
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=header,params=params)
		# print('报名页', res.json())
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

	#微信支付
	@pytest.mark.getAPI
	def test_jsapi(self):
		Url = config.fission_host + '/api/xiaobai/jsapi?mid=1609747790887781'
		# header = {
		# 	"Content - Type": "application/x-www-form-urlencoded",
		# 	"host": config.referer_host
		# }

		res = requests.get(url=Url)
		assert res.json()['code'] == 20000 or res.json()['code'] == 10002

if __name__ == '__main__':
	pytest.main(["-s", "test_fission_get.py"])
