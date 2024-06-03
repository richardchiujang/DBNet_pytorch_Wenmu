"""
dbnet pytorch implementation
after datasets files ready, run this script to generate train.txt and test.txt file
from dataset folder generate train.txt and test.txt file
這檔案是直接在datasets資料夾更新train.txt和test.txt檔案
"""

import os, glob

def gen_txtfile_from_dataset_fd(dataset_folder=r'.\datasets'):

    test_list = []
    test_txt = 'test.txt'
    test_list = glob.glob(os.path.join(dataset_folder, 'test', 'gt', '*.txt'))
    f = open(r'.\datasets\test.txt', 'w', encoding='utf-8')
    for item in test_list:
        f.write("{}\t{}\n".format(item.replace('gt', 'img').replace('.txt', '.jpg'), item))
    f.close()

    train_list = []
    train_txt = 'train.txt'
    train_list = glob.glob(os.path.join(dataset_folder, 'train', 'gt', '*.txt'))
    f = open(r'.\datasets\train.txt', 'w', encoding='utf-8')
    for item in train_list:
        f.write("{}\t{}\n".format(item.replace('gt', 'img').replace('.txt', '.jpg'), item))
    f.close()


gen_txtfile_from_dataset_fd()
print('done')