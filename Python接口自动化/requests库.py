# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2021/12/21 下午4:20

from bs4 import BeautifulSoup
import requests
import json

login_url = "https://test-web-te-yi-xing-env-1.teyixing.com/tmc-customer-api-gateway/front/v1/account/tmc/loginPassword"
login_headers = {"content-type": "application/json"}
login_data = {"mobile": "13632296409",
              "password": "@12345678",
              "captchaCode": None,
              "remember": True,
              "captchaToken": None,
              "invitationCode": None,
              "operateSource": "WebCustomer",
              "loginScene": "Normal"}
login_data_json = json.dumps(login_data)  # 需要将 请求参数
# 登录系统
login_res = requests.post(login_url, headers=login_headers, data=login_data_json)
login_res_json = login_res.json()
print(login_res_json)
# 获取 token 信息
accountToken = login_res_json["data"]["accountToken"]
employeeToken = "Bearer " + login_res_json["data"]["employeeToken"]
print(employeeToken)
# post 请求获取数据的方式不同于 get，post 请求数据必须要 构建请求头才可以

# 查询酒店
search_hotel_url = "https://test-web-te-yi-xing-env-1.teyixing.com/tmc-customer-api-gateway/domestic-hotel-resource/front/v1/hotelSearch/searchHotels"
search_hotel_headers = {"content-type": "application/json", "accounttoken": accountToken, "authorization": employeeToken}
search_hotel_data = {"checkDateRange":["2021-12-22","2021-12-23"],"cityCode":"4403","keyWord":None,"checkInDate":"2021-12-22","checkOutDate":"2021-12-23","orderBy":"Default","condition":{"brands":[],"priceRanges":[]},"searchProtocolType":"All"}
search_hotel_data_json = json.dumps(search_hotel_data)
# search_hotel_data_json = json.dumps(search_hotel_data, ensure_ascii=False, skipkeys=True)


# 发起查询
search_hotel_res = requests.post(search_hotel_url, headers=search_hotel_headers, data=search_hotel_data_json)
print(search_hotel_data_json)
print(search_hotel_res.text)


