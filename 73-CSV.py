import json
import csv

# json->csv
# 1.分别读，创建文件
json_fp = open('02data.json', 'r')
csv_fp = open('03.csv', 'w', encoding='utf-8')
# 2.提出表头，表内容
data_list = json.load(json_fp)
sheet_title = data_list[0].keys()  # 表头
# 把表头改为中文
# sheet_title = {"姓名","年龄"}
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())  # 表内容
# 3.csv写入器
writer = csv.writer(csv_fp)
# 4.写入表头
writer.writerow(sheet_title)  # 表头单个
# 5.写入内容
writer.writerows(sheet_data)  # 表内容有多个，用writerows
# 6.关闭文件
json_fp.close()
csv_fp.close()
