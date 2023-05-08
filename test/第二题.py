import csv
import math
list1=[]
with open('fyx_chinamoney.csv',"r",encoding="utf-8",) as csvfile:
    data_list = csvfile.readlines()
    for data in data_list:
        list1.append(data.strip("\n"))
    #用csv库读取
    # rows=csv.reader(csvfile)
    # for row in rows:
    #     list=list+row
for i in range(math.ceil(len(list1)/80)):

    print(list1[i: i+80])
