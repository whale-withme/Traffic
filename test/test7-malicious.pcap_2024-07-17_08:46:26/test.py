import pandas as pd
import json

# 读取原始 CSV 文件
input_csv_file = 'flows.csv'

# 读取 CSV 文件，假设没有表头
df = pd.read_csv(input_csv_file, header=None, quotechar='"')

# 提取 JSON 数据并转换为字典
def extract_json_data(json_str):
    try:
        # 解析 JSON 数据
        data = json.loads(json_str.replace('""', '"'))
        # 提取所需字段
        return {
            'starttime': data.get('starttime'),
            'dur': data.get('dur'),
            'saddr': data.get('saddr'),
            'sport': data.get('sport'),
            'daddr': data.get('daddr'),
            'dport': data.get('dport'),
            'proto': data.get('proto'),
            'origstate': data.get('SRPA_SPA'),
            'state': data.get('state'),
            'pkts': data.get('spkts'),
            'allbytes': data.get('sbytes', 0) + data.get('dbytes', 0),
            'spkts': data.get('spkts'),
            'sbytes': data.get('sbytes'),
            'appproto': data.get('appproto'),
            'label': 'Normal',  # 从原始数据中获取
            'module_labels': {"flowalerts-long-connection": "Normal"} # 从原始数据中获取
        }
    except json.JSONDecodeError:
        return {}

# 处理每一行数据并创建字典
processed_data = []
for index, row in df.iterrows():
    json_data = row[1]
    extracted_data = extract_json_data(json_data)
    # 添加其他字段
    extracted_data['uid'] = row[0]
    extracted_data['classification'] = row[2]
    extracted_data['profile'] = row[3]
    extracted_data['timewindow'] = row[4]
    extracted_data['hash'] = row[5]
    processed_data.append(extracted_data)

# 返回处理后的数据字典
data_dict = {'flows': processed_data}

# 打印字典
import pprint
pprint.pprint(data_dict)

# 如果需要将字典保存为 JSON 文件，可以使用以下代码：
# import json
# with open('processed_flows.json', 'w') as f:
#     json.dump(data_dict, f, indent=4)

