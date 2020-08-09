# -*- coding: utf-8 -*-
# @author: Ting-Hao Chen
# @date: 2020/08/09


import unittest
import pandas as pd
from nlp_algo.process.preprocessing import Remove


class TestRemove(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        df = pd.DataFrame()
        df["url"] = ["My github is https://github.com/"]
        df["pun"] = ["!'#$%&()*+-/:;<=>?@[\\]^_`{|}~"]
        df["num"] = ["1234567890"]
        df["space"] = ["a b c"]
        self.remove = Remove(df)

    def test_url(self):
        clean_df = self.remove.url(col_target="url", col_new=None)
        self.assertTrue("https://github.com/" not in clean_df["url"][0])

    def test_punctuation(self):
        punctuation = "!'#$%&()*+-/:;<=>?@[\\]^_`{|}~"
        clean_df = self.remove.punctuation(col_target="pun", col_new=None)
        self.assertTrue(punctuation not in clean_df["pun"][0])

    def test_number(self):
        clean_df = self.remove.number(col_target="num", col_new=None)
        self.assertTrue("1234567890" not in clean_df["num"][0])

    def test_space(self):
        clean_df = self.remove.space(col_target="space", col_new=None)
        self.assertTrue(" " not in clean_df["space"][0])

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

