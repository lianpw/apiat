# -*- coding: utf-8 -*-
# Auth:guoxiaohua
# Time:2020/12/29 18:50

import requests,pytest,json
from config import config
from utils import stamp,mysql

class TestFission(object):
	def setup_class(self):
		self.start_time = stamp.timeday(0)
		self.end_time = stamp.timeday(+1)
		self.header = config.header
		self.header['referer'] = config.referer_host
	#
	# #生成订单号并取得支付参数
	# @pytest.mark.postAPI
	# def test_get_productInfo(self):
	# 	Url = config.xby_host + '/api/app/pay'
	# 	header = {
	# 		"Content-Type": "application/x-www-form-urlencoded"
	# 	}
	# 	params = {
	# 		"mid": 1608351268831628,
	# 		"paytype":1,
	# 		"channel":9200
	# 	}
	# 	res = requests.post(url=Url, headers=header,data=params)
	# 	print('生成订单号并取得支付参数', res.json())
	# 	assert res.json()['status'] == 20000

if __name__ == '__main__':
	pytest.main(["-s", "test_xby_app_post.py"])
