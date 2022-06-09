
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


    #优惠券-用户优惠券查询
    @pytest.mark.getAPI
    def test_get_couponcode_memberCodes(self):
        data = mysql.mysqldb().exeSQL('select app_id,member_id from wm_marketing_center.t_promotion_coupon_code where member_id is not null limit 1')['msg'][0]
        Url = config.host + "/api/marketing/service/couponcode/memberCodes?appId=%s&memberId=%s&page=1" % (data[0],data[1])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()['code'] == 0

if __name__=="__main__":
    pytest.main(["-s","test_service_coupon.py"])