#coding:utf-8
#author by wangyunbao


import time,hmac,hashlib,base64,requests,json
import urllib.parse
from config import config

timestamp = str(round(time.time()*1000))
secret = config.secret
secret_enc = secret.encode("utf-8")
string_to_sign = '{}\n{}'.format(timestamp,secret)
string_to_sign_enc = string_to_sign.encode("utf-8")
hmac_code = hmac.new(secret_enc,string_to_sign_enc,digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

def ding(message):

    Url = "https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s" %(
    config.at_token, timestamp, sign)

    header = {
        "Content-Type":"application/json"
    }

    textMsg = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "at": {
            "atMobiles": [
                "11111111111"
            ],
            "isAtAll": 0
        }
    }
    json_textMsg = json.dumps(textMsg)
    res = requests.post(url=Url,data=json_textMsg,headers=header)
    return res.json()

#print(ding(message="test"))
