#!/bin/bash
python //homes/ljs116/tensorflow/word-rnn-tensorflow/train.py --data_dir=//homes/ljs116/tensorflow/word-rnn-tensorflow/data/best/ --save_dir=//homes/ljs116/tensorflow/word-rnn-tensorflow/save/ --init_from=//homes/ljs116/tensorflow/word-rnn-tensorflow/save/ --rnn_size=256 --num_layers=2
