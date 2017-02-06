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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='save',
                       help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=500,
                       help='number of characters to sample')
    parser.add_argument('--prime', type=text_type, default=u' ',
                       help='prime text')
    parser.add_argument('--sample', type=int, default=1,
                       help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')

    args = parser.parse_args()
    sample(args)

def benchmark():
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='//homes/ljs116/tensorflow/char-rnn-tensorflow/save/',
                       help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=500,
                       help='number of characters to sample')
    parser.add_argument('--prime', type=text_type, default=u' ',
                       help='prime text')
    parser.add_argument('--sample', type=int, default=1,
                       help='0 to use max at each timestep, 1 to sample at each timestep, 2 to sample on spaces')

    args = parser.parse_args()
    sample(args)

def sample(args):
    with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir, 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, True, useDropout=False)
    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        saver = tf.train.Saver(tf.all_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            if args.sample == 5:
                ## 0=max -1=weighed 5=benchmark allelse=temperature
                print("================ sample: 0 ====================")
                print(model.sample(sess, chars, vocab, args.n, args.prime, 0))
                print("================ sample: -1 ====================")
                print(model.sample(sess, chars, vocab, args.n, args.prime, -1))
                for i in range(1,10):
                    s = i / 10.0
                    print("================ sample temperature: {:.3f} ====================".format(s))
                    print(model.sample(sess, chars, vocab, args.n, args.prime, s))

            else:
                print(model.sample(sess, chars, vocab, args.n, args.prime, args.sample))

if __name__ == '__main__':
    main()
