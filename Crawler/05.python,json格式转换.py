import json


#Python转json

json_str='{"name":"美国","province":"GoldenStates","number":123456}'
python_dict=json.loads(json_str)
print(python_dict)
#文件形式
with open('/data/test_w.json') as f:
    python_list=json.load(f)
    print(python_list)


#json转Python
json_str=json.dumps(python_dict,ensure_ascii=False)
print(json_str)
#Python数据以json文件写入
with open('/data/test_w.json', mode='w')as f:
    json.dump(python_dict,f,ensure_ascii=False)