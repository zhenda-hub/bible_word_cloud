# coding: utf-8
# Author: zhenda
# Time  ：2022/10/28 7:11
import os.path

import jieba
from collections import Counter
# import matplotlib.pyplot as plt
from wordcloud import WordCloud
from src.utils.timecalc import timecalc
import pprint
from time import perf_counter
import pdb
import logging

logger = logging.getLogger(__name__)


@timecalc
def read_words(file):
    with open(file, 'r', encoding='u8') as wf:
        words_list = wf.read()
    words_gene = jieba.cut(words_list)
    # words_list = jieba.lcut(words_list)
    return words_gene


@timecalc
def read_words_bbe(file):
    all_line = ''
    with open(file, 'r', encoding='u8') as wf:
        for line in wf:
            one_line = ' '.join(line.split()[2:])
            all_line += one_line + ' '

    words_gene = jieba.cut(all_line)
    # words_list = jieba.lcut(all_line)
    return words_gene
    # return words_list


@timecalc
def read_words_hgb(file):
    all_line = ''
    with open(file, 'r', encoding='gbk') as wf:
        for line in wf:
            one_line = ' '.join(line.split()[2:])
            all_line += one_line + ' '

    words_gene = jieba.cut(all_line)
    return words_gene


@timecalc
def read_stop_words(file):
    with open(file, 'r', encoding='u8') as wf:
        stop_words = wf.read()

    stop_words = stop_words.split('\n')  # str转list
    stop_words.append('\n')
    stop_words.append('\u3000')
    # print(stop_words)
    return stop_words


@timecalc
def get_res_dict(words_gene, stop_words):
    words_dict = Counter(words_gene)
    # pdb.set_trace()
    all_key = set(words_dict.keys())  # 循环删除key， 一定要用list， 不能原地修改
    for k in (all_key & set(stop_words)):
        words_dict.pop(k)

    final_list = words_dict.most_common(200)
    final_dict = {}
    for item in final_list:
        final_dict[item[0]] = item[1]

    pprint.pprint(final_dict)  # 打印结果

    return final_dict


@timecalc
def draw_word_img(res_dict, out_file):
    word_cloud = WordCloud(
        width=1500,
        height=800,
        font_path="simkai.ttf",
        colormap='rainbow',
        background_color='white',
        # mask=mask
    )
    word_cloud.generate_from_frequencies(res_dict)
    word_cloud.to_file(out_file)
    addr = os.path.abspath(out_file)

    logger.info('生成图片 %s', addr)
    return addr
