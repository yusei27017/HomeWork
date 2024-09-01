import json

#file_path = 'data.json'
file_path = './data.json'
#file_path = 'd:/my_project/HomeWork/python_base/hw01/data.json'

# import os
# print(os.getcwd())

def read_data():
    # 打開檔案並讀取內容
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        file_content = file_content.replace('\xa0', ' ')
        data = json.loads(file_content)
    # 現在 data 變數中保存著 JSON 檔案的資料，可以直接操作
    return data

def data_replace(vehicles_data):
    '''
    out
    {"古羅帝": [{"modelName": "X80 概念款","manufacturerName": "古羅帝","plateStyle": "blueWhite3"},
        {"modelName": "義塔力 RSX","manufacturerName": "古羅帝","plateStyle": "orangeBlue"}]

    "培羅": [{"modelName": "艾默瑞思","manufacturerName": "培羅","plateStyle": "blueWhite3"},
        {"modelName": "義塔力 GTB 改裝款","manufacturerName": "培羅","plateStyle": "orangeBlue"}]}
    '''
    res = {}
    for vehicle in vehicles_data:
        if 'manufacturerName' in vehicle:
            if vehicle['manufacturerName'] in res:
                res[vehicle['manufacturerName']].append(vehicle)
            else:
                res[vehicle['manufacturerName']] = [vehicle]
        #未分類 資料清洗 不列入
    return res

if __name__ == "__main__":
    input_data = read_data()
    vehicles_data = input_data['vehicles']
    data_dict = data_replace(vehicles_data)
    print(data_dict)