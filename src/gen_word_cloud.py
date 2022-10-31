# coding: utf-8
# Author: zhenda
# Time  ：2022/10/28 7:11
import jieba
from collections import Counter
# import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pprint
import pdb


def read_words(file):
    with open(file, 'r', encoding='u8') as wf:
        words_list = wf.read()
    words_gene = jieba.cut(words_list)
    # words_list = jieba.lcut(words_list)
    return words_gene


def read_words_bbe(file):
    words_list = []
    with open(file, 'r', encoding='u8') as wf:
        words_oneline = wf.readline()
        pdb.set_trace()

    words_gene = jieba.cut(words_list)
    # words_list = jieba.lcut(words_list)
    return words_gene


def read_stop_words(file):
    with open(file, 'r', encoding='u8') as wf:
        stop_words = wf.read()

    stop_words = stop_words.split('\n')  # str转list
    stop_words.append('\n')
    stop_words.append('\u3000')
    # print(stop_words)
    return stop_words


def get_res_dict(words_gene, stop_words):
    res_list = []
    for item in words_gene:
        if item not in stop_words:
            res_list.append(item)

    res_dict = Counter(res_list)
    final_list = res_dict.most_common(200)
    final_dict = {}
    for item in final_list:
        final_dict[item[0]] = item[1]
    # pprint.pprint(final_dict)

    return final_dict


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
    return out_file



