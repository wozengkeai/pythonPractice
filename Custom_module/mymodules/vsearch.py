# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/6 14:39
@Auth ： zengxiaoyan
@File ：vsearch.py
"""
def search4vowels(phrase:str) -> set:
    """
    return any vowels found in a supplied phrase.
    :param phrase:
    :return:
    """
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str,letters:str='aeiou') -> set:
    """
    return a set of the 'letters' found in 'phrase'.
    :param phrase:
    :param letters:
    :return:
    """
    return set(letters).intersection(set(phrase))