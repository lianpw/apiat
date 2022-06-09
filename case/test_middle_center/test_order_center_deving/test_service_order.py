#coding:utf-8
#author by wangyunbao+yangxi01

import pytest,requests,json,random
from config import config
from utils import login,baseData,mysql
mysqld = mysql.mysqldb()

class TestOrder(object):

    def setup_class(self):
        token = login.login()
        self.appid = baseData.account_app_list()["data"][0]["appID"]
        self.header = config.header
        self.header["h-app-id"] = self.appid
        self.header["Cookie"] = "c_token="+token

    #业务端-订单详情
    # @pytest.mark.getAPI
    # def test_order_detail(self):
    #     orderNo=baseData.create_order()["data"]["orderInfoList"][0]["order"]["orderNo"]
    #     Url = config.host + "/api/order/service/order/queryOrderDetail"
    #     body = {
    #         "appId":self.appid,
    #         "orderNo":orderNo
    #     }
    #     res = requests.get(url=Url, params=body, headers=self.header)
    #     assert res.json()["data"]["orderNo"] == orderNo
    #
    # #业务端-订单详情
    # @pytest.mark.getAPI
    # def test_query_order_detail(self):
    #     data = mysql.mysqldb().fetch(col='app_id,order_no', relation='', table='wm_order_center.t_order')['msg'][0]
    #     Url = config.host + "/api/order/service/order/queryOrderDetail?appId=%s&orderNo=%s" % (data[0],data[1])
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 0

    #退款订单详情
    # @pytest.mark.getAPI
    # def test_refund_order_detail(self):
    #     refundOrderNO = baseData.refundOrder_refund()["data"]["orderNo"]
    #     Url = config.host + "/api/order/service/refundOrder/queryRefundOrderDetail"
    #     body = {
    #         "appId":self.appid,
    #         "orderNo":refundOrderNO
    #     }
    #     res = requests.get(url=Url, params=body, headers=self.header)
    #     baseData.refundOrder_updateRefundOrderInfo(refundorder=refundOrderNO)
    #     assert res.json()["data"]["refundOrderDetailList"][0]["orderNo"] == refundOrderNO
    #
    # #业务端-退款订单详情
    # @pytest.mark.getAPI
    # def test_query_refundorder_info(self):
    #     data = mysql.mysqldb().fetch(col='app_id,order_no,refund_no', relation='', table='wm_order_center.t_refund_order')['msg'][0]
    #     Url = config.host + "/api/order/service/refundOrder/queryRefundOrderDetail?appId=%s&orderNo=%s" % (data[0],data[1])
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 0

    # #业务端-待支付订单列表
    # @pytest.mark.getAPI
    # def test_queryUnpayOrderList(self):
    #     Url = config.host + "/api/order/service/order/queryUnpayOrderList"
    #     body = {
    #         "appId":self.appid,
    #         "memberId":11
    #     }
    #     res = requests.get(url=Url, params=body, headers=self.header)
    #     assert res.json()["code"] == 0

    # #业务端-待支付订单列表
    # @pytest.mark.getAPI
    # def test_queryUnpayOrderList(self):
    #     data = mysql.mysqldb().fetch(col='app_id,order_no,member_id', relation='', table='wm_order_center.t_order',conditions={"order_status":0})['msg'][0]
    #     Url = config.host + "/api/order/service/order/queryUnpayOrderList?appId=%s&orderNo=%s&memberId=%s&pageNum=1&pageSize=5" % (data[0],data[1],data[2])
    #     res = requests.get(url=Url, headers=self.header)
    #     assert res.json()["code"] == 0

    # #订单支付回调接口
    # @pytest.mark.postAPI
    # def test_updateOrderInfo(self):
    #     orderNo=baseData.create_order()["data"]
    #     Url = config.host + "/api/order/service/order/updateOrderInfo"
    #     body = {
    #         "orderNo": orderNo["orderInfoList"][0]["order"]["orderNo"],
    #         "memberId":orderNo["memberId"],
    #         "appId":orderNo["appId"],
    #         "paymentChannel": orderNo["channel"],
    #         "paymentAmount":orderNo["orderInfoList"][0]["order"]["orderAmount"],
    #         "paymentNo":"autotest1234567",
    #         "paymentWaterNo":"1111",
    #         "paymentPlatformNo":"autotest1234567",
    #         "remark":"autotest",
    #         "paymentTime":"2020-12-23 14:46:51",
    #         "paymentCompleteTime":"2020-12-23 14:46:51"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     print("test_updateOrderInfo:", res.json())
    #     assert res.json()["code"] == 0

    # 转单-未完成
    # @pytest.mark.postAPI
    # def test_refundOrder_transfer(self):
    #     Url = config.host + "/api/order/service/refundOrder/transfer"
    #     body = {
    #         "orderNo": baseData.create_order(),
    #         "memberId":"12"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    # 订单取消--未完成
    # @pytest.mark.postAPI
    # def test_refundOrder_cancel(self):
    #     Url = config.host + "/api/order/service/refundOrder/cancel"
    #     body = {
    #         "orderNo":baseData.create_order()
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=self.header)
    #     assert res.json()["code"] == 0

    #订单列表查询（人维度）随机100个人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList(self):
        memberId = mysqld.fetch(table="wm_order_center.t_order",col="distinct(member_id)",relation="",limitd=100)['msg']
        temp = random.sample(memberId,random.randint(1,100))
        memberIds = ""
        for m in temp:
            memberIds+=m[0]+","
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberIds[0:-1])
        res = requests.get(url=Url, headers=self.header)
        print(res.json())
        assert res.json()['code'] == 0

    #订单列表查询（人维度）人+商品
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_goodsNo(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order",col="distinct(goods_no)",relation="",limitd=100)['msg']
        memberId = mysqld.fetch(table="wm_order_center.t_order", col="distinct(member_id)", relation="goods_no ='goodsNo[0][0]'",
                     limitd=10)['msg'][9][0]
        temp = random.sample(goodsNo,random.randint(1,100))
        goodsNos = ""
        for m in temp:
            goodsNos+=m[0]+","
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&goodsNo=%s" % (memberId,goodsNos)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #订单列表查询（人维度）不带人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_nomemberid(self):
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8008

    #订单列表查询（人维度）带假人+假商品
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_nomemberid(self):
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=3124674432454&goodsNo=31254568934675"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #订单列表查询（人维度）101个人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList(self):
        memberIds = mysqld.fetch(table="wm_order_center.t_order",col="distinct(member_id)",relation="",limitd=101)['msg']
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberIds,)
        res = requests.get(url=Url, headers=self.header)
        print(res.json())
        assert res.json()['code'] == 8019


    #订单列表查询（人维度）人+订单状态
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList(self):
        memberId = mysqld.fetch(table="wm_order_center.t_order", col="distinct(member_id)", relation="", limitd=10)[
            'msg'][9][0]
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberId)
        res = requests.get(url=Url, headers=self.header)
        print(res.json())
        assert res.json()['code'] == 0

    #订单列表查询（人维度）商品
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_ogoodsNo(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order",col="distinct(goods_no)",relation="goods_no !=""",limitd=1)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?goodsNo=%s" % (goodsNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8008

    #订单列表查询（人维度）人+商品+订单状态
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_All(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order",col="distinct(goods_no)",relation="goods_no !=""",limitd=1)['msg'][0][0]
        memberId = mysqld.fetch(table="wm_order_center.t_order", col="distinct(member_id)", relation="goods_no ='goodsNo'", limitd=10)[
            'msg'][9][0]
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&goodsNo=%s&orderStatus=0" % (memberId,goodsNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #订单列表查询（人维度）人为0 +商品+订单状态0
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_0(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order",col="distinct(goods_no)",relation="",limitd=1)['msg'][0][0]
        memberId = 0
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&goodsNo=%s&orderStatus=0" % (memberId,goodsNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8008

    #查询订单详情（根据订单号查询detail）
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_detail(self):
        sql = 'select order_no from wm_order_center.t_order_payment_detail where order_no != "" limit 1'
        orderNo = mysql.mysqldb().exeSQL(sql)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList?orderNo=%s" % (orderNo)
        res = requests.get(url=Url, headers=self.header)
        print(res.json())
        assert res.json()['code'] == 0

    #查询订单详情（根据订单号查询detail+mapping）
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_detail_mapping(self):
        sql = 'select order_no from wm_order_center.t_order_payment_detail where order_no != "" limit 1'
        orderNo_detail = mysql.mysqldb().exeSQL(sql)['msg'][0][0]
        sql_m = 'select order_no from wm_order_center.t_order_mapping where order_no != "" limit 1'
        orderNo_mapping = mysql.mysqldb().exeSQL(sql_m)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList?orderNo=%s,%s" %(orderNo_detail,orderNo_mapping)
        res = requests.get(url=Url, headers=self.header)
        print(res.json())
        assert res.json()['code'] == 0


    #查询订单详情（根据订单号查询mapping）
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_mapping(self):
        sql = 'select order_no from wm_order_center.t_order_mapping where order_no != "" limit 1'
        orderNo = mysql.mysqldb().exeSQL(sql)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList?orderNo=%s" % (orderNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #查询订单详情（根据订单号查询）未传订单号
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_noorderNo(self):
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8014

    #查询订单详情（根据订单号查询）不存在订单号
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_worderNo(self):
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList?orderNo=0"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #查询订单详情（根据订单批次号查询）
    @pytest.mark.getAPI
    def test_order_queryByOrderBatchNoOrderList(self):
        orderBatchNo = mysqld.fetch(table="wm_order_center.t_order",col="order_batch_no",relation="order_batch_no !=""",limitd=1)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryByOrderBatchNoOrderList?orderBatchNo=%s" % (orderBatchNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #查询订单详情（根据订单批次号查询）未传批次号
    @pytest.mark.getAPI
    def test_order_queryByOrderBatchNoOrderList_nobatchNo(self):
        Url = config.host + "/api/order/service/order/queryByOrderBatchNoOrderList"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8013

    #查询订单详情（根据订单批次号查询）不存在批次号
    @pytest.mark.getAPI
    def test_order_queryByOrderBatchNoOrderList_wbatchNo(self):
        Url = config.host + "/api/order/service/order/queryByOrderBatchNoOrderList?orderNo=BT1328282570856779333"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8013




if __name__=="__main__":
    pytest.main(["-s","test_service_order.py"])