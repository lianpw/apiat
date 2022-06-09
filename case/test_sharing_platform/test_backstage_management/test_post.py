#coding:utf-8
#author by lianpengwei


# import pytest
# import requests
# from config import config
# from utils import login
# from utils.mysql import mysqldb
#
# mydb = mysqldb()
# id = mydb.exeSQL('select id from wm_sharing_platform.tags where deleted_at is null limit 1')['msg'][0][0]
#
# class TestTestingEnvironment(object):
#     def setup_class(self):
#         token = login.login()
#         self.header = config.header
#         self.header["h-app-id"] = "111"
#         self.header["Cookie"] = "c_token=" + token

    # # 添加文章(只能在测试环境执行)
    # @pytest.mark.postAPI
    # def test_article_add(self):
    #     url = config.gxpt_bk_host + '/admin/article/add'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "title": "test1124-001",
    #         "cover_image": "./photo.jpg",
    #         "sample_content": "我是试读",
    #         "content": "我是试读\r\n——————————以上为试读——————————\r\n我是正文",
    #         "category_id": 1,
    #         "author_id": "1603710643613287",
    #         "price": '1200',
    #         "is_publish": 0
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # # 添加标签
    # @pytest.mark.postAPI
    # def test_tag_add(self):
    #     url = config.gxpt_bk_host + '/admin/tag/add'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "name": "test001",
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # # 标签更新
    # @pytest.mark.postAPI
    # def test_tag_eidt(self):
    #     url = config.gxpt_bk_host + '/admin/tag/edit'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "name": "更新",
    #         "id": id,
    #         "remark": "更新标签"
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # # 标签删除
    # @pytest.mark.postAPI
    # def test_tag_del(self):
    #     url = config.gxpt_bk_host + '/admin/tag/del'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "id": id
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # # 文章上下架
    # @pytest.mark.postAPI
    # def test_article_publish(self):
    #     url = config.gxpt_bk_host + '/admin/article/publish'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "publish": 0,
    #         "product_no": "sp_16027368791689235"
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # # 编辑文章(只能用线上的测试数据)
    # @pytest.mark.postAPI
    # def test_article_edit(self):
    #     url = config.gxpt_bk_host + '/admin/article/edit'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "product_no": "sp_16027368791689235"
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['code'] == 0
    #
    # # 预览前保存数据
    # @pytest.mark.postAPI
    # def test_preview_save(self):
    #     url = config.gxpt_bk_host + '/admin/article/preview/save'
    #     data = {
    #         "title": "试读测试",
    #         "content": "内容"
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['code'] == 0


# if __name__ == '__main__':
#     pytest.main(['-s', 'test_post.py'])