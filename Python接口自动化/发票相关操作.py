# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/11/10 上午10:06

import json
import requests
import random

# json.dumps() 将Python对象编码成JSON字符串
"""
json.dump(obj, fp, *, skipkeys=false, ensure_ascii=True,check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
json.dumps(obj, *, skipkeys=false, ensure_ascii=True,check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

obj：表示要序列化的对象
fp：文件描述，将序列化的 str 保存到文件中， json 模块总是生成 str 对象，而不是字节对象；因此 fp.write() 必须支持 str 输入
skipkeys：默认为 False，如果 skipkeys=True，则跳过不是基本类型（str、int、float、bool、None）的 dict 键，不会引发 TypeError
ensure_ascii：默认值为 True，能将所有传入的非 ASCII字符转义输出；如果 ensure_ascii=False，则这些字符串按原样输出，例如汉字也原样输出
check_circular：默认值为 True，如果 check_circular=False，则跳过对容器类型的循环引用检查，循环引用将导致OverflowError
allow_nan：默认值为True，如果 allow_nan=False，则严格遵守JSON规范，序列化超出范围的浮点值（nan，inf，-inf）会引发ValueError。如果 allow_nan=True，则将使用它们的 JavaScript 等效项（NaN，Infinity，-Infinity）。
indent：设置缩进格式，默认值为 None，选择的是最紧凑的（顶格，且不换行）表示，
        如果 indent 是字符串，插入换行符且 JSON 数组元素和对象成员将使用 该字符串进行补充缩进； 
        indent 为0、负数、""或者"  "，仅插入换行符；
        indent 为正整数，插入换行符且使用正整数个空格进行缩进；
        如果 indent 是一个转义字符串（例如"\t",相当于 tab键；"\n",相当于换行符），则插入换行符且使用该转义符用于缩进每个级别
separators：去除分隔符后面的空格，默认值为 None，则默认为 (', ', ': ') ；如果指定，则分割符应为 (item_separator, key_separator) 元组，要获得最紧凑的 JSON 表示，可以指定 (',', ':')以消除空格。
default：默认值为 None，如果指定，则 default 应该是为无法以其他方式序列化的对象调用的函数，它应返回对象的 JSON 可编码版本或引发 TypeError，如果没有指定，则会引发 TypeError
sort_keys：默认值为 False，如果sort_keys=True，则字典的输出将按 键值 排序。
"""
# json.loads() 将已编码的JSON字符串解码为Python对象
# json.dump()和json.load() 需要传入文件描述符，加上文件操作
# JSON内部的格式要注意，一个好的格式能够方便读取，可以用 indent格式化

data = {"id": None, "consignee": "14", "mobile": "11145637574", "address": "6573564424", "defaulted": None,
        "wasCorpAddress": None, "province": "广东省", "city": "深圳市", "area": "福田区"}
my_data = json.dumps(data, ensure_ascii=False, skipkeys=True)
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="    ")
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent=-1)
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent=0)
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent=2)
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="小朱")
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="\t")
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="\n")
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="\b")

my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="\t", separators=(', ', ': '))


# # my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="\t", separators=(',', ':'))
# my_data1 = json.dumps(data, ensure_ascii=False, skipkeys=True, sort_keys=True, indent="\t", separators=('Ai', '--'))

# print(my_data, type(my_data))
# print(my_data1)

# def create_data():
#     # my_address_data = []
#     with open('my_data.txt', 'w', encoding='utf8') as f:
#         for n in range(20, 102):
#             mobile = 11145637574 + n
#             address = 6573564424 + n
#             my_address = {"id": None, "consignee": str(n), "mobile": str(mobile), "address": str(address), "defaulted": None, "wasCorpAddress": None, "province": "广东省", "city": "深圳市", "area": "福田区"}
#             my_address_json = json.dumps(my_address, ensure_ascii=False, skipkeys=True)
#             # my_address_data.append(my_address_json)
#             f.writelines(str(my_address_json)+ '\n')
#
#         # print(my_address_data)
#     f.close()


# create_data()


def create_invoice():
    # my_invoice_data = []
    my_invoice_type = ["Corporation", "NonEnterpriseEntity"]
    with open('my_invoice_data.txt', 'w', encoding='utf8') as f:
        for n in range(1, 6):
            registrationNo = ""
            invoice_registrationNo = registrationNo.join(random.choice("0123456789") for i in range(15))
            invoice_type = random.choice(my_invoice_type)
            invoice_title = "大乔" + str(n)
            my_address = {"defaulted": False, "registrationNo": str(invoice_registrationNo), "title": invoice_title,
                          "type": invoice_type}
            my_address_json = json.dumps(my_address, ensure_ascii=False, skipkeys=True)
            # my_address_data.append(my_address_json)
            f.writelines(str(my_address_json) + '\n')

        # print(my_address_data)
    f.close()


