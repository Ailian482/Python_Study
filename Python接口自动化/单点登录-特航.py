# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/11/20 下午5:07


import requests
import json
import urllib3

login_url = "https://dev-corp-integration-api-gateway-env-6.teyixing.com/corp/v1/login/getEmployeeLoginToken"
login_headers = {"Content-Type": "application/json"}
login_data = {"corpCode": "32131", "sign": "8888c8389501a4f96a0de7805e64bb2b", "clientCode": "210004", "approvalNo": "20211118006"}
# 处理请求参数为 json 字符串
login_data_json = json.dumps(login_data, ensure_ascii=False, skipkeys=True)
# print(login_data_json, type(login_data_json))

# urllib3.disable_warnings()
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

send_login = requests.post(url=login_url, headers=login_headers, data=login_data_json, verify=False)
login_res_json = send_login.json()
print(login_res_json)

