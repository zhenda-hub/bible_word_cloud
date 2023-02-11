# coding: utf-8
# Author: zhenda
from src.gen_word_cloud import *
from src.gen_word_cloud_echarts import gene_wc_echarts, dict2list
from src.utils.gene_fold import gene_fold
from src.utils.mylog import setlogging


def gene_bbe(num):
    words_list = read_words_bbe(file='resources/bbe.txt')
    stop_words = read_stop_words(file='resources/stop_words.txt')
    res_dict = get_res_dict(words_list, stop_words)
    for i in range(num):
        draw_word_img(res_dict, f'out/bbe_wordcloud{i}.png')


def gene_hgb(num):
    words_list = read_words_hgb(file='resources/hgb.txt')
    stop_words = read_stop_words(file='resources/stop_words.txt')
    res_dict = get_res_dict(words_list, stop_words)
    for i in range(num):
        draw_word_img(res_dict, f'out/hgb_wordcloud{i}.png')


def gene_bbe_echarts():
    words_list = read_words_bbe(file='resources/bbe.txt')
    stop_words = read_stop_words(file='resources/stop_words.txt')
    res_dict = get_res_dict(words_list, stop_words)
    res_lst = dict2list(res_dict)
    gene_wc_echarts(res_lst, f'out/bbe_wordcloud.html')


def gene_hgb_echarts():
    words_list = read_words_hgb(file='resources/hgb.txt')
    stop_words = read_stop_words(file='resources/stop_words.txt')
    res_dict = get_res_dict(words_list, stop_words)
    res_lst = dict2list(res_dict)
    gene_wc_echarts(res_lst, f'out/hgb_wordcloud.html')


if __name__ == '__main__':
    gene_fold('out')
    setlogging('out/main.log')

    # gene_bbe(2)
    # gene_hgb(2)

    gene_bbe_echarts()
    gene_hgb_echarts()