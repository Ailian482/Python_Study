# -*- coding:utf-8 -*-
# 作   者：Ailian
# 开发时间：2025/4/18 16:26

"""
JsonPath 是一种用于 JSON 数据中定位和提取特定元素的表达方式语言，其作用类似于 XPath 在 XML 数据中的作用，通过 JsonPath 表达式，可以方便地从 JSON 对象或数组汇总获取所需的数据。可以帮助我们高效地定位和提取所需的数据。
JsonPath 语法基础：
根节点与子节点的访问
- 根节点: 使用 $ 表示根节点,它代表整个 JSON 数据.
- 子节点访问: 可以使用点号 . 或者中括号 [] 来访问子节点。
示例 JSON 数据:

"""

from jsonpath_ng import jsonpath, parse

json_data = {
    "code": 0,
    "message": "OK",
    "data": {
        "queryId": "9b6d39c8-b25c-4519-8b82-2f3266cb5646",
        "queryKey": "5d3a706d-ecdd-43aa-b5fa-ec7e91a642a4",
        "fromStation": None,
        "fromStationCode": None,
        "toStation": None,
        "toStationCode": None,
        "trainDate": "2025-04-30",
        "trainInfoList": [
            {
                "serialNumber": 1,
                "trainNo": "C7298",
                "trainNoOf12306": "6i000C729800",
                "fromTime": "07:00",
                "toTime": "07:19",
                "fromStation": "深圳北",
                "fromStationPinYin": "shenzhenbei",
                "fromStationCode": "IOQ",
                "fromCityCode": "4403",
                "fromCityName": "深圳",
                "toStation": "深圳坪山",
                "toStationPinYin": "shenzhenpingshan",
                "toStationCode": "IFQ",
                "toCityCode": "4403",
                "toCityName": "深圳",
                "runTimeSpan": "19",
                "fromPassType": 0,
                "toPassType": 2,
                "canBuyNow": True,
                "trainClass": "C",
                "trainClassName": "城际高速",
                "tickets": [
                    {
                        "seatType": "secondSeat",
                        "seatName": "二等座",
                        "price": 16,
                        "seatState": 1,
                        "seats": 21,
                        "upPrice": 16,
                        "midPrice": None,
                        "downPrice": 16
                    },
                    {
                        "seatType": "firstSeat",
                        "seatName": "一等座",
                        "price": 26,
                        "seatState": 1,
                        "seats": 21,
                        "upPrice": 26,
                        "midPrice": None,
                        "downPrice": 26
                    },
                    {
                        "seatType": "noSeat",
                        "seatName": "无座",
                        "price": 16,
                        "seatState": 1,
                        "seats": 21,
                        "upPrice": 16,
                        "midPrice": None,
                        "downPrice": 16
                    }
                ],
                "accessByIdCard": False,
                "saleFlag": "0",
                "saleDateTime": "",
                "wasMtr": False
            },
            {
                "serialNumber": 2,
                "trainNo": "D674",
                "trainNoOf12306": "6i0000D6742B",
                "fromTime": "07:16",
                "toTime": "07:33",
                "fromStation": "深圳北",
                "fromStationPinYin": "shenzhenbei",
                "fromStationCode": "IOQ",
                "fromCityCode": "4403",
                "fromCityName": "深圳",
                "toStation": "深圳坪山",
                "toStationPinYin": "shenzhenpingshan",
                "toStationCode": "IFQ",
                "toCityCode": "4403",
                "toCityName": "深圳",
                "runTimeSpan": "17",
                "fromPassType": 0,
                "toPassType": 1,
                "canBuyNow": False,
                "trainClass": "D",
                "trainClassName": "动车组",
                "tickets": [
                    {
                        "seatType": "secondSeat",
                        "seatName": "二等座",
                        "price": 16,
                        "seatState": 0,
                        "seats": 0,
                        "upPrice": 16,
                        "midPrice": None,
                        "downPrice": 16
                    },
                    {
                        "seatType": "firstSeat",
                        "seatName": "一等座",
                        "price": 26,
                        "seatState": 0,
                        "seats": 0,
                        "upPrice": 26,
                        "midPrice": None,
                        "downPrice": 26
                    },
                    {
                        "seatType": "noSeat",
                        "seatName": "无座",
                        "price": 16,
                        "seatState": 0,
                        "seats": 0,
                        "upPrice": 16,
                        "midPrice": None,
                        "downPrice": 16
                    }
                ],
                "accessByIdCard": False,
                "saleFlag": "0",
                "saleDateTime": "",
                "wasMtr": False
            }
        ],
        "fromStations": [
            {
                "station": "深圳北",
                "stationCode": "IOQ"
            },
            {
                "station": "福田",
                "stationCode": "NZQ"
            }
        ],
        "toStations": [
            {
                "station": "深圳坪山",
                "stationCode": "IFQ"
            }
        ],
        "canBookTime": None
    }
}
# 定义 JSONPath 表达式
jsonpath_expression = parse('$.data.trainInfoList[*].trainNo')

# 查找匹配的结果
matches = [match.value for match in jsonpath_expression.find(json_data)]
for match in jsonpath_expression.find(json_data):
    print(type(match))

# 输出结果
print("车次号:", matches)