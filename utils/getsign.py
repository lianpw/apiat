#coding:utf-8
#author by wangyunbao

import hashlib

def sign(Mid,Appkey):
    postfix = {"wm_class":"f8sYE88t07Gzqw8BHxBBsAg76sLTRJLB","xiaobai":"bvWXsNllkr20DHqv3IjMd2yAVd9JslLr","opening":"XC2mPdhcjZpn5Bhc0XoMbRvJKGhRtiIW",}
    org = ("app_key=%s&mid=%s%s") %(Appkey,Mid,postfix[Appkey])
    s = hashlib.md5(org.encode('UTF-8')).hexdigest()
    return s

# print(sign(21279,'wm_class'))