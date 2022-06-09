import pytest,requests,json,datetime
from config import config
from utils import login,baseData,stamp,mysql


class TestCoupon(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["Cookie"] = "c_token="+token
        self.header["h-app-id"] = "100"
        self.startTime = stamp.timeday(-1)
        self.endTime = stamp.timeday(+1)

    #优惠券类型查询
    @pytest.mark.getAPI
    def test_query_coupontypes(self):
        Url = config.host + "/api/marketing/metadata/coupon/coupontypes"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0
        assert res.json()['data'][0]['name' ]=='满减优惠'


    # 优惠券-列表查询
    @pytest.mark.getAPI
    def test_coupon_list(self):
        Url = config.host + "/api/marketing/metadata/coupon/list?&appId=%s&page=1" % ("100")
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    # 优惠券-明细
    @pytest.mark.getAPI
    def test_get_coupon_info(self):
        data = mysql.mysqldb().fetch(col='app_id,id', relation='', table='wm_marketing_center.t_promotion_coupon')['msg'][0]
        Url = config.host + "/api/marketing/metadata/coupon/info?appId=%s&couponId=%s" % (data[0] ,data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #优惠券 - 优惠规则
    @pytest.mark.getAPI
    def test_get_coupon_rule(self):
        Url = config.host + "/api/marketing/metadata/coupon/rule?couponTypeCode=%s" % (1)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0


    #优惠券码-列表查询
    @pytest.mark.getAPI
    def test_couponcode_list(self):
        data = mysql.mysqldb().fetch(col='app_id,coupon_id', relation='', table='wm_marketing_center.t_promotion_coupon_code')['msg'][0]
        Url = config.host + "/api/marketing/metadata/couponcode/list?appId=%s&couponId=%s&page=1" % (data[0] ,data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

if __name__=="__main__":
    pytest.main(["-s","test_backend_coupon.py"])