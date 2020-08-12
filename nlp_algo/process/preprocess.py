# -*- coding: utf-8 -*-
# @author: Ting-Hao Chen
# @date: 2020/08/09


from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def to_token(fit_text, text):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(fit_text)
    token = tokenizer.texts_to_sequences(text)
    return token


def pad(seq, maxlen):
    return pad_sequences(seq, maxlen=maxlen)


if __name__ == "__main__":
    fit_text = ["The earth is an awesome place to live"]
    text = ["The earth is an great place to live"]
    token = to_token(fit_text, text)

    seq = [[1, 2, 3, 4, 5]]
    seq_pad = pad(seq, maxlen=10)

    import hanlp
    tokenizer = hanlp.load('CTB6_CONVSEG')
    print(tokenizer('商品和服务'))

    tokenizer = hanlp.utils.rules.tokenize_english
    print(tokenizer("Don't go gentle into that good night."))

    print(tokenizer(['萨哈夫说，伊拉克将同联合国销毁伊拉克大规模杀伤性武器特别委员会继续保持合作。',
               '上海华安工业（集团）公司董事长谭旭光和秘书张晚霞来到美国纽约现代艺术博物馆参观。',
               'HanLP支援臺灣正體、香港繁體，具有新詞辨識能力的中文斷詞系統']))





