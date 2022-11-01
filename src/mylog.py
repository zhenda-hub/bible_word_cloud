# coding: utf-8
# Author: zhenda
import logging


def setlogging(outfile):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    fh_formatter = logging.Formatter('[%(asctime)s] %(name)s - %(lineno)s  - %(levelname)s - %(message)s')
    sh_formatter = logging.Formatter('%(name)s - %(lineno)s - %(levelname)s - %(message)s')

    fh = logging.FileHandler(filename=outfile, encoding='u8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fh_formatter)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(sh_formatter)

    logger.addHandler(fh)
    logger.addHandler(sh)


