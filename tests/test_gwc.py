# import sys
# import pprint
# pprint.pprint(sys.path)


import unittest
import pytest
from src import gen_word_cloud
from src.gen_word_cloud_echarts import gene_wc_echarts
from src.utils.gene_fold import gene_fold
import os
from src.utils.mylog import setlogging


class TestWc(unittest.TestCase):
    out_path = 'out'

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def test_read_words(self):
        words_gene = gen_word_cloud.read_words(file='resources/sub_bbe.txt')
        self.assertTrue(words_gene)

    def test_read_words_bbe(self):
        words_gene = gen_word_cloud.read_words_bbe(file='resources/sub_bbe.txt')
        self.assertTrue(words_gene)

    def test_read_stop_words(self):
        stop_words = gen_word_cloud.read_stop_words(file='resources/stop_words.txt')
        self.assertIsInstance(stop_words, list)

    def test_get_res_dict(self):
        words_gene = gen_word_cloud.read_words(file='resources/sub_bbe.txt')
        stop_words = gen_word_cloud.read_stop_words(file='resources/stop_words.txt')
        res_dict = gen_word_cloud.get_res_dict(words_gene, stop_words)
        self.assertIsInstance(res_dict, dict)

    def test_draw_word_img(self):
        res_dict = {
            'a': 2,
            'b': 2,
            'c': 10,
            'd': 4,
        }
        addr = gen_word_cloud.draw_word_img(res_dict, f'{self.out_path}/demo1.png')
        self.assertTrue(os.path.exists(addr))
        
    # @pytest.mark.skip
    def test_gene_wc_echarts(self):
        res_dict = [
            ('a', 2),
            ('b', 2),
            ('c', 10),
            ('d', 4),
            ('e', 14),
            ('f', 114),
            ('g', 43),
            ('h', 4),
            ('i', 24),
        ]
        addr = gene_wc_echarts(res_dict, f'{self.out_path}/demo1.html')
        self.assertTrue(os.path.exists(addr))


if __name__ == '__main__':
    gene_fold('out')
    setlogging('out/testWc.log')
    
    unittest.main()
