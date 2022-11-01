# coding: utf-8
# Author: zhenda
import os


def gene_fold(fold):
    if not os.path.exists(fold):
        os.makedirs(fold)