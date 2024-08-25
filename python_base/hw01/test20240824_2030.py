import json

import os
print(os.getcwd()) #確認當前資料夾位置

file_path = './data.json'

def read_data():
    # 打開檔案並讀取內容
    with open(file_path, 'r', encoding='utf-8') as file:

        file_content = file.read()

        file_content = file_content.replace('\xa0', ' ')

        data = json.loads(file_content)
    # 現在 data 變數中保存著 JSON 檔案的資料，可以直接操作

    if file.closed:
	    print("file is closed")
    else:
	    print("file is still not closed")

    return data



def data_replace(vehicles_data):

    print(vehicles_data)
    #....

    pass

if __name__ == "__main__":

    input_data = read_data()

    vehicles_data = input_data['vehicles']

    data_dict = data_replace(vehicles_data)

    print(data_dict)

