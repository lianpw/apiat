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


class TestOrder(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        self.header["Cookie"] = "c_token=" + token

    # 订单列表
    @pytest.mark.getAPI
    def test_order_list(self):
        url = config.gxpt_bk_host + '/admin/order/list'
        data = {
            "page": 1,
            "page_size": 1
        }
        res = requests.get(url, params=data, headers=self.header)
        assert res.json()['code'] == 0

    # 订单详情(只能用线上数据)
    @pytest.mark.getAPI
    def test_order_info(self):
        url = config.gxpt_bk_host + '/admin/order/info'
        order_no = mydb.exeSQL('select order_no from wm_order_center.t_order where app_id = "111" and order_status = 2 limit 10')['msg'][9][0]
        data = {
            "order_no": order_no
        }
        res = requests.get(url, params=data, headers=self.header)
        assert res.json()['code'] == 0

    # 退款列表
    @pytest.mark.getAPI
    def test_refund_list(self):
        url = config.gxpt_bk_host + '/admin/refund/list'
        data = {
                "page_size": 1,
                "size": 1
            }
        res = requests.get(url, params=data, headers=self.header)
        assert res.json()['code'] == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_order.py'])