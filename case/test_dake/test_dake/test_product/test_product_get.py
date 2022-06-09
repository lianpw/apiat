#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class TestProduct(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    #种类列表
    @pytest.mark.getAPI
    def test_species_list(self):
        Url = config.spzx_host + "/api/species/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #全部商品名称列表
    @pytest.mark.getAPI
    def test_product_all_list(self):
        Url = config.spzx_host + "/api/product/all_name"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #商品分类
    @pytest.mark.getAPI
    def test_product_category(self):
        product_No = mysqld.fetch(table="wm_product_center.wp_product", col="product_num", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/product/category?product_num=%s" %(product_No[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #渠道列表
    @pytest.mark.getAPI
    def test_channel_list(self):
        Url = config.spzx_host + "/api/channel/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #分类详情
    @pytest.mark.getAPI
    def test_category_info(self):
        category_id = mysqld.fetch(table="wm_product_center.wp_category", col="id", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/category/info?ids=%s" %(category_id[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #物品列表_simple
    @pytest.mark.getAPI
    def test_itemlist_simple(self):
        itemname = mysqld.fetch(table="wm_product_center.wp_item", col="item_name", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/item/list_simple?item_num_name=%s" %(itemname[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #类目列表
    @pytest.mark.getAPI
    def test_category_list(self):
        Url = config.spzx_host + "/api/category/list?page=1"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #物品详情
    @pytest.mark.getAPI
    def test_item_info(self):
        item_No = mysqld.fetch(table="wm_product_center.wp_item", col="item_num", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/item/info?item_num=%s" %(item_No[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #物品列表
    @pytest.mark.getAPI
    def test_item_list(self):
        Url = config.spzx_host + "/api/item/list"
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #商品列表
    @pytest.mark.getAPI
    def test_product_list_01(self):
        product1 = mysqld.fetch(table="wm_product_center.wp_product,wm_product_center.wp_item", col="product_name,item_num,item_name", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/product/list?product_name=%s&item_num=%s&item_name=%s&page=%s&page_size=%s" %(product1[0],product1[1],product1[2],1,1)
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


    #商品详情
    @pytest.mark.getAPI
    def test_product_info_01(self):
        product_No = mysqld.fetch(table="wm_product_center.wp_product", col="product_num", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/product/info?product_num=%s" %(product_No[0])
        res = requests.get(url=Url, headers=self.header)
        # print("res:",res.json())
        assert res.json()["code"] == 0


    #商品详情_批量查询
    @pytest.mark.getAPI
    def test_product_info_batch(self):
        product_No = mysqld.fetch(table="wm_product_center.wp_product", col="product_num", relation="", limitd=1)["msg"][0]
        Url = config.spzx_host + "/api/product/info_batch?product_num_list=%s" %(product_No[0])
        res = requests.get(url=Url, headers=self.header)
        assert res.json()["code"] == 0


if __name__=="__main__":
     pytest.main(["-s","test_product_get.py"])