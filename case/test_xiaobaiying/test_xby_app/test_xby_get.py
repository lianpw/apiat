# -*- coding: utf-8 -*-
# Auth:guoxiaohua
# Time:2020/12/28 18:35

import requests,pytest,json
from config import config
from utils import stamp,mysql

class TestFission(object):
	def setup_class(self):
		self.start_time = stamp.timeday(0)
		self.end_time = stamp.timeday(+1)
		self.header = config.header
		self.header['referer'] = config.referer_host
		self.mid = mysql.mysqldb().fetch(table='wm_order_center.t_order',col='member_id',relation='', conditions={"order_status": 2}, limitd=1)['msg'][0][0]


	#取得小白营商品及价格
	@pytest.mark.getAPI
	def test_get_productInfo(self):
		Url = config.xby_host + '/api/app/productInfo'
		params = {
			"mid": self.mid
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('取得小白营商品及价格', res.json())
		assert res.json()['status'] == 20000

	#取得支付状态
	@pytest.mark.getAPI
	def test_get_payStatus(self):
		res_parameter = mysql.mysqldb().fetch(table='wm_order_center.t_order_payment_detail', col='payment_platform_no,order_no', relation='and',conditions={"order_status": 2}, limitd=1)
		Url = config.xby_host + '/api/app/payStatus'
		params = {
			"mid":self.mid,
			"order_num":res_parameter['msg'][0][0],
			"order_sn":res_parameter['msg'][0][1]
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('取得支付状态', res.json())
		assert res.json()['status'] == 20000


	#取得用户信息
	@pytest.mark.getAPI
	def test_get_user(self):
		Url = config.xby_host + '/api/app/user'
		params = {
			"mid":self.mid
		}
		res = requests.get(url=Url, headers=self.header,params=params)
		# print('取得用户信息', res.json())
		assert res.json()['status'] == 20000

	#支持的商品列表
	@pytest.mark.getAPI
	def test_productSnList(self):
		Url = config.xby_host + '/api/app/productSnList'
		res = requests.get(url=Url, headers=self.header)
		# print('支持的商品列表', res.json())
		assert res.json()['status'] == 20000


if __name__ == '__main__':
	pytest.main(["-s", "test_xby_get.py"])