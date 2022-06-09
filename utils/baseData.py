#coding:utf-8
#author by wangyunbao

import requests, json, os
from config import config
from utils import login,stamp,mysql

base_dir = os.path.abspath(".")
case_dir = base_dir+"\\case\\test_middle_center\\test_account_center"

mysqld = mysql.mysqldb()

# 获取用户授权的业务线
def account_app_list():
    token = login.login()
    header = config.header
    header["h-app-id"] = "100"
    header["Cookie"] = "c_token=" + token
    Url = config.host_open + "/api/auth/account/app/list"
    body = {}
    res = requests.post(url=Url, data=json.dumps(body), headers=header)
    return res.json()


#获取服务名称列表
def get_serviceName(caseKey):
    serviceList = {'case':'ALL','test_middle_center':'业务中台','order_center_deving':'订单中心','test_account_center':'账户中心'}
    try:
        return serviceList[caseKey]
    except Exception as err:
        return err

#订单新增
def create_order():
    goods_no = mysqld.fetch(table="wm_product_center.wp_product",col="product_num",relation="and",conditions={"status":1,"repeatable":1},limitd=1)
    Url = config.host + "/api/order/service/order/createOrder"
    body = {
        "appId":account_app_list()["data"][0]["appID"],
        "channel":"11",
        "promotionList":[{"promotionType":"","value":""}],
        "goods":[{
            "goodsNo":goods_no["msg"][0][0],
            "goodsNum":11,
            "goodsPrice":11,
            "orderSort":1
        }],
        "memberId":"11",
        "orderType":1,
        "phone":stamp.phoneNum(),
        "remark": "自动化测试的新增订单"
    }
    res = requests.post(url=Url, data=json.dumps(body), headers=header)
    return res.json()

# 退款单新增
def refundOrder_refund():
    refund = mysqld.fetch(table="wm_order_center.t_order", col="order_no,order_amount,order_batch_no,member_id", relation="and",
                            conditions={"order_status": 2}, limitd=1)["msg"][0]
    Url = config.host + "/api/order/service/refundOrder/refund"
    body = {
        "orderNo": refund[0],
        "orderBatchNo":refund[2],
        "refundAmount": refund[1],
        "reason":"auto test refund order",
        "appId":account_app_list()["data"][0]["appID"],
        "memberId":refund[3]
    }
    res = requests.post(url=Url, data=json.dumps(body), headers=header)
    return res.json()


def refundOrder_updateRefundOrderInfo(refundorder):
    refund = mysqld.fetch(table="wm_order_center.t_refund_order", col="app_id,refund_no,order_batch_no", relation="and",
                 conditions={"order_no":refundorder})["msg"][0]
    Url = config.host + "/api/order/service/refundOrder/updateRefundOrderInfo"
    body = {
        "appId":refund[0],
        "refundNo": refund[1],
        "orderBatchNo":refund[2],
        "refundStatus":5,
        "refundAmount": 1200,
        "refundChannel":1,
        "refundWaterNo":stamp.timeStamp(),
        "paymentPlatformNo":stamp.timeStamp(),
        "refundCompleteTime":"2020-09-23 14:46:51",
        "remark":"auto test refund order"
    }
    res = requests.post(url=Url, data=json.dumps(body), headers=header)
    return res.json()

# print(refundOrder_updateRefundOrderInfo(refundOrder_refund()["data"]["orderNo"]))
# print(create_order())