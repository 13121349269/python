#-*-coding:utf8-*-
#@Time : 2020/8/17 17:46
#@Author: tu

import requests
import json
import time
import os

# 定义各项目信息
contacts = "韩静"
tel = "18910777860"
#url = "https://web.hopex.com/api/v1/gateway/Home/ContractSummary?market=BTCUSDT&marketCode=BTCUSDT&contractCode=BTCUSDT&lang=cn"
# url = "https://api0.yuanfangnet.com/v1/api/paycenter/checkapi"
program_name = "CheckAccount"
# 组合信息
alert = "\n程序名称:" + program_name + "服务器IP：" + "192.168.92.153" +"\n联系人:" + contacts + "\n联系电话:" + tel + "\n手动启动192.168.92.153上相同程序"
IP="192.168.92.153"

# 钉钉报警
def dingding(massage):
    dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=c6939d2a80b7366958072d3b65d07ba5bebd5e741850c0382f4c192c7b3aff87"
    #dingding_url = "https://oapi.dingtalk.com/robot/send?access_token=1351a9d6409a366fd37c5aa8401e4f8f180cb152e2e05c7989cff3481594cf47"
    dingding_headers = {"Content-Type": "application/json"}
    dingding_massage = massage
    dingding_data = {"msgtype": "text", "text": {"content": dingding_massage}}
    res = requests.post(dingding_url, headers=dingding_headers, data=json.dumps(dingding_data))
    cur_time = time.strftime('%Y-%m-%d|%H:%M:%S')
    os.environ['massage'] = massage
    os.environ['cur_time'] = cur_time
    os.system("echo $cur_time  $massage >> /home/lichao/alarmlogs/CFD.PayCenter.Push.Host.log")
    return res

headers = {'Content-Type': 'application/json',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
           }

def isRunning(process_name):
    try:
        process = len(os.popen('ps aux | grep "' + process_name + '" | grep -v grep').readlines())
        if process >= 2:
            return True
        else:
            err_massage = "报警！！！ %s is not running" % (program_name, IP)
            dingding(err_massage)
            return False
    except:
        print("Check process ERROR!!!")
        return False

isRunning(program_name)
print('完成')
