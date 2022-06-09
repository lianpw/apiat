#coding:utf-8
#author by lianpengwei
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
import pytest
import requests
import datetime
from config import config
from utils import login
from utils import stamp
from utils.mysql import mysqldb

mydb = mysqldb()


class TestPost(object):
    id = None

    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        # self.header["Cookie"] = "c_token=" + token

    # 用户听书感悟列表
    @pytest.mark.postAPI
    def test_admin_feeling_list(self):
        url = config.dushuhui_bk_host + '/admin/feeling/list'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "page": 1,
            "page_size": 1
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # banner列表
    @pytest.mark.postAPI
    def test_admin_bannermanage_list(self):
        url = config.dushuhui_bk_host + '/admin/bannermanage/list'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "page": 1,
            "page_size": 1,
            "banner_type_id": 1
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # banner立即生效
    @pytest.mark.postAPI
    def test_admin_bannermanage_flushBanner(self):
        url = config.dushuhui_bk_host + '/admin/bannermanage/flushBanner'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "banner_type_id": 1
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # 活动列表
    @pytest.mark.postAPI
    def test_admin_activitymanage_list(self):
        url = config.dushuhui_bk_host + '/admin/activitymanage/list'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "page": 1,
            "page_size": 1
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # 活动详情
    @pytest.mark.postAPI
    def test_admin_activitymanage_detail(self):
        url = config.dushuhui_bk_host + '/admin/activitymanage/detail'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "id": 1
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # 活动预览
    @pytest.mark.postAPI
    def test_admin_activitymanage_preview(self):
        url = config.dushuhui_bk_host + '/admin/activitymanage/preview'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "id": 1,
            "activity_name": "test",
            "content": "test content"
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # 添加活动
    @pytest.mark.postAPI
    def test_admin_activitymanage_add(self):
        url = config.dushuhui_bk_host + '/admin/activitymanage/add'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "activity_name": "test",
            "content": "test content",
            "operate_id": "1598606668982307",
            "operate_name": "维伊"
        }
        res = requests.post(url, data=data, headers=self.header)
        TestPost.id = mydb.exeSQL("select id from dushuhui.mh_dsh_admin_activity_manage where activity_name = 'test' ORDER BY created desc").get('msg')[0][0]
        assert res.json()['code'] == '200'

    # 活动修改
    @pytest.mark.postAPI
    def test_admin_activitymanage_edit(self):
        url = config.dushuhui_bk_host + '/admin/activitymanage/edit'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "id": self.id,
            "activity_name": stamp.phoneNum(),
            "content": "test content",
            "operate_id": "1598606668982307",
            "operate_name": "维伊"
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # 活动删除
    @pytest.mark.postAPI
    def test_admin_activitymanage_del(self):
        url = config.dushuhui_bk_host + '/admin/activitymanage/del'
        self.header['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            "id": self.id,
            "operate_id": "1598606668982307",
            "operate_name": "维伊"
        }
        res = requests.post(url, data=data, headers=self.header)
        assert res.json()['code'] == '200'

    # 大数据推送标签用户
    @pytest.mark.postAPI
    def test_admin_MenuAndTag_bigDataPushMemberTag(self):
        url = config.dushuhui_bk_host + '/admin/MenuAndTag/bigDataPushMemberTag'
        data = {
                  "secret": "menu_and_tag",
                  "push_data": [
                    "1:oYYbYweU11X0Lw_30QsdGnGsk3SY",
                    "2:oYYbYwYXjlNzrDRtrD8zLz4MIJP0"
                  ]
                }
        res = requests.post(url, json=data, headers=self.header)
        assert res.json()['code'] == 1

    # 书籍上架日历
    @pytest.mark.postAPI
    def test_admin_Wxbook_upShelfCalendar(self):
        url = config.dushuhui_bk_host + '/admin/Wxbook/upShelfCalendar'
        res = requests.post(url, headers=self.header)
        assert res.json()['code'] == '200'

    # 书籍开启/关闭自动上架
    @pytest.mark.postAPI
    def test_admin_Wxbook_checkAuto(self):
        url = config.dushuhui_bk_host + '/admin/Wxbook/checkAuto'
        id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='')['msg'][0][0]
        now = datetime.datetime.now()
        date = str(now + datetime.timedelta(days=1))[:10]
        data = {
            'id': id,
            'is_auto': 1,
            'shelf_time': date
        }
        res = requests.post(url, headers=self.header, json=data)
        assert res.json()['code'] == '200' or res.json()['code'] == '500'


if __name__ == '__main__':
    pytest.main(['-s', 'test_backstage_post.py'])