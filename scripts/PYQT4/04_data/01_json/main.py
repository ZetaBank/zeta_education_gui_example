# -*- coding: utf-8 -*-

import json

data = {"name": "John", "age": 30, "city": "New York"}

# 데이터 저장
with open("data.json", "w") as file:
    json.dump(data, file)

# 데이터 읽기
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
