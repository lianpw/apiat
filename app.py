# -*- coding: utf-8 -*-
__author__ = 'cowry'
import os

from flask import Flask

app = Flask(__name__,static_url_path='')

@app.route('/report')
def report():

    test_report = os.path.abspath('./static')
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # 按时间排序
    return  app.send_static_file(lists[-1])

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)

