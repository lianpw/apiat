#coding:utf-8
#author by wangyunbao
import traceback
import requests, hashlib,json,re,subprocess
from config import config

def login():
    try:
        passw = hashlib.md5(config.passwd.encode(encoding='UTF-8')).hexdigest()
        Url = config.host + "/api/auth/account/login"
        body = {
            "name": config.user,
            "password": passw,
            "verifyCode":'1234'

        }
        # config.header["Cookie"]="1234"
        if config.header.get('Cookie'):
            config.header.pop('Cookie')
        cookies = {"verification_code":'1234'}
        res = requests.post(url=Url, data=json.dumps(body), headers=config.header, cookies =cookies )
        token = res.json()["data"]["token"]
        return token
    except Exception as e:
        return res.json()

def course_login():
    try:
        Url = config.sjy_host_loign + "/api/user/doLogin"
        body = {
            "openId": config.openId
        }

        res = requests.post(url=Url, data=body, headers='')
        return res.headers["Set-Cookie"]
    except Exception:
        return res.json()

def xby_login():
    try:
        header = config.header
        header["If-None-Match"] = "A8EF1853E4325FF5326AFE808B1E0D84"
        header["Content-Type"] = "application/x-www-form-urlencoded"
        session = requests.session()
        Url = config.xby_host + "/api/user/doLogin"
        body = {
            "openId": config.openId
        }
        res = session.post(url=Url, data=body)
        header["Set-Cookie"] = res.headers["Set-Cookie"]
        return header
    except Exception:
        return res.json()

def sharing_platform_login():
    return config.sharing_platform_cookie

def dushuhui_login():
    return config.dushuhui

def dushuhui_h5_login():
    return config.dushuhui_h5

# 9mK42XKkTH01yXocpgZ6CeEgUPe1tp0UTdYMwz1O
