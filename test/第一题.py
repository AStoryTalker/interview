import requests
import json
import csv
#全局变量，用来存储所有解析到的数据
row_list=[]
def get_data(pageNo:int):
    """
    :param pageNo:页码
    """
    #data用来作为post请求的参数
    data = {
        'pageNo': pageNo,
        'pageSize':15,
        'bondType': 100001,
        'issueYear':2023
    }
    html1=requests.post('https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN',data=data)

    dict_data = json.loads(html1.text)


    for i in dict_data["data"]["resultList"]:
        row=[i["isin"], i["bondCode"], i["entyFullName"],i["bondType"] ,i["issueStartDate"], i["debtRtng"]]
        row_list.append(row)
    print(row_list)

if __name__ == '__main__':
    header_list = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]
    for i in range(1,4):
        get_data(i)

    with open('result.csv', 'w', encoding='utf-8',newline='') as file_obj:
        # 1:创建writer对象
        writer = csv.writer(file_obj)
        # 2:写表头
        writer.writerow(header_list)
        # 3:遍历列表，将每一行的数据写入csv
        for row in row_list:
            writer.writerow(row)

