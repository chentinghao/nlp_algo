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