create_invoice()


class LoginWeb(object):
    """前台自主登录"""

    # 注意，需要将 传参 改成 json 格式然后再放入 函数形参，进行传参
    def __init__(self, login_data):
        """传入登录参数"""
        self.login_data_json = json.dumps(login_data)  # 需要将字典转成 json 格式，然后再传参

    def login_web(self, login_url, login_headers):
        """自主登录web页面，需要传入 登录URL、登录headers"""
        send_login_req = requests.post(url=login_url, data=self.login_data_json, headers=login_headers)
        login_res_json = send_login_req.json()  # 将返回数据以 json 格式打印出来
        # print(login_res_json)
        # 获取返回数据的 accountToken，employeeToken
        login_accountToken = login_res_json["data"]["accountToken"]
        login_employeeToken = login_res_json["data"]["employeeToken"]
        login_authorization = "Bearer " + login_employeeToken
        return {"login_accountToken": login_accountToken, "login_authorization": login_authorization}


# login = LoginWeb(login_data).login_web(login_url, login_headers)
# print(login["login_accountToken"])

class Operate_Invoice(LoginWeb):
    def __init__(self, login_data, login_url, login_headers):
        # 继承的登录 类，改写登录的 __init__() 方法
        super().__init__(login_data)
        # 登录
        login_web = LoginWeb(login_data).login_web(login_url, login_headers)
        # 获取登录的 accountToken 和 authorization
        self.login_accountToken = login_web["login_accountToken"]
        self.login_authorization = login_web["login_authorization"]
        self.json_headers = {"content-type": "application/json", "authorization": self.login_authorization,
                        "accounttoken": self.login_accountToken}
        self.form_headers = {"authorization": self.login_authorization,
                        "accounttoken": self.login_accountToken}

    def search_invoice(self, search_invoice_url, search_data):
        """查询所有发票"""
        self.search_data_json = json.dumps(search_data)  # 需要将字典转成 json 格式，然后再传参
        send_search_req = requests.post(url=search_invoice_url, headers=self.json_headers, data=self.search_data_json)
        search_res_json = send_search_req.json()
        # search_res_json_data = search_res_json["data"]["content"][-2]["title"]
        # 返回查询结果的 json 数据
        return search_res_json

    def create_invoice(self, create_url):
        """新增发票"""
        with open('my_invoice_data.txt', 'r', encoding='utf8') as f:
            for line in f.readlines():  # 逐行读取数据
                create_data_json = line.encode('utf-8')
                # 没有加 .encode('utf-8') 时报错
                # UnicodeEncodeError: 'latin-1' codec can't encode characters in position 68-70: Body ('公孙离') is not valid Latin-1. Use body.encode('utf-8') if you want to send it encoded in UTF-8.
                # print(line_data, type(line_data))
                # 发起 新增发票 请求
                send_create_req = requests.post(url=create_url, data=create_data_json, headers=self.json_headers)
                create_res_json = send_create_req.json()
                print("===============================================")
                print(create_res_json)

    def delete_invoice(self, delete_url, search_invoice_url, search_data):
        """调用查询发票的接口，获取发票的id，通过发票id删除发票"""
        search_invoice = self.search_invoice(search_invoice_url, search_data)
        # 获取最后一条发票的id
        invoice_id = search_invoice["data"]["content"][-1]["id"]
        delete_data = {"invoiceId": invoice_id}
        # print(delete_data)
        # delete_data_json = json.dumps(delete_data)
        delete_url_id = delete_url + "?invoiceId=" + invoice_id
        # 删除操作
        res = requests.post(url=delete_url, data=delete_data, headers=self.form_headers).json()
        # 断言删除的发票是否还在
        re_search_invoice = self.search_invoice(search_invoice_url, search_data)["data"]["content"]
        invoice_id_list = []
        for invoice in re_search_invoice:
            invo_id = invoice["id"]
            invoice_id_list.append(invo_id)
        panduan = invoice_id in invoice_id_list
        if False == panduan:
            print("发票已被删除")
        return res


web_tbt_host = "https://test-web-te-yi-xing-env-3.teyixing.com"
web_tbo_host = "https://test-tehang-system-env-3.teyixing.com"
login_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/account/tmc/loginPassword"
login_datas = {"mobile": "13632296409", "password": "@12345678", "captchaCode": None, "remember": False,
               "captchaToken": None, "invitationCode": None, "operateSource": "WebCustomer", "loginScene": "Normal"}
