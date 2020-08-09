# -*- coding: utf-8 -*-
# @author: Ting-Hao Chen
# @date: 2020/08/09


import pickle
import tensorflow as tf
import pandas as pd
import numpy as np
import tensorflow_hub as hub


model_path = "https://tfhub.dev/google/elmo/2"


def elmo_vectors(df, col_target, save_path=None):
    def gen_vectors(series):
        tf.compat.v1.disable_eager_execution()
        model = hub.Module(model_path, trainable=True)
        embed = model(series.tolist(), signature="default", as_dict=True)["elmo"]
        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            sess.run(tf.compat.v1.tables_initializer())

            # Return average of ELMo vectors
            return sess.run(tf.reduce_mean(embed, 1))

    batches = [df[i:i + 100] for i in range(0, len(df), 100)]
    vectors = np.concatenate([gen_vectors(batch[col_target]) for batch in batches], axis=0)

    if save_path is not None:
        open_file = open(save_path, "wb")
        pickle.dump(vectors, open_file)
        open_file.close()

    return vectors


if __name__ == "__main__":
    df = pd.DataFrame()
    df["text"] = ["iphone s iphone s iphone splus iphoneseller applestore ios iphone apple",
                  "new app for iphone , for the people who sail in italy appstore mobile apple travel holiday"]
    text = ["Roasted ants are a popular snack in Columbia"]
    vectors = elmo_vectors(df, col_target="text")

