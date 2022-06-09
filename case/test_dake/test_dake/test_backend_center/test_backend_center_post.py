#coding:utf-8
#author by yinjiangbing
import requests,pytest
from config import config
from config.config import header
from utils import login,stamp,mysql
mysqld = mysql.mysqldb()

import json
class Test_backend_post(object):
    def setup_class(self):
        self.header = config.header
        self.mysqld =mysql.mysqldb()
        self.header["h-app-id"] = "100"
        self.header["Cookie"] = login.course_login()


    # #批改作业
    # @pytest.mark.postAPI
    # def test_homework_check(self):
    #     Url = config.sjy_host_homework + "/api/practice/homework/check"
    #     body = {
    #         "id": '1',
    #         "content": '1',
    #         "score": "1"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     assert res.json()["code"] == 0



    # #消息推送
    # @pytest.mark.postAPI
    # def test_homework_notify(self):
    #     Url = config.sjy_host_homework + "/api/practice/homework/notify"
    #     body = {
    #         "user_ids": [
    #     "ea non Ut eiusmod aliqua"
    #             ],
    #         "title": "veniam sed tempor ea",
    #         "content": "in culpa labore in eu"
    #     }
    #     res = requests.post(url=Url, data=json.dumps(body), headers=header)
    #     print("res:",res.json())
    #     assert res.json()["code"] == 0


if __name__=="__main__":
    pytest.main(["-s","test_backend_center_post.py"])