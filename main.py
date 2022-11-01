# coding: utf-8
# Author: zhenda
from src.gen_word_cloud import *
from src.utils.gene_fold import gene_fold
from src.utils.mylog import setlogging


if __name__ == '__main__':
    gene_fold('out')
    setlogging('out/main.log')
    words_list = read_words_bbe(file='resources/bbe.txt')
    stop_words = read_stop_words(file='resources/stop_words.txt')
    # res_dict = get_res_dict(words_list, stop_words)
    res_dict = get_res_dict2(words_list, stop_words)
    draw_word_img(res_dict, 'out/bbe_wordcloud.png')
