import numpy as np
from sklearn.model_selection import train_test_split
import csv
import pandas as pd
import os.path
import json

# 假设 triples 是所有的三元组，格式为：(实体1,关系,实体2)
# triples = [(e1, r, e2), ...]
# triples = pd.read_csv('small_data.txt', header=None)
with open('small_data.txt') as f:
    triples = f.readlines()
# 使用字典将三元组按关系分组
triples_grouped_by_relation = {}
for line in triples:
    line = line.rstrip().split(',')
    r = line[1]
    e1 = line[0]
    e2 = line[2]
    if r not in triples_grouped_by_relation:
        triples_grouped_by_relation[r] = []
    triples_grouped_by_relation[r].append((e1, r, e2))

# 按关系对应的三元组数量从大到小排序
sorted_relations = sorted(triples_grouped_by_relation.keys(), key=lambda r: len(triples_grouped_by_relation[r]),
                          reverse=True)

# 分割数据为训练集、验证集和测试集
train_set = {}
val_set = {}
test_set = {}

relations = list(sorted_relations)
# np.random.shuffle(relations)

# 比例
train_ratio = 0.7
val_ratio = 0.1
test_ratio = 0.2

num_relations = len(relations)
train_relations = relations[:int(train_ratio * num_relations)]
val_relations = relations[int(train_ratio * num_relations):int((train_ratio + val_ratio) * num_relations)]
test_relations = relations[int((train_ratio + val_ratio) * num_relations):]

# for r in train_relations:
#     train_set[r] = triples_grouped_by_relation[r]

# for r in val_relations:
#     val_set[r] = triples_grouped_by_relation[r]
#
# for r in test_relations:
#     test_set[r] = triples_grouped_by_relation[r]


# 过滤train_set中value数量大于5的项
train_set_filtered = {r: triples_grouped_by_relation[r] for r in train_relations if
                      len(triples_grouped_by_relation[r]) > 5}

# # 分割数据为train、test和dev集合
# train_set = {}
# test_set = {}
# val_set = {}


def split_dict_by_key(dictionary, train_ratio, dev_ratio):
    keys = list(dictionary.keys())
    # random.shuffle(keys)

    total_len = len(keys)
    train_len = int(total_len * train_ratio)
    dev_len = int(total_len * dev_ratio)

    train_keys = keys[:train_len]
    dev_keys = keys[train_len:(train_len + dev_len)]
    test_keys = keys[(train_len + dev_len):]

    train_dict = {key: dictionary[key] for key in train_keys}
    dev_dict = {key: dictionary[key] for key in dev_keys}
    test_dict = {key: dictionary[key] for key in test_keys}

    return train_dict, dev_dict, test_dict

train_ratio = 0.7  # 训练集比例
dev_ratio = 0.1    # 开发集比例，剩下的比例会分给测试集

train_set, dev_set, test_set = split_dict_by_key(train_set_filtered, train_ratio, dev_ratio)

json.dump(train_set, open('./try300/train_tasks.json', 'w'))
json.dump(test_set, open('./try300/test_tasks.json', 'w'))
json.dump(dev_set, open('./try300/dev_tasks.json', 'w'))

def bubble_sort()
