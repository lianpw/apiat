# -*- coding: utf-8 -*-
# Auth:guoxiaohua
# Time:2020/12/28 11:25

# 裂变项目   post请求
import requests,pytest,json
from config import config
from utils import stamp,mysql

class TestFission(object):
	def setup_class(self):
		self.start_time = stamp.timeday(0)
		self.end_time = stamp.timeday(+1)
		self.header = config.header
		self.header['referer'] = config.referer_host

	# #首次分享
	# @pytest.mark.postAPI
	# def test_firstShare(self):
	# 	Url = config.fission_host + '/api/index/firstShare'
	# 	header = {
	# 		"Content - Type": "application/x-www-form-urlencoded",
	# 	}
	# 	params = {
	# 		"mid": 1608351268831628
	# 	}
	# 	res = requests.post(url=Url, headers=header,data=params)
	# 	print('海报分享页面', res.json())
	# 	assert res.json()['code'] == 20000 or res.json()['code'] == 10002 or res.json()['code'] == 10003
	#
	#
	# #领书提交   code:20001  请勿重复提交，您已经提交过地址了。
	# @pytest.mark.postAPI
	# def test_postAddress(self):
	# 	Url = config.fission_host + '/api/operating/postAddress'
	# 	header = {
	# 		"Content - Type": "application/x-www-form-urlencoded",
	# 	}
	# 	params = {
	# 		"consignee":'郭',
	# 		"phone":15712968756,
	# 		"address":'北京市',
	# 		"mtype": 20210102,
	# 		"mid": 1608351268831628
	# 	}
	# 	res = requests.post(url=Url, headers=header,data=params)
	# 	print('领书提交', res.json())
	# 	assert res.json()['code'] == 20000 or res.json()['code'] == 10002 or res.json()['code'] == 10003  or res.json()['code'] == 20001
	#
	# #钱包提现操作
	# @pytest.mark.postAPI
	# def test_walletWithdraw(self):
	# 	Url = config.fission_host + '/api/operating/walletWithdraw'
	# 	header = {
	# 		"Content - Type": "application/x-www-form-urlencoded",
	# 	}
	# 	params = {
	# 		"mid": 1608351268831628
	# 	}
	# 	res = requests.post(url=Url, headers=header,data=params)
	# 	print('钱包提现操作', res.json())
	# 	assert res.json()['code'] == 20000 or res.json()['code'] == 10002 or res.json()['code'] == 10003  or res.json()['code'] == 20001
	#
	# #提醒用户学习
	# @pytest.mark.postAPI
	# def test_remindFriendLearn(self):
	# 	Url = config.fission_host + '/api/operating/remindFriendLearn'
	# 	header = {
	# 		"Content - Type": "application/x-www-form-urlencoded",
	# 	}
	# 	params = {
	# 		"mid": 1608351268831628,
	# 		"fmid":1608351268831628
	# 	}
	# 	res = requests.post(url=Url, headers=header,data=params)
	# 	print('提醒用户学习', res.json())
	# 	assert res.json()['code'] == 20000 or res.json()['code'] == 10002 or res.json()['code'] == 10003  or res.json()['code'] == 20001
	#
	#
	# #一次性弹窗确认
	# @pytest.mark.postAPI
	# def test_onceConfirm(self):
	# 	Url = config.fission_host + '/api/dialog/onceConfirm'
	# 	header = {
	# 		"Content - Type": "application/x-www-form-urlencoded",
	# 	}
	# 	params = {
	# 		"dialog_num": 2,
	# 		"mid": 1608351268831628
	# 	}
	# 	res = requests.post(url=Url, headers=header,data=params)
	# 	print('一次性弹窗确认', res.json())
	# 	assert res.json()['code'] == 20000 or res.json()['code'] == 10002 or res.json()['code'] == 10003 or res.json()['code'] == 20001


if __name__ == '__main__':
	pytest.main(["-s", "test_fission_post.py"])