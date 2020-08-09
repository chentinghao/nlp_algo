# -*- coding: utf-8 -*-
# @author: Ting-Hao Chen
# @date: 2020/08/09


import re
import spacy


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

    def lemma(self, col_target, col_new=None):
        if col_new is None:
            col_new = col_target
        nlp = spacy.load("en", disable=["parser", "ner"])
        series = []
        for i in self.df[col_target]:
            s = [token.lemma_ for token in nlp(i)]
            series.append(" ".join(s))
        self.df[col_new] = series
        return self.df


if __name__ == "__main__":
    import pandas as pd

    df = pd.DataFrame()
    df["url"] = ["My github is https://github.com/"]
    df["pun"] = ["!'#$%&()*+-/:;<=>?@[\\]^_`{|}~"]
    df["num"] = ["1234567890"]
    df["space"] = ["a b c"]
    df["lemma"] = ["produces"]

    remove = Remove(df)
    df_clean = remove.url(col_target="url", col_new="url_new")
    df_clean = remove.punctuation(col_target="pun", col_new="pun_new")
    df_clean = remove.number(col_target="num", col_new="num_new")
    df_clean = remove.space(col_target="space", col_new="space_new")
    df_clean = remove.space(col_target="lemma", col_new="lemma_new")



