#coding:utf-8
#author by lianpengwei
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
import pytest
import requests
from config import config
from utils import login
from utils.stamp import phoneNum
from utils.mysql import mysqldb

mydb = mysqldb()


class TestPublicClassify(object):
    def setup_class(self):
        self.token = login.dushuhui_login()
        self.header = config.header
        self.header["h-app-id"] = "111"


    # 用户频道
    # @pytest.mark.postAPI
    # def test_WxUser_getClientChannel(self):
    #     url = config.dushuhui_bjnews_host + '/WxUser/getClientChannel'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 热搜词
    # @pytest.mark.postAPI
    # def test_WxBook_hotWord(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/hotWord'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 热搜好书
    # @pytest.mark.postAPI
    # def test_WxBook_hotSearchBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/hotSearchBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 书籍搜索
    # @pytest.mark.postAPI
    # def test_WxBook_searchBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/searchBook'
    #     data = {
    #         "searchName": "小狗",
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # banner
    # @pytest.mark.postAPI
    # def test_WxBook_getNewBanner(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getNewBanner'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 首页banner(后台配置)
    # @pytest.mark.postAPI
    # def test_Banner_bannerList(self):
    #     url = config.dushuhui_bjnews_host + '/Banner/bannerList'
    #     params = {
    #         "banner_type_id": 1
    #     }
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header, params=params)
    #     assert res.json()['statusCode'] == '200'

    # 清除banner缓存
    # @pytest.mark.postAPI
    # def test_Banner_clearBannerCache(self):
    #     url = config.dushuhui_bjnews_host + '/Banner/clearBannerCache'
    #     params = {
    #         "banner_type_id": 1
    #     }
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header, params=params)
    #     assert res.json()['statusCode'] == '200'

    # 活动详情
    # @pytest.mark.postAPI
    # def test_Activity_detail(self):
    #     url = config.dushuhui_bjnews_host + '/Activity/detail'
    #     params = {
    #         "id": 1
    #     }
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header, params=params)
    #     assert res.json()['statusCode'] == '200'

    # 活动详情清缓存
    # @pytest.mark.postAPI
    # def test_Activity_clearDetailCache(self):
    #     url = config.dushuhui_bjnews_host + '/Activity/clearDetailCache'
    #     params = {
    #         "id": 1
    #     }
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header, params=params)
    #     assert res.json()['statusCode'] == '200'

    # 一级分类列表
    # @pytest.mark.postAPI
    # def test_WxBookTags_tagList(self):
    #     url = config.dushuhui_bjnews_host + '/WxBookTags/tagList'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 二级分类列表
    # @pytest.mark.postAPI
    # def test_WxBookTags_secondList(self):
    #     url = config.dushuhui_bjnews_host + '/WxBookTags/secondList'
    #     data = {
    #         "cate": "1",
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 二级分类书籍列表
    # @pytest.mark.postAPI
    # def test_WxBookTags_tagsWxBookList(self):
    #     url = config.dushuhui_bjnews_host + '/WxBookTags/tagsWxBookList'
    #     data = {
    #         "cate": "1",
    #         "second_cate": 2,
    #         "page": 0,
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 每日推荐
    # @pytest.mark.postAPI
    # def test_WxBook_getRecommendBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getRecommendBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 书籍每日上新
    # @pytest.mark.postAPI
    # def test_WxBook_everyDayNewBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/everyDayNewBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 本周上新书籍
    # @pytest.mark.postAPI
    # def test_WxBook_getNewBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getNewBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 下周上新书籍
    # @pytest.mark.postAPI
    # def test_WxBook_getAutoBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getAutoBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 新书月榜
    # @pytest.mark.postAPI
    # def test_WxBook_getMonthBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getMonthBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 口碑榜
    # @pytest.mark.postAPI
    # def test_WxBook_getWordBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getWordBook'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 书籍列表
    # @pytest.mark.postAPI
    # def test_WxBook_getList(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getList'
    #     data = {
    #         "page": 2,
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 书籍详情
    # @pytest.mark.postAPI
    # def test_WxBook_detailBook(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/detailBook'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     data = {
    #         "book_id": id,
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 书稿
    # @pytest.mark.postAPI
    # def test_WxBook_manuscript(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/manuscript'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     data = {
    #         "book_id": id,
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 检查用户听书计划状态
    # @pytest.mark.postAPI
    # def test_WxUserPlan_checkPlanStatus(self):
    #     url = config.dushuhui_bjnews_host + '/WxUserPlan/checkPlanStatus'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 保存用户听书提醒
    # @pytest.mark.postAPI
    # def test_WxUserPlan_savePlanStatus(self):
    #     url = config.dushuhui_bjnews_host + '/WxUserPlan/savePlanStatus'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 我的
    # @pytest.mark.postAPI
    # def test_MyHome_mine(self):
    #     url = config.dushuhui_bjnews_host + '/MyHome/mine'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 我的收藏
    # @pytest.mark.postAPI
    # def test_WxUser_getCollectionList(self):
    #     url = config.dushuhui_bjnews_host + '/WxUser/getCollectionList'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 收藏书籍
    # @pytest.mark.postAPI
    # def test_WxUser_checkCollection(self):
    #     url = config.dushuhui_bjnews_host + '/WxUser/checkCollection'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     data = {
    #         "book_id": id,
    #         "status": 2,
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 检查是否为新用户
    # @pytest.mark.postAPI
    # def test_WxBook_checkNewUser(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/checkNewUser'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 已听完书籍
    # @pytest.mark.postAPI
    # def test_WxBook_getHistoryList(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/getHistoryList'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 检查用户是否为VIP
    # @pytest.mark.postAPI
    # def test_WxBook_isVip(self):
    #     url = config.dushuhui_bjnews_host + '/WxBook/isVip'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 检查用户是否关注公众号
    # @pytest.mark.postAPI
    # def test_MyHome_checkIsSub(self):
    #     url = config.dushuhui_bjnews_host + '/MyHome/checkIsSub'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 积分历史
    # @pytest.mark.postAPI
    # def test_Points_pointRule(self):
    #     url = config.dushuhui_bjnews_host + '/Points/pointRule'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 积分商城
    # @pytest.mark.postAPI
    # def test_Points_intShop(self):
    #     url = config.dushuhui_bjnews_host + '/Points/intShop'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 获取用户IP、系统、设备号
    # @pytest.mark.postAPI
    # def test_WxUser_getIp(self):
    #     url = config.dushuhui_bjnews_host + '/WxUser/getIp'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # VIP购买记录
    # @pytest.mark.postAPI
    # def test_MyHome_vipList(self):
    #     url = config.dushuhui_bjnews_host + '/MyHome/vipList'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 已过期VIP记录（分页）
    # @pytest.mark.postAPI
    # def test_MyHome_expiredVip(self):
    #     url = config.dushuhui_bjnews_host + '/MyHome/expiredVip'
    #     data = {
    #         "token": self.token,
    #         "page": 0
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 是否报名
    # @pytest.mark.postAPI
    # def test_NoobBarrack_isSignup(self):
    #     url = config.dushuhui_bjnews_host + '/NoobBarrack/isSignup'
    #     data = {
    #         "token": self.token,
    #         "is_member": True
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 发送手机验证码
    # @pytest.mark.postAPI
    # def test_NoobBarrack_sendMobileCode(self):
    #     url = config.dushuhui_bjnews_host + '/NoobBarrack/sendMobileCode'
    #     data = {
    #         "token": self.token,
    #         "phone": "18500000000"
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 验证手机验证码
    # @pytest.mark.postAPI
    # def test_NoobBarrack_checkMobileCode(self):
    #     url = config.dushuhui_bjnews_host + '/NoobBarrack/checkMobileCode'
    #     data = {
    #         "token": self.token,
    #         "phone": "18500000000",
    #         "code": 1342
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 更新用户联系电话
    # @pytest.mark.postAPI
    # def test_NoobBarrack_checkMobileCode(self):
    #     url = config.dushuhui_bjnews_host + '/NoobBarrack/checkMobileCode'
    #     data = {
    #         "token": self.token,
    #         "code": "1342",
    #         "encrypted_data": "18500000000",
    #         "iv": "18500000000"
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200' or res.json()['statusCode'] == '500'

    # 书籍话题列表
    # @pytest.mark.postAPI
    # def test_BookTopic_bookTopicList(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/bookTopicList'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "book_id": id
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 精选评论
    # @pytest.mark.postAPI
    # def test_BookTopic_choiceComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/choiceComment'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "topic_id": id,
    #         "page": 1,
    #         "page_size": 1
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 详情页-我的评论
    # @pytest.mark.postAPI
    # def test_BookTopic_detailMyComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/detailMyComment'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     topic_id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='', conditions={'book_id': id})['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "book_id": id,
    #         "topic_id": topic_id,
    #         "page": 1,
    #         "page_size": 1
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 个人中心-我的评论
    # @pytest.mark.postAPI
    # def test_BookTopic_centerMyComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/centerMyComment'
    #     data = {
    #         "token": self.token,
    #         "page": 1,
    #         "page_size": 1
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 评论点赞
    # @pytest.mark.postAPI
    # def test_BookTopic_likeComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/likeComment'
    #     topic_id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='')['msg'][0][0]
    #     comment_id = mydb.fetch('dushuhui.mh_dsh_book_topic_comment', 'id', relation='', conditions={'topic_id': topic_id})['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "topic_id": topic_id,
    #         "comment_id": comment_id,
    #         "is_choice": 1
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 取消评论点赞
    # @pytest.mark.postAPI
    # def test_BookTopic_unLikeComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/unLikeComment'
    #     topic_id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='')['msg'][0][0]
    #     comment_id = mydb.fetch('dushuhui.mh_dsh_book_topic_comment', 'id', relation='', conditions={'topic_id': topic_id})['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "topic_id": topic_id,
    #         "comment_id": comment_id,
    #         "is_choice": 1
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 检查用户是否有手机号
    # @pytest.mark.postAPI
    # def test_BookTopic_checkHasMobile(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/checkHasMobile'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 授权手机号
    # @pytest.mark.postAPI
    # def test_BookTopic_authMobile(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/authMobile'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200' or res.json()['statusCode'] == '500'

    # 发送手机验证码
    # @pytest.mark.postAPI
    # def test_BookTopic_sendMessage(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/sendMessage'
    #     data = {
    #         "token": self.token,
    #         "mobile": phoneNum()
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 验证手机验证码
    # @pytest.mark.postAPI
    # def test_BookTopic_checkMobileCode(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/checkMobileCode'
    #     data = {
    #         "token": self.token,
    #         "mobile": phoneNum(),
    #         "code": 3344
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200' or res.json()['statusCode'] == '500'

    # 发表评论
    # @pytest.mark.postAPI
    # def test_BookTopic_publishComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/publishComment'
    #     id = mydb.fetch('dushuhui.mh_dsh_api_wxbook', 'id', relation='and', conditions={'isdelete': 1, 'status': 1})['msg'][0][0]
    #     topic_id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='')['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "book_id": id,
    #         "topic_id": topic_id,
    #         "content": "这本书很不错"
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 删除评论
    # @pytest.mark.postAPI
    # def test_BookTopic_delComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/delComment'
    #     topic_id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='')['msg'][0][0]
    #     comment_id = mydb.exeSQL('select id from dushuhui.mh_dsh_book_topic_comment where topic_id = ' + str(topic_id) + ' and is_del = 2 order by id desc')['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "topic_id": topic_id,
    #         "comment_id": comment_id
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 后台操作接口
    # @pytest.mark.postAPI
    # def test_BookTopic_delComment(self):
    #     url = config.dushuhui_bjnews_host + '/BookTopic/delComment'
    #     topic_id = mydb.fetch('dushuhui.mh_dsh_book_topic', 'id', relation='')['msg'][0][0]
    #     comment_id = mydb.exeSQL('select id from dushuhui.mh_dsh_book_topic_comment where topic_id = ' + str(
    #         topic_id) + ' and is_del = 2 order by id desc')['msg'][0][0]
    #     data = {
    #         "token": self.token,
    #         "secret": "book_topic",
    #         "action": "add_choice",
    #         "topic_id": topic_id,
    #         "comment_id": comment_id,
    #         "like_num": 10
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 检测用户状态
    # @pytest.mark.postAPI
    # def test_SignIn_checkUser(self):
    #     url = config.dushuhui_bjnews_host + '/SignIn/checkUser'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 获取用户周历
    # @pytest.mark.postAPI
    # def test_SignIn_weeks(self):
    #     url = config.dushuhui_bjnews_host + '/SignIn/weeks'
    #     data = {
    #         "token": self.token
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # # 获取周详情
    # @pytest.mark.postAPI
    # def test_SignIn_weekInfo(self):
    #     url = config.dushuhui_bjnews_host + '/SignIn/weekInfo'
    #     self.header['Content-Type'] = 'application/x-www-form-urlencoded'
    #     data = {
    #         "token": self.token,
    #         "number": 1
    #     }
    #     res = requests.post(url, data=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'

    # 精选文章列表
    # @pytest.mark.postAPI
    # def test_ChoiceArticle_articleList(self):
    #     url = config.dushuhui_bjnews_host + '/ChoiceArticle/articleList'
    #     data = {
    #         "page": 1,
    #         "page_size": 1,
    #         "type": 1
    #     }
    #     res = requests.post(url, json=data, headers=self.header)
    #     assert res.json()['statusCode'] == '200'


if __name__ == '__main__':
    pytest.main(['-s', 'test_bjnews_post.py'])