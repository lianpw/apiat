#coding:utf-8
#author by lianpengwei

import warnings
warnings.simplefilter('ignore', DeprecationWarning)

import pytest
import requests
from config import config
from utils import login
from utils.mysql import mysqldb

mydb = mysqldb()
cate_id = mydb.fetch('wm_product_center.wp_category', 'id', conditions={'category_name': '企业分析'}, limitd=1)['msg'][0][0]
product_no = mydb.fetch('wm_product_center.wp_product', 'product_num', relation='and', conditions={'status': 1, 'category_id': cate_id}, limitd=1)['msg'][0][0]


class TestOrdeerDiscountCouponPay(object):
    def setup_class(self):
        token = login.sharing_platform_login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "laravel_session=" + token

    # 兑换优惠券
    @pytest.mark.getAPI
    def test_coupon_exchange(self):
        url = config.gxpt_fb_host + '/coupon/exchange'
        data = {
            'coupon_code': 'oBzzo2Dw31onm1'
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0 or res.json()['code'] == 701

    # 下单前数据获取
    @pytest.mark.getAPI
    def test_order_before(self):
        url = config.gxpt_fb_host + '/order/before'
        data = {
            'product_no': product_no
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0

    # 优惠券列表
    @pytest.mark.getAPI
    def test_coupon_list(self):
        url = config.gxpt_fb_host + '/coupon/list'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == 0

    # 待支付订单列表
    @pytest.mark.getAPI
    def test_order_unpays(self):
        url = config.gxpt_fb_host + '/order/unpays'
        data = {
            'page': 1,
            'page_size': 1
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0

    # 我的已购
    @pytest.mark.getAPI
    def test_my_purchased(self):
        url = config.gxpt_fb_host + '/user/my/purchased'
        data = {
            "page": 1,
            "page_size": 1
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0
        return res.json().get('data').get('list')[0].get('order_no')

    # 已购订单详情
    @pytest.mark.getAPI
    def test_order_info(self):
        url = config.gxpt_fb_host + '/order/info'
        data = {
            'order_no': self.test_my_purchased()
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == 0




if __name__ == '__main__':
    pytest.main(['-s', 'test_order_discount_coupon_pay.py'])