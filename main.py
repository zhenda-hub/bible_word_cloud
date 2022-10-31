# coding: utf-8
# Author: zhenda
from src.gen_word_cloud import *
from src.gene_fold import gene_fold

if __name__ == '__main__':
    gene_fold('out')
    words_list = read_words(file='resources/sub_bbe.txt')
    stop_words = read_stop_words(file='resources/stop_words.txt')
    res_dict = get_res_dict(words_list, stop_words)
    draw_word_img(res_dict, 'out/sub_bbe_wordcloud.png')
