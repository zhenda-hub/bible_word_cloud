# import sys
# print(sys.path)
import unittest
from src import gen_word_cloud, gene_fold
import os


class TestWc(unittest.TestCase):
    out_path = 'out'

    @classmethod
    def setUpClass(cls) -> None:
        gene_fold.gene_fold(cls.out_path)

    def test_read_words(self):
        words_gene = gen_word_cloud.read_words(file='resources/sub_bbe.txt')
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


if __name__ == '__main__':
    unittest.main()
