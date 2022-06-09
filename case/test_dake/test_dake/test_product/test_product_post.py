#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_pro_post(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    # #物品添加(需要写入数据库)
    # @pytest.mark.postAPI
    # def test_user_item_add(self):
    #     Url = config.spzx_host + "/api/item/add"
    #     body = {
    #
    #         "item_name": 'test_product',
    #         "category_id": '1',
    #         "description": '测试'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()


    # #物品编辑(需要编辑数据库)
    # @pytest.mark.postAPI
    # def test_item_edit(self):
    #     item_No = mysqld.fetch(table="wm_product_center.wp_item", col="item_num", relation="", limitd=1)["msg"][0]
    #     Url = config.spzx_host + "/api/item/edit"
    #     body = {
    #
    #         "item_num": item_No[0],
    #         "description": '1'
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()


    # #商品添加(需要编辑数据库)
    # @pytest.mark.postAPI
    # def test_product_add(self):
    #     Url = config.spzx_host + "/api/product/add"
    #     body = {
    #           "product_name": "贺超",
    #           "category_id": 7813185911799516,
    #           "price": 462,
    #           "description": "wg7QH0p3",
    #           "item_list": [
    #             "wp_159213490832566",
    #             "wp_159213490832566",
    #             "wp_159213490832566",
    #             "wp_159213490832566",
    #             "wp_159213490832566"
    #           ],
    #           "original_price": 120,
    #           "precondition_nums": [
    #             "sp_159236926958601",
    #             "sp_159236926958601",
    #             "sp_159236926958601",
    #             "sp_159236926958601"
    #           ],
    #           "precondition_relation": 1,
    #           "repeatable": 1
    #         }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     return res.json()



    # #商品编辑(需要编辑数据库)
    # @pytest.mark.postAPI
    # def test_product_edit(self):
    #     product_No = mysqld.fetch(table="wm_product_center.wp_product", col="product_num	", relation="", limitd=1)["msg"][0]
    #     Url = config.spzx_host + "/api/product/edit"
    #     body = {
    #
    #         "product_num": product_No[0],
    #         "description": 'test',
    #         "precondition_ids": '',
    #         "original_price	": '',
    #         "precondition_relation": ''
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()



    # #商品上/下架(需要编辑数据库)
    # @pytest.mark.postAPI
    # def test_product_on(self):
    #     product_No = mysqld.fetch(table="wm_product_center.wp_product", col="product_num	", relation="", limitd=1)["msg"][0]
    #     Url = config.spzx_host + "/api/product/on"
    #     body = {
    #
    #         "product_num": product_No[0],
    #         "status": '1'#1,上架；2，下架
    #
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:", res.json())
    #     return res.json()




if __name__=="__main__":
     pytest.main(["-s","test_product_post.py"])