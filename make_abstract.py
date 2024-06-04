import json

# 假設 JSON 資料存儲在 'data.json' 文件中
with open('EX.json', 'r') as json_file:
    data = json.load(json_file)

# 提取需要的欄位
fields = ['Name', 'City']

# 開啟 TSV 檔案進行寫入
with open('output.tsv', 'w', newline='', encoding='utf-8') as tsv_file:
    # 寫入標題行
    tsv_file.write('\t'.join(fields) + '\n')
    
    # 寫入每一行的資料
    for entry in data:
        tsv_file.write('\t'.join(str(entry[field]) for field in fields) + '\n')

print("TSV 檔案已成功生成")