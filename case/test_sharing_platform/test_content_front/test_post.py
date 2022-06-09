#coding:utf-8
#author by lianpengwei

import pytest
import requests
from config import config
from utils import login
from utils.mysql import mysqldb

mydb = mysqldb()


class TestPost(object):
    order_no = None

    def setup_class(self):
        token = login.sharing_platform_login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "laravel_session=" + token

    # 参加活动
    @pytest.mark.postAPI
    def test_activity_participate(self):
        url = config.gxpt_fb_host + '/activity/participate'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        res = requests.post(url, headers=self.header)
        assert res.json()['code'] == 0 or res.json()['code'] == 904

    # 订阅或取消订阅
    @pytest.mark.postAPI
    def test_category_subscribe(self):
        url = config.gxpt_fb_host + '/category/subscribe'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'is_subscribed': 0
        }
        res = requests.post(url, headers=self.header, data=data)
        assert res.json()['code'] == 0

    # 点赞(或者取消)
    @pytest.mark.postAPI
    def test_article_thumbsup(self):
        url = config.gxpt_fb_host + '/article/thumbsup'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        cate_id = mydb.fetch('wm_product_center.wp_category', 'id', conditions={'category_name': '企业分析'}, limitd=1)['msg'][0][0]
        product_no = mydb.fetch('wm_product_center.wp_product', 'product_num', relation='and', conditions={'status': 1, 'category_id': cate_id}, limitd=10)['msg'][9][0]
        data = {
            'thumbsup_status': 0,
            'product_no': product_no
        }
        res = requests.post(url, headers=self.header, data=data)
        assert res.json()['code'] == 0

    # 下单并支付
    @pytest.mark.postAPI
    def test_order_create(self):
        url = config.gxpt_fb_host + '/order/create'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        cate_id = mydb.fetch('wm_product_center.wp_category', 'id', conditions={'category_name': '企业分析'}, limitd=1)['msg'][0][0]
        product_no = mydb.fetch('wm_product_center.wp_product', 'product_num', relation='and', conditions={'status': 1, 'category_id': cate_id}, limitd=10)['msg'][9][0]
        data = {
            'product_no': product_no
        }
        res = requests.post(url, headers=self.header, data=data)
        TestPost.order_no = res.json().get('data').get('order_no')
        assert res.json()['code'] == 0 or res.json()['code'] == 503

    # 支付指定订单
    @pytest.mark.postAPI
    def test_order_pay(self):
        url = config.gxpt_fb_host + '/order/pay'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'order_no': self.order_no
        }
        res = requests.post(url, headers=self.header, data=data)
        assert res.json()['code'] == 0

    # 取消订单
    @pytest.mark.postAPI
    def test_order_cancel(self):
        url = config.gxpt_fb_host + '/order/cancel'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'order_no': self.order_no
        }
        res = requests.post(url, headers=self.header, data=data)
        assert res.json()['code'] == 0

    # 计算优惠后价格
    @pytest.mark.postAPI
    def test_coupon_calculate(self):
        cate_id = mydb.fetch('wm_product_center.wp_category', 'id', conditions={'category_name': '企业分析'}, limitd=1)['msg'][0][0]
        product_no = mydb.exeSQL('select product_num from wm_product_center.wp_product where status = 1 and category_id = 15 and price > 0').get('msg')[3][0]
        url = config.gxpt_fb_host + '/coupon/calculate'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'product_no': product_no,
            'coupon_code': 'g6qqoADw3poPn',
            'coupon_type': 1
        }
        res = requests.post(url, headers=self.header, data=data)
        assert res.json()['code'] == 0

    # 退款
    @pytest.mark.postAPI
    def test_order_refund(self):
        url = config.gxpt_fb_host + '/order/refund'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'order_no': '123'
        }
        res = requests.post(url, headers=self.header, data=data)
        assert res.json()['code'] == 0 or res.json()['code'] == 501


if __name__ == '__main__':
    pytest.main(['-s', 'test_post.py'])