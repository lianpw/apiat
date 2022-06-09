# -*- coding: utf-8 -*-
__author__ = 'cowry'

import pytest,os,sys,time
from utils import ding,readhtml,baseData,stamp
from config import config


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
#rootPath = "/www/webroot/apiat/release"
sys.path.append(curPath)

base_dir = os.path.abspath(".")
case_dir = base_dir+"/case/"
report_dir = base_dir+"/static/report"+time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime()) +".html"
report_url = "http://"+config.report_ip+"/report"

case_project = sys.argv[1]
# 'getAPI'
api_type = sys.argv[2]

if __name__=="__main__":
    name = baseData.get_serviceName(caseKey=case_project)
    pytest.main(["-s", case_dir, "-m", api_type, "--html=%s" % report_dir])
    message = readhtml.readhtml(report_dir, report_url, name)
    #ding.ding(message)


