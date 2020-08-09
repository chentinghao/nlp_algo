# -*- coding: utf-8 -*-
# @author: Ting-Hao Chen
# @date: 2020/08/09


import re


class Remove(object):
    def __init__(self, df):
        self.df = df

    def url(self, col_target, col_new=None):
        if col_new is None:
            col_new = col_target
        self.df[col_new] = self.df[col_target].apply(lambda x: re.sub(r"http\S+", "", x))
        return self.df

    def punctuation(self, col_target, col_new=None):
        punctuation = "!'#$%&()*+-/:;<=>?@[\\]^_`{|}~"
        if col_new is None:
            col_new = col_target
        self.df[col_new] = self.df[col_target].apply(lambda x: "".join(ch for ch in x if ch not in set(punctuation)))
        return self.df

    def number(self, col_target, col_new=None):
        if col_new is None:
            col_new = col_target
        self.df[col_new] = self.df[col_target].str.replace("[0-9]", "")
        return self.df

    def space(self, col_target, col_new=None):
        if col_new is None:
            col_new = col_target
        self.df[col_new] = self.df[col_target].apply(lambda x: "".join(x.split()))
        return self.df

