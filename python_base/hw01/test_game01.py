import json

file_path = './data.json'
#內部資料範例 {"modelName": "驚駭位元","manufacturerName": "貝飛特","plateStyle": "orangeBlue"}

def read_data():
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read().replace('\xa0', ' ')
        return json.loads(file_content)

def data_replace(vehicles_data): 
    #建立data_replace函數，由於(vehicles_data) 故此函數需要vehicles_data參數

    categorized_data = {} #建立新字典

    for vehicle in vehicles_data: 
        #使用vehicle 從 if __name__ == "__main__" 這下 獲取 input_data['vehicles']

        manufacturer = vehicle.get('manufacturerName') 
        #從{"modelName":"型號" ,"manufacturerName":"廠牌" ,"plateStyle":"顏色"}
        #獲取第二key 及其value 

        if manufacturer: 
            #判斷 是否 有manufacturer這項第二key 

            if manufacturer not in categorized_data:
                #判斷 manufacturer 這項第二key 如不在categorized_data資料庫中 則進入下一行執行
                
                categorized_data[manufacturer] = []
                #建立空list
                #例:當前vehicle資料中 manufacturer鍵值 的 value是貝菲特
                #結果會得到 categorized_data = { "貝飛特": [] }

            categorized_data[manufacturer].append(vehicle)
            #將當前vehicle中取的值 存到對應manufacturer[]的資料中
            #例:當前manufacturer是貝菲特 數據{"modelName": "驚駭位元","manufacturerName": "貝飛特","plateStyle": "orangeBlue"}
            #其結果為 categorized_data = { "貝飛特": [{"modelName": "驚駭位元", "manufacturerName": "貝飛特", "plateStyle": "orangeBlue"}] }

        else:
            #如判斷ditc中沒有manufacturer鍵值則進入else

            print(f"缺少 manufacturerName 的車輛: {vehicle}")
            #如ditc中沒有manufacturer鍵值 {"modelName": "黑神","plateStyle": "yellowBlack"}
            #例{"modelName": "黑神","plateStyle": "yellowBlack"}將直接印出

    return categorized_data
    #使用data_replace(vehicles_data)呼叫此函數，將從vehicle提取的數據categorized_data結果輸出

if __name__ == "__main__":
    input_data = read_data()
    #將data內容匯入 input_data 變數中

    vehicles_data = input_data['vehicles']
    #將 input_data 內容的 vehicles鍵值下的 內容都匯入 vehicles_data

    data_dict = data_replace(vehicles_data)
    #使用 data_replace(vehicles_data)函數 將其輸出的categorized_data內容匯入data_dict

transformed_data = {
    manufacturer: [item["modelName"] for item in models]
    for manufacturer, models in data_dict.items()
}
print(json.dumps(transformed_data, ensure_ascii=False, indent=4))