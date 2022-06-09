#coding:utf-8
#author by wangyunbao

import random,time,string,datetime

def timeStamp():
    ts = str(round(time.time()*1000))
    return ts

def phoneNum():
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                 '188','147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    start = random.choice(num_start)
    end = ''.join(random.sample(string.digits,8))
    res = start+end
    return res

#用于定义时间，例如startTime, endTime. timeday(-0.5) 表示当前时间减12小时, timeday(+1) 表示当前时间加24小时
def timeday(day):
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')

#随机数 想取几位的就输入几 ,例如： stamp.randomNum(19) 则表示要取随机得19位数
def randomNum(Num):
    mi = ''.join(str(random.randint(10**(Num-1),10**Num-1)))
    return mi

#随机取得活动数据类型
    # 'source_dimension' => '用户来源',
    # 'inst_dimension' => '投放人员',
    # 'agent_dimension' => '代理',
    # 'periods_dimension' => '期数',
    # 'class_dimension' => '小白营班级',
    # 'live_class_dimension' => '小白营直播班级',
    # 'teacher_dimension' => '班主任',
    # 'big_class_dimension' => '大课班级',
def random_crowd_dimension():
    type = ['source_dimension' ,'inst_dimension' ,'agent_dimension', 'periods_dimension','class_dimension' ,
            'live_class_dimension' ,'teacher_dimension' ,'big_class_dimension']
    crowd_dimension = random.choice(type)
    return crowd_dimension

