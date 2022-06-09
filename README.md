*   驱动框架：pytest
*   测试报告：pytest-html
*   目录说明：
*     case：测试用例目录，根据服务划分不同的文件夹
*     report：测试报告目录，只有一个index.html文件，不能累计增加测试报告，执行测试后，都会把上一次的测试结果清除，如果需要累计测试报告，修改mainRun.py文件
*     utils：工具目录，用于编写case的时候，常用的工具在这里，例如：登陆、mysql连接、生成随机数等等
*     config.py：配置文件，常用的账户信息、数据库信息、测试地址在这里保存
*     mainRun.py：运行测试用例的主入口

*   初始化环境安装：pip3 install -r config/requirements.txt
*   启动服务：python3 app.py 2>&1 &
*   配置crontab：* 9,21 * * * python3 mainRun.py test_middle_center test_account_center getAPI
*   命令行使用规则：
*       python3 mainRun.py test_middle_center test_account_center getAPI
*       mainRun.py:需要写绝对路径
*       参数：
*           test_middle_center：需要测试的服务名称，对应yapi的group
*           test_account_center：需要测试的接口分组，对应yapi的project
*           getAPI：需要执行测试的分类，在写case的时候需要用mark做case分组