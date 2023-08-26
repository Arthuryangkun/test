import csv
import os.path
from collections import Counter
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import json


# data = np.load("./Wiki/ent2vec.npy")

def get_two_data():
    df = pd.read_csv('./drug_disease_drug/drug_disease_drug.txt', header=None)
    data = df.iloc[:, 1].tolist()

    # 统计第二列数据中相同值出现的次数
    counts = df.iloc[:, 1].value_counts()

    # 获取出现次数大于等于120的值
    big_values = counts[counts >= 120].index.tolist()

    # 将第二列值在出现次数大于等于120的列表中的数据保存到一个txt文件中
    # 剩下的数据保存到另一个txt文件中
    big_data = df[df.iloc[:, 1].isin(big_values)]
    small_data = df[~df.iloc[:, 1].isin(big_values)]

    # 写入txt文件
    if not big_data.empty:
        big_data.to_csv('big_data.txt', sep=',', index=False, header=False)
    if not small_data.empty:
        small_data.to_csv("small_data.txt", sep=',', index=False, header=False)


# split_data = pd.read_csv('small_data.txt', header=None)
# train, test = train_test_split(split_data, test_size=0.15, random_state=42)
# train, dev = train_test_split(train, test_size=0.1764, random_state=42)
#
# train.to_csv(os.path.join("train.txt"), index=False, header=False)
#
# test.to_csv(os.path.join("test.txt"), index=False, header=False)
#
# dev.to_csv(os.path.join("dev.txt"), index=False, header=False)


# for row in data:
#     my_data.append(row[1])
#
# counts = Counter(data)
# big_values = [value for value, count in counts.items() if count >= 120]
#
# big_data = []
# small_data = []
# for row in data:
#     if row[1] in big_values:
#         big_data.append(row)
#     else:
#         small_data.append(row)
#
# big_data.to_csv(os.path.join('big_data.txt'), index=False, header=False, sep=',')
# small_data.to_csv(os.path.join('small_data.txt'), index=False, header=False, sep=',')

# path_graph_lines = open('./big_data.txt').readlines()
# entity = set()
# path_graph = []
# for line in path_graph_lines:
#     triple = line.strip().split(',')
#     entity.add(triple[0])
#     entity.add(triple[2])
#     path_graph.append(triple)
# json.dump(path_graph, open('./drug_disease_drug/path_graph.json', 'w'))


# 读取ent2id文件
# ent2id = {}
# with open('./drug_disease_drug/data_300/ent2ids', 'r') as f:
#     line = f.readline().strip()  # 读取一行数据并去除空白符
#     entities = line.split(',')  # 按照逗号分隔数据，得到一个包含所有实体的列表
#     ent2id = {e: i for i, e in enumerate(entities)}  # 构建实体到ID的映射
#
# # 读取train.txt文件
# with open('./drug_disease_drug/drug_disease_drug.txt', 'r') as f:
#     for line in f:
#         head, _, tail = line.strip().split(',')
#         # 如果head或tail不在ent2id中，则将其加入
#         if head not in ent2id:
#             ent2id[head] = len(ent2id)
#         if tail not in ent2id:
#             ent2id[tail] = len(ent2id)
#
# # 将更新后的字典存储到ent2id文件中
# # with open('./drug_disease_drug/data_300/ent2ids', 'w') as f:
# #     for ent, id in ent2id.items():
# #         f.write(f'{ent}\t{id}\n')


if __name__ == '__main__':
    get_two_data()
