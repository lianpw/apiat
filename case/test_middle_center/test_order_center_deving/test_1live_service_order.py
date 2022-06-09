#coding:utf-8
#author by wangyunbao+yangxi01

import pytest,requests,json,random
from config import config
from utils import login,baseData,mysql
mysqld = mysql.mysqldb()

class TestOrder(object):

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"

    #订单列表查询（人维度）随机100个人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList1(self):
        memberId = mysqld.fetch(table="wm_order_center.t_order",col="distinct(member_id)",limitd=100)['msg']
        temp = random.sample(memberId,random.randint(1,100))
        memberIds = ""
        for m in temp:
            memberIds+=m[0]+","
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberIds[0:-1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #订单列表查询（人维度）人+商品
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_goodsNo(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order",col="distinct(goods_no)",limitd=100)['msg']
        memberId = mysqld.fetch(table="wm_order_center.t_order", col="member_id", conditions={"goods_no": goodsNo[0][0]},
                     limitd=1)['msg'][0][0]
        temp = random.sample(goodsNo,random.randint(1,100))
        goodsNos = ""
        for m in temp:
            goodsNos+=m[0]+","
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&goodsNo=%s" % (memberId,goodsNos)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    # 订单列表查询（人维度）不带人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_nomemberid(self):
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8008


    # 订单列表查询（人维度）带假人+假商品
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_nomemberid(self):
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=3124674432454&goodsNo=31254568934675"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

    #订单列表查询（人维度）100个人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList2(self):
        memberIds = mysqld.fetch(table="wm_order_center.t_order",col="distinct(member_id)",relation="",limitd=100)['msg']
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberIds,)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #订单列表查询（人维度）101个人
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList3(self):
        memberIds = mysqld.fetch(table="wm_order_center.t_order",col="distinct(member_id)",relation="",limitd=101)['msg']
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberIds,)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8019


    #订单列表查询（人维度）人+订单状态
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList4(self):
        memberId = mysqld.fetch(table="wm_order_center.t_order", col="member_id", relation="", limitd=1)[
            'msg'][0][0]
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&orderStatus=1" % (memberId)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #订单列表查询（人维度）商品
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_ogoodsNo(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order",col="distinct(goods_no)",relation="",limitd=1)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?goodsNo=%s" % (goodsNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 8008


    # 订单列表查询（人维度）人+商品+订单状态
    @pytest.mark.getAPI
    def test_order_queryMemberIdOrderList_All(self):
        goodsNo = mysqld.fetch(table="wm_order_center.t_order", col="distinct(goods_no)", relation="", limitd=1)['msg'][
            0][0]
        memberId = mysqld.fetch(table="wm_order_center.t_order", col="distinct(member_id)", conditions={"goods_no": goodsNo}, limitd=1)[
            'msg'][0][0]

        Url = config.host + "/api/order/service/order/queryMemberIdOrderList?memberId=%s&goodsNo=%s&orderStatus=0" % (
        memberId, goodsNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    # 查询订单详情（根据订单号查询detail）
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_detail(self):
        sql = 'select order_no from wm_order_center.t_order_payment_detail where order_no != "" limit 1'
        orderNo = mysql.mysqldb().exeSQL(sql)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList?orderNo=%s" % (orderNo)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    # 查询订单详情（根据订单号查询detail+mapping）
    @pytest.mark.getAPI
    def test_order_queryByOrderNoOrderList_detail_mapping(self):
        sql = 'select order_no from wm_order_center.t_order_payment_detail where order_no != "" limit 1'
        orderNo_detail = mysql.mysqldb().exeSQL(sql)['msg'][0][0]
        sql_m = 'select order_no from wm_order_center.t_order_mapping where order_no != "" limit 1'
        orderNo_mapping = mysql.mysqldb().exeSQL(sql_m)['msg'][0][0]
        Url = config.host + "/api/order/service/order/queryByOrderNoOrderList?orderNo=%s,%s" % (
        orderNo_detail, orderNo_mapping)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    # 查询订单详情（根据订单号查询mapping）
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
        orderBatchNo = mysqld.fetch(table="wm_order_center.t_order",col="order_batch_no",limitd=1)['msg'][0][0]
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
    pytest.main(["-s","test_1live_service_order.py"])