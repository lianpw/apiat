#coding:utf-8
#author by wangyunbao
import time

import pytest,requests
from config import config
from utils import login,baseData,mysql


class TestBackendOrder(object):

    def setup_class(self):
        # self.refundOrderNO=baseData.refundOrder_refund()["data"]["orderNo"]
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    # #订单列表查询
    # @pytest.mark.getAPI
    # def test_metadata_order_list(self):
    #     Url = config.host +"/api/order/metadata/order/list"
    #     body = {
    #         "appId":self.appid,
    #         "memberId":11,
    #         "orderNo":"",
    #         "orderType":"",
    #         "orderStatus":"",
    #         "infoflowChannel":"",
    #         "createrStartTime":"",
    #         "createrEndTime":"",
    #         "pageNum":1,
    #         "pageSize":20
    #     }
    #     res = requests.get(url=Url,params=body,headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # #订单退款列表查询
    # @pytest.mark.getAPI
    # def test_metadata_refundOrder_list(self):
    #     Url = config.host +"/api/order/metadata/refundOrder/list"
    #     body = {
    #         "appId":self.appid,
    #         "orderNo":self.refundOrderNO,
    #         "orderType":"",
    #         "orderStatus":"",
    #         "createrStartTime":"",
    #         "createrEndTime":"",
    #         "pageNum":1,
    #         "pageSize":20
    #     }
    #     res = requests.get(url=Url,params=body,headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # #退款订单详情
    # @pytest.mark.getAPI
    # def test_metadata_refundOrder_info(self):
    #
    #     Url = config.host +"/api/order/service/refundOrder/queryRefundOrderDetail"
    #     body = {
    #         "appId":self.appid,
    #         "orderNo":self.refundOrderNO
    #     }
    #     res = requests.get(url=Url,params=body,headers=self.header)
    #     baseData.refundOrder_updateRefundOrderInfo(refundorder=self.refundOrderNO)
    #     assert res.json()['data']["refundOrderDetailList"][0]["orderNo"] == self.refundOrderNO
    #
    # #订单详情
    # @pytest.mark.getAPI
    # def test_metadata_order_info(self):
    #     #print(baseData.create_order()["data"]["orderInfoList"][0]["order"]["orderNo"])
    #     Url = config.host + "/api/order/metadata/order/info"
    #     body = {
    #         "appId": self.appid,
    #         "orderNo": baseData.create_order()["data"]["orderInfoList"][0]["order"]["orderNo"]
    #     }
    #     res = requests.get(url=Url, params=body, headers=self.header)
    #     assert res.json()['code'] == 0
    #后端-订单列表查询（多条件查询带分页）
    @pytest.mark.getAPI
    def test_order_list(self):
        Url = config.host + "/api/order/metadata/order/list?appId=%s&page=1" % ("100")
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #后端-订单退款列表查询
    @pytest.mark.getAPI
    def test_query_refundorder_list(self):
        data = mysql.mysqldb().fetch(col='app_id,order_no', relation='', table='wm_order_center.t_refund_order')['msg'][0]
        Url = config.host + "/api/order/metadata/refundOrder/list?appId=%s" % (data[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #后端-退款订单详情
    @pytest.mark.getAPI
    def test_query_refundorder_info(self):
        data = mysql.mysqldb().fetch(col='app_id,order_no', relation='', table='wm_order_center.t_refund_order')['msg'][0]
        Url = config.host + "/api/order/metadata/refundOrder/info?appId=%s&orderNo=%s" % (data[0],data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #后端-订单详情
    @pytest.mark.getAPI
    def test_query_order_info(self):
        data = mysql.mysqldb().fetch(col='app_id,order_no', relation='', table='wm_order_center.t_order')['msg'][0]
        Url = config.host + "/api/order/metadata/order/info?appId=%s&orderNo=%s" % (data[0],data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

if __name__=="__main__":
    pytest.main(["-s","test_backend_order.py"])