login_headers = {"content-type": "application/json"}
# 登录
# login_web = LoginWeb(login_datas).login_web(login_url, login_headers)
login = Operate_Invoice(login_datas, login_url, login_headers)

search_data = {"pageNumber": 1, "pageSize": 100}
search_invoice_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/customer/invoice/search"
search_invoice_data = login.search_invoice(search_invoice_url,search_data)
# print(search_invoice_data)

create_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/customer/invoice/create"
create_invoice_data = login.create_invoice(create_url)


delete_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/customer/invoice/delete"
delete_invoice_data = login.delete_invoice(delete_url, search_invoice_url, search_data)
print(delete_invoice_data)



# web_tbt_host = "https://test-web-te-yi-xing-env-1.teyixing.com"
# web_tbo_host = "https://test-tehang-system-env-1.teyixing.com/"
# login_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/account/tmc/loginPassword"
#
# # 获取 token 的方法
# # 自主登录账号
# login_data = {"mobile": "13632296409", "password": "@12345678", "captchaCode": None, "remember": False, "captchaToken": None, "invitationCode": None, "operateSource": "WebCustomer", "loginScene": "Normal"}
# login_data_json = json.dumps(login_data)  # 需要将字典转成 json 格式，然后再传参
# login_headers = {"content-type": "application/json"}
# send_login_req = requests.post(url=login_url, data=login_data_json, headers=login_headers)
# login_res_json = send_login_req.json()  # 将返回数据以 json 格式打印出来
# # 获取返回数据的 accountToken，employeeToken
# login_accountToken = login_res_json["data"]["accountToken"]
# login_employeeToken = login_res_json["data"]["employeeToken"]
# login_authorization = "Bearer " + login_employeeToken
# print(login_accountToken)
# print(login_employeeToken)
# print(login_authorization)
# print(send_login_req.text)


# # 查询 员工名下的 发票信息
# search_invoice_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/customer/invoice/search"
# search_headers = {"content-type": "application/json", "authorization": login_authorization, "accounttoken": login_accountToken}
# search_data = {"pageNumber": 1, "pageSize": 100}
# search_data_json = json.dumps(search_data)
# # 发起 查询发票 请求
# send_search_req = requests.post(url=search_invoice_url, headers=search_headers, data=search_data_json)
# search_res_json = send_search_req.json()
# search_res_json_data = send_search_req.json()["data"]["content"][-2]["title"]
# print(search_res_json)
# print(search_res_json_data)
#
# print("===============================================")
# # 新增发票
# create_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/customer/invoice/create"
# create_headers = {"content-type": "application/json", "authorization": login_authorization, "accounttoken": login_accountToken}
# # create_invoice_data = {"defaulted": False, "registrationNo": "5735676576537657", "title": "公孙离", "type": "Corporation"}
# # create_data_json = json.dumps(create_invoice_data)
# with open('my_invoice_data.txt', 'r', encoding='utf8') as f:
#     for line in f.readlines():  #逐行读取数据
#         create_data_json = line.encode('utf-8')
#         # 没有加 .encode('utf-8') 时报错
#         # UnicodeEncodeError: 'latin-1' codec can't encode characters in position 68-70: Body ('公孙离') is not valid Latin-1. Use body.encode('utf-8') if you want to send it encoded in UTF-8.
#         # print(line_data, type(line_data))
#         # 发起 新增发票 请求
#         send_create_req = requests.post(url=create_url, data=create_data_json, headers=create_headers)
#         create_res_json = send_create_req.json()
#         print("===============================================")
#         print(create_res_json)
#
# # 通过读取 .txt文件来获取新增发票信息
#
# print("===============================================")
# # 查询 员工名下的 发票信息
# search_invoice_url = web_tbt_host + "/tmc-customer-api-gateway/front/v1/customer/invoice/search"
# search_headers = {"content-type": "application/json", "authorization": login_authorization, "accounttoken": login_accountToken}
# search_data = {"pageNumber": 1, "pageSize": 100}
# search_data_json = json.dumps(search_data)
# # 发起 查询发票 请求
# send_search_req = requests.post(url=search_invoice_url, headers=search_headers, data=search_data_json)
# search_res_json = send_search_req.json()
# search_res_json_data = send_search_req.json()["data"]["content"][-2]["title"]
# print(search_res_json)
# print(search_res_json_data)
