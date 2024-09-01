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
    vehicle_dict = {}
    for vehicle in vehicles_data:
        if 'manufacturerName' in vehicle:
            if vehicle['manufacturerName'] in vehicle_dict:
                vehicle_dict[vehicle['manufacturerName']].append(vehicle)
            else:
                vehicle_dict[vehicle['manufacturerName']] = [vehicle]
        #未分類 資料清洗 不列入
    return vehicle_dict

def data_trs_json(data):
    json_data = json.dumps(data, ensure_ascii=False, indent=4)
    with open('./output.json', 'w', encoding='utf-8') as file:
        file.write(json_data)
    return 'ok'

def print_replace(target_data, indenta_str):
    data_type = type(target_data)
    if data_type is list and target_data != []:
        for element in target_data:
            if type(element) is not list and type(element) is not dict:
                print(element)
            else:
                print_replace(element, indenta_str)

    if data_type is dict and target_data != {}:
        print(indenta_str, end="")
        for key, val in target_data.items():
            if type(val) is not list and type(val) is not dict:
                print(f'{key}:{val}', end=', ')
            else:
                res_str = key + ":"
                print(res_str)
                print_replace(val, indenta_str+"\t")
        print()
    return

def print_json(data, indent=0):
    spaces = ' ' * (indent * 4)
    if isinstance(data, dict):
        print(spaces + '{')
        for i, (key, value) in enumerate(data.items()):
            print(f"{spaces}    \"{key}\": ", end='')
            if isinstance(value, (dict, list)):
                print()
                print_json(value, indent + 1)
            else:
                if isinstance(value, str):
                    print(f"\"{value}\"", end='')
                else:
                    print(value, end='')
            if i < len(data) - 1:
                print(',')
            else:
                print()
        print(spaces + '}', end='')
    elif isinstance(data, list):
        print(spaces + '[')
        for i, item in enumerate(data):
            if isinstance(item, (dict, list)):
                print_json(item, indent + 1)
            else:
                if isinstance(item, str):
                    print(f"{spaces}    \"{item}\"", end='')
                else:
                    print(f"{spaces}    {item}", end='')
            if i < len(data) - 1:
                print(',')
            else:
                print()
        print(spaces + ']', end='')
    else:
        print(data, end='')


if __name__ == "__main__":
    input_data = read_data()
    vehicles_data = input_data['vehicles']
    vehicle_dict = data_replace(vehicles_data)
    save_res = data_trs_json(vehicle_dict)
    print(save_res)
    print_json(vehicle_dict)