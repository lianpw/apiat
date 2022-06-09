# -*- coding: utf-8 -*-
# Auth:guoxiaohua
# Time:2020/11/9 16:40
import pytest,requests
from config import  config
from utils import login,baseData,stamp,aes

#财务后台
class TestFinancial(object):
	def setup_class(self):
		token = login.login()
		self.start_time = stamp.timeday(0)
		self.end_time = stamp.timeday(+1)
		self.header = config.header
		self.header["h-app-id"] = "100"
		self.header["Cookie"] = 'mid=10006787'

	#小白营报大课(微信/支付宝/京东)每天支付
	@pytest.mark.getAPI
	def test_financialApi_xbDk(self):
		Url = config.xby_host + '/Home/FinancialApi/xbDk'
		data = aes.encrypt('{"time_start":"2020-07-01 00:00:00","time_end":"2020-07-09 00:00:00"}')
		res = requests.get(url=Url, data=data, headers=self.header)
		res_data = aes.decrypt(res.text)
		# print('小白营报大课(微信/支付宝/京东)每天支付:',res_data)
		assert res_data['code'] == 20000


	#小白营报大课(淘宝 / 对公转账 / 国外付款)每天支付
	@pytest.mark.getAPI
	def test_financialApi_xbDkOther(self):
		Url = config.xby_host + '/Home/FinancialApi/xbDkOther'
		data = aes.encrypt('{"time_start":"2020-07-01 00:00:00","time_end":"2020-07-09 00:00:00"}')
		res = requests.get(url=Url, data=data, headers=self.header)
		res_data = aes.decrypt(res.text)
		# print('小白营报大课(淘宝 / 对公转账 / 国外付款)每天支付:',res_data)
		assert res_data['code'] == 20000
	# #
	#大课每天退款    /Home/FinancialApi/refundDk
	@pytest.mark.getAPI
	def test_financialApi_refundDk(self):
		Url = config.xby_host + '/Home/FinancialApi/refundDk'
		data = aes.encrypt('{"time_start":"2020-07-01 00:00:00","time_end":"2020-07-09 00:00:00"}')
		res = requests.get(url=Url, data=data, headers=self.header)
		res_data = aes.decrypt(res.text)
		# print('大课每天退款:',res_data)
		assert res_data['code'] == 20000
	#
	#小白营 + 信息流每天支付
	@pytest.mark.getAPI
	def test_financialApi_merchant12(self):
		Url = config.xby_host + '/Home/FinancialApi/merchant12'
		data = aes.encrypt('{"time_start":"2020-07-01 00:00:00","time_end":"2020-07-09 00:00:00"}')
		res = requests.get(url=Url, data=data, headers=self.header)
		res_data = aes.decrypt(res.text)
		# print('小白营 + 信息流每天支付:', res_data)
		assert res_data['code'] == 20000
	#
	#小白营5元红包
	@pytest.mark.getAPI
	def test_financialApi_xb5Yuan(self):
		Url = config.xby_host + '/Home/FinancialApi/xb5Yuan'
		data = aes.encrypt('{"time_start":"2020-07-01 00:00:00","time_end":"2020-07-09 00:00:00"}')
		res = requests.get(url=Url, data=data, headers=self.header)
		res_data = aes.decrypt(res.text)
		# print('小白营5元红包:',res_data)
		assert res_data['code'] == 20000

if __name__ == '__main__':
	pytest.main(["-s", "test_server_financial.py"])