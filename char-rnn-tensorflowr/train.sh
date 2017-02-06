#!/bin/bash
python //homes/ljs116/tensorflow/char-rnn-tensorflow/train.py --data_dir=//homes/ljs116/tensorflow/char-rnn-tensorflow/data/best/ --save_dir=//homes/ljs116/tensorflow/char-rnn-tensorflow/save/ --init_from=//homes/ljs116/tensorflow/char-rnn-tensorflow/save/ --rnn_size=512 --num_layers=3
