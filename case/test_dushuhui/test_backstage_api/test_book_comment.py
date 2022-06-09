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


class TestBookComment(object):
    def setup_class(self):
        token = login.login()
        self.header = config.header
        self.header["h-app-id"] = "111"
        # self.header["Cookie"] = "c_token=" + token

    # 评论列表
    @pytest.mark.getAPI
    def test_Booktopiccomment_list(self):
        url = config.dushuhui_bk_host + '/admin/Booktopiccomment/list'
        data = {
            "page": 1,
            "page_size": 1
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == '200'

    # 评论设置/取消精选 (不能走线上)
    @pytest.mark.postAPI
    def test_BookTopicComment_choiceness(self):
        url = config.dushuhui_bk_host + '/admin/BookTopicComment/choiceness'
        id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='')['msg'][0][0]
        data = {
            "comment_id": id
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == '200'

    # 获取用户列表
    @pytest.mark.getAPI
    def test_Virtualuser_list(self):
        url = config.dushuhui_bk_host + '/admin/Virtualuser/list'
        res = requests.get(url, headers=self.header)
        assert res.json()['code'] == '200'

    # 新增精选评论
    @pytest.mark.postAPI
    def test_BookTopicComment_add(self):
        url = config.dushuhui_bk_host + '/admin/BookTopicComment/add'
        num = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id, book_id', relation='')['msg'][0]
        data = {
            "book_id": num[1],
            "topic_id": num[0],
            "content": "test",
            "user_id": "1607310586954202",
            "virtual_like": 100
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == '200'

    # 获取书籍详情
    @pytest.mark.getAPI
    def test_Wxbook_info(self):
        id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='')['msg'][0][0]
        url = config.dushuhui_bk_host + '/admin/Wxbook/info'
        data = {
            'book_id': id
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == '200'

    # 编辑虚拟用户
    @pytest.mark.getAPI
    def test_Virtualuser_edit(self):
        url = config.dushuhui_bk_host + '/admin/Virtualuser/edit'
        data = {
            'user_id': 123456
        }
        res = requests.get(url, headers=self.header, params=data)
        assert res.json()['code'] == '200'


if __name__ == '__main__':
    pytest.main(['-s', 'test_book_comment.py'])