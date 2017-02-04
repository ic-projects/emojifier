from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model

from six import text_type
import os

def main():
    initializeModel()

def initializeModel():
    cwd = os.getcwd()
    save_dir = cwd + "/save/"
    print(save_dir)
    with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, True, useDropout=False)
    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        saver = tf.train.Saver(tf.all_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            print("Initalized")
            print(model.sample(sess, chars, vocab, 200, "memes r us", 0.8))
            message = ""
            while(message != "exit"):
                message = raw_input("Type your stuff:")
                print(message)
                print(sample(message, chars, sess, vocab, model))
                



def sample(prime, chars, sess, vocab, model):
    charsList, probs = model.rawsample(sess, chars, vocab, prime)
    


    return model.sample(sess, chars, vocab, 100, prime, 0.7)
    #print(model.sample(sess, chars, vocab, 10, prime, 0.7))

if __name__ == '__main__':
    main()
