# coding: utf-8
# Author: zhenda
from functools import wraps
from time import perf_counter
import logging

logger = logging.getLogger(__name__)


def timecalc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = perf_counter()
        res = func(*args, **kwargs)
        et = perf_counter()
        logger.debug('%s 耗时为 %s', func.__name__, et - st)
        return res

    return wrapper
