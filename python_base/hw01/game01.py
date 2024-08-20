import json

file_path = 'data.json'

def read_data():
    # 打開檔案並讀取內容
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        file_content = file_content.replace('\xa0', ' ')
        data = json.loads(file_content)
    # 現在 data 變數中保存著 JSON 檔案的資料，可以直接操作
    return data

def data_replace(vehicles_data):
    print(vehicles_data)
    '''
    請完成這個function !
    將我剛剛爬下來的gta線上模式的載具品牌跟名稱進行分類使用字典dict
    key為品牌名稱 value為list載具名稱
    例如{
        '浪子':['柒-70', 'JB 700W', ..],
        '古羅帝':['義塔力 GTO', '披治崇敬'..]
        }
    return dict給輸出
    '''
    pass

if __name__ == "__main__":
    input_data = read_data()
    vehicles_data = input_data['vehicles']
    data_dict = data_replace(vehicles_data)
    print(data_dict)