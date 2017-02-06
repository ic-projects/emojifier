from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
import sys
from six.moves import cPickle

from utils import TextLoader
from model import Model
from six import text_type

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='data/tinyshakespeare',
                       help='data directory containing input.txt')
    parser.add_argument('--save_dir', type=str, default='save',
                       help='directory to store checkpointed models')
    parser.add_argument('--rnn_size', type=int, default=512,
                       help='size of RNN hidden state')
    parser.add_argument('--num_layers', type=int, default=3,
                       help='number of layers in the RNN')
    parser.add_argument('--model', type=str, default='lstm',
                       help='rnn, gru, or lstm')
    parser.add_argument('--batch_size', type=int, default=50,
                       help='minibatch size')
    parser.add_argument('--seq_length', type=int, default=25,
                       help='RNN sequence length')
    parser.add_argument('--num_epochs', type=int, default=50,
                       help='number of epochs')
    parser.add_argument('--save_every', type=int, default=1000,
                       help='save frequency')
    parser.add_argument('--grad_clip', type=float, default=5.,
                       help='clip gradients at this value')
    parser.add_argument('--learning_rate', type=float, default=0.0015,
                       help='learning rate')
    parser.add_argument('--decay_rate', type=float, default=0.97,
                       help='decay rate for rmsprop')
    parser.add_argument('--init_from', type=str, default=None,
                       help="""continue training from saved model at this path. Path must contain files saved by previous training process:
                            'config.pkl'        : configuration;
                            'chars_vocab.pkl'   : vocabulary definitions;
                            'checkpoint'        : paths to model file(s) (created by tf).
                                                  Note: this file contains absolute paths, be careful when moving files around;
                            'model.ckpt-*'      : file(s) with model definition (created by tf)
                        """)
    args = parser.parse_args()
    train(args)

def train(args):
    print(sys.path)
    data_loader = TextLoader(args.data_dir, args.batch_size, args.seq_length)
    args.vocab_size = data_loader.vocab_size

    # check compatibility if training is continued from previously saved model
    if args.init_from is not None:
        # check if all necessary files exist
        assert os.path.isdir(args.init_from)," %s must be a a path" % args.init_from
        assert os.path.isfile(os.path.join(args.init_from,"config.pkl")),"config.pkl file does not exist in path %s"%args.init_from
        assert os.path.isfile(os.path.join(args.init_from,"chars_vocab.pkl")),"chars_vocab.pkl.pkl file does not exist in path %s" % args.init_from
        ckpt = tf.train.get_checkpoint_state(args.init_from)
        assert ckpt,"No checkpoint found"
        assert ckpt.model_checkpoint_path,"No model path found in checkpoint"

        # open old config and check if models are compatible
        with open(os.path.join(args.init_from, 'config.pkl'), 'rb') as f:
            saved_model_args = cPickle.load(f)
        need_be_same=["model","rnn_size","num_layers","seq_length"]
        for checkme in need_be_same:
            assert vars(saved_model_args)[checkme]==vars(args)[checkme],"Command line argument and saved model disagree on '%s' "%checkme

        # open saved vocab/dict and check if vocabs/dicts are compatible
        with open(os.path.join(args.init_from, 'chars_vocab.pkl'), 'rb') as f:
            saved_chars, saved_vocab = cPickle.load(f)
        assert saved_chars==data_loader.chars, "Data and loaded model disagree on character set!"
        assert saved_vocab==data_loader.vocab, "Data and loaded model disagree on dictionary mappings!"

    with open(os.path.join(args.save_dir, 'config.pkl'), 'wb') as f:
        cPickle.dump(args, f)
    with open(os.path.join(args.save_dir, 'chars_vocab.pkl'), 'wb') as f:
        cPickle.dump((data_loader.chars, data_loader.vocab), f)

    model = Model(args)
    summaries_dir = '//homes/ljs116/tensorflow/char-rnn-tensorflow/summary'
    with tf.Session() as sess:
        merged = tf.summary.merge_all()
        train_writer = tf.train.SummaryWriter(summaries_dir + '/train',sess.graph)
        test_writer = tf.train.SummaryWriter(summaries_dir + '/test')

        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver(tf.global_variables())
        # restore model
        if args.init_from is not None:
            saver.restore(sess, ckpt.model_checkpoint_path)
        for e in range(args.num_epochs):
            sess.run(tf.assign(model.lr, args.learning_rate * (args.decay_rate ** e)))
            data_loader.reset_batch_pointer()
            state = sess.run(model.initial_state)
            #data_loader.reset_batch_pointer_offset(9000)
            for b in range(data_loader.num_batches):
                #b = bb + 9000
                start = time.time()
                x, y = data_loader.next_batch()
                feed = {model.input_data: x, model.targets: y}
                for i, (c, h) in enumerate(model.initial_state):
                    feed[c] = state[i].c
                    feed[h] = state[i].h
                summary, train_loss, state, _ = sess.run([merged, model.cost, model.final_state, model.train_op], feed)
                #train_writer.add_summary(summary, b + (data_loader.num_batches * e))
                end = time.time()
                print("{}/{} (epoch {}), train_loss = {:.3f}, time/batch = {:.3f}" \
                    .format(e * data_loader.num_batches + b,
                            args.num_epochs * data_loader.num_batches,
                            e, train_loss, end - start))
                if (b % 20 == 0):
                    train_writer.add_summary(summary, (b  + (data_loader.num_batches * e)) / 20)
                    #all_loss = 0
                    #sess.run(tf.assign(model.drop, 1))
                    val_state = sess.run(model.initial_state)
                    #for vb in range(data_loader.val_num_batches):
                    x, y = data_loader.val_next_batch()
                    feed = {model.input_data: x,model.targets: y}
                    state_feed = {pl: s for pl, s in zip(sum(model.initial_state, ()), sum(val_state, ()))}
                    feed.update(state_feed)
                    summary, batch_loss, val_state = sess.run([merged, model.cost, model.final_state], feed)
                    test_writer.add_summary(summary, (b  + (data_loader.num_batches * e)) / 20)
                    #all_loss += batch_loss
                    #val_loss = all_loss / data_loader.val_num_batches
                    print("val_loss = {:.3f}".format(batch_loss))
                    #sess.run(tf.assign(model.drop, 0.7))
                    #data_loader.val_reset_batch_pointer()
                if (e * data_loader.num_batches + b) % args.save_every == 0\
                    or (e==args.num_epochs-1 and b == data_loader.num_batches-1): # save for the last result
                    #sess.run(tf.assign(model.drop, 1))
                    checkpoint_path = os.path.join(args.save_dir, 'model.ckpt')
                    saver.save(sess, checkpoint_path, global_step = e * data_loader.num_batches + b)
                    #sess.run(tf.assign(model.drop, 0.7))
                    print("model saved to {}".format(checkpoint_path))
            train_writer.close()
            test_writer.close()
                    #print("Using sample=0")
                    #print(model.sample(sess, data_loader.chars, data_loader.vocab, 500, 'The ', 0))

if __name__ == '__main__':
    main()
