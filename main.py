# coding: utf-8
# Author: zhenda
from src.gen_word_cloud import *
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


if __name__ == '__main__':
    gene_fold('out')
    setlogging('out/main.log')

    # gene_bbe(2)
    gene_hgb(2)