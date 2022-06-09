# -*- coding: utf-8 -*-
__author__ = 'cowry'

import pymysql,re
from config import config


class mysqldb():

    def connectDB(self,table):
        '''
        初始化mysql连接字符串
        :return:
        '''
        db = re.search(r'from (.*)\.',table,re.M | re.I)
        if db == None:
            db = table.split(".")[0]
        else:
            db = db.group(1)
        dblist = {"wm_order_center": config.db_order_promotion_host,
                  "wm_marketing_center": config.db_order_promotion_host,
                  "wm_product_center": config.db_goods_host,
                  "wm_authority_center": config.db_auth_host,
                  "wm_live_class": config.db_dk_live_host,
                  "wm_contract_center": config.db_dk_live_host,
                  "wm_live": config.db_xby_live_host,
                  "weimiao": config.db_weimiao_host,
                  "wm_class": config.db_class_host,
                  "wm_opening_center": config.db_user_host,
                  "wm_ucenter_secret": config.db_user_host,
                  "wm_user_center": config.db_user_host,
                  "wm_sms_center":config.db_goods_host,
                  "wm_sharing_platform":config.db_sharing_host,
                  "wm_infoflow":config.db_infoflow_host,
                  "wm_subject":config.db_subject_host,
                  "dushuhui":config.db_dushuhui_host
                  }
        Host = dblist[db]
        User = config.db_user
        Passwd = config.db_passwd
        Port = config.db_port
        con = pymysql.connect(host=Host,
                               user=User,
                               password=Passwd,
                               port=Port,
                               charset="utf8")
        self.conn = con.cursor()

    def dict_2_str_and(self,dictin):
        '''
        将字典变成,key='value' and key='value'的形式
        :param ditcin:字典
        :return:
        '''
        tmplist = []
        try:
            for k, v in dictin.items():
                tmp = "%s='%s'" % (str(k), (str(v)))
                tmplist.append(' ' + tmp + ' ')
            dict_and =  ' and '.join(tmplist)
            return dict_and
        except Exception as err:
            return err

    def dict_2_str_or(self,dictin):
        '''
        将字典变成,key='value' and key='value'的形式
        :param ditcin:字典
        :return:
        '''
        tmplist = []
        try:
            for k, v in dictin.items():
                tmp = "%s='%s'" % (str(k), (str(v)))
                tmplist.append(' ' + tmp + ' ')
            dict_or =' or '.join(tmplist)
            return dict_or
        except Exception as err:
            return err

    def fetch(self,table, col, relation='', conditions=None,limitd =1):
        '''
        :param col:列名
        :param table: 表名
        :param conditions: 条件
        :return:
        '''
        self.connectDB(table)
        sql = 'select %s from %s' % (col, table)
        if relation == 'and':
            if conditions:
                sql += ' where %s limit %s' % (mysqldb().dict_2_str_and(dictin=conditions),limitd)
        elif relation == 'or':
            if conditions:
                sql += ' where %s limit %s' % (mysqldb().dict_2_str_or(dictin=conditions),limitd)
        else:
            if conditions:
                sql += ' where %s limit %s' % (mysqldb().dict_2_str_or(dictin=conditions), limitd)
            else:
                sql += ' limit %s' % (limitd)
        print("sql:",sql)
        self.conn.execute(sql)
        res = self.conn.fetchall()
        self.conn.close()
        return {"code": 0, "msg": res}

    def update(self,col, table, relation, conditions=None):
        '''
        :param col:列名
        :param table: 表名
        :param conditions: 条件
        :return:
        '''
        sql = 'update %s set %s' % (table, col)
        if relation == 'and':
            if conditions:
                sql += ' where %s ' % mysqldb.dict_2_str_and(dictin=conditions)
        else:

            if conditions:
                print("conditions")
                print(conditions)
                sql += ' where %s ' % mysqldb.dict_2_str_or(dictin=conditions)
        try:
            self.connectDB(sql)
            res = self.conn.execute(sql)
            return {"code": 0, "msg": res}
        except Exception as err:
            return {"code": 1, "msg": err}

    def exeSQL(self,sql):
        print("sql:", sql)
        self.connectDB(sql)
        self.conn.execute(sql)
        res = self.conn.fetchall()
        self.conn.close()
        return {"code": 0, "msg": res}

if __name__ == '__main__':

    mysql = mysqldb().fetch(col='app_id,order_no', relation='', table='wm_order_center.t_order')
    print("mysql")


