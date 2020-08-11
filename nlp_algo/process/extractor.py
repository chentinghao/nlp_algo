# -*- coding: utf-8 -*-
# @author: Ting-Hao Chen
# @date: 2020/08/10

import re
import itertools


class Extractor(object):
    def __init__(self):
        pass

    def extract_email(self, text):
        email_pattern = r"^[\.a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z_-]+)+$"
        if text == "":
            return []
        text_en = self.remove_chinese(text)
        text_en = text_en.replace(" at ", "@").replace(" dot ", ".")
        sep = ",!?:; ，。！？《》、|\\/"
        text_en_split = ["".join(g) for k, g in itertools.groupby(text_en, sep.__contains__) if not k]
        email_list = []
        for eng_text in text_en_split:
            result = re.match(email_pattern, eng_text, flags=0)
            if result:
                email_list.append(result.string)
        return email_list

    def remove_chinese(self, text):
        if text == "":
            return []
        pattern = re.compile(u"[\u4E00-\u9FA5]")
        return pattern.sub(r" ", text)


if __name__ == '__main__':

    text = "我的信息：18312345678，183-1234-5678，hello.world@gmail.com and find.me at gmail dot com"
    extractor = Extractor()
    email_list = extractor.extract_email(text)



