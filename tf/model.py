import tensorflow as tf
from tensorflow.python.ops import rnn_cell
from tensorflow.python.ops import seq2seq

import numpy as np

class Model():
    def __init__(self, args, infer=False, useDropout=False):
        self.args = args
        if infer:
            args.batch_size = 1
            args.seq_length = 1

        
        cell_fn = rnn_cell.BasicLSTMCell
        self.drop = tf.Variable(1, trainable=False)
        cell = cell_fn(args.rnn_size, state_is_tuple=True)
        if useDropout:
            wrapped_cell = tf.nn.rnn_cell.DropoutWrapper(cell, input_keep_prob=self.drop)
        else:
            wrapped_cell = cell
        self.cell = cell = rnn_cell.MultiRNNCell([wrapped_cell] * args.num_layers, state_is_tuple=True)
        self.input_data = tf.placeholder(tf.int32, [args.batch_size, args.seq_length])
        self.targets = tf.placeholder(tf.int32, [args.batch_size, args.seq_length])
        self.initial_state = cell.zero_state(args.batch_size, tf.float32)
        #self.zero_state = self.cell.zero_state(args.batch_size, tf.float32)
        with tf.variable_scope('rnnlm'):
            softmax_w = tf.get_variable("softmax_w", [args.rnn_size, args.vocab_size])
            softmax_b = tf.get_variable("softmax_b", [args.vocab_size])
            with tf.device("/cpu:0"):
                embedding = tf.get_variable("embedding", [args.vocab_size, args.rnn_size])
                inputs = tf.split(1, args.seq_length, tf.nn.embedding_lookup(embedding, self.input_data))
                inputs = [tf.squeeze(input_, [1]) for input_ in inputs]

        def loop(prev, _):
            prev = tf.matmul(prev, softmax_w) + softmax_b
            prev_symbol = tf.stop_gradient(tf.argmax(prev, 1))
            return tf.nn.embedding_lookup(embedding, prev_symbol)

        outputs, last_state = seq2seq.rnn_decoder(inputs, self.initial_state, cell, loop_function=loop if infer else None, scope='rnnlm')
        output = tf.reshape(tf.concat(1, outputs), [-1, args.rnn_size])
        self.logits = tf.matmul(output, softmax_w) + softmax_b
        self.probs = tf.nn.softmax(self.logits)
        loss = seq2seq.sequence_loss_by_example([self.logits],
                [tf.reshape(self.targets, [-1])],
                [tf.ones([args.batch_size * args.seq_length])],
                args.vocab_size)

        self.cost = tf.reduce_sum(loss) / args.batch_size / args.seq_length
        with tf.name_scope('perplexity'):
            self.perplexity = tf.exp(self.cost)
            tf.summary.scalar('perplexity', self.perplexity)
        self.final_state = last_state
        self.lr = tf.Variable(0.0, trainable=False)
        tvars = tf.trainable_variables()
        grads, _ = tf.clip_by_global_norm(tf.gradients(self.cost, tvars),
                args.grad_clip)
        optimizer = tf.train.AdamOptimizer(self.lr)
        self.train_op = optimizer.apply_gradients(zip(grads, tvars))



    def sample(self, sess, chars, vocab, num=200, prime='The ', sampling_type=-1):
        state = sess.run(self.cell.zero_state(1, tf.float32))
        for char in prime[:-1]:
            x = np.zeros((1, 1))
            x[0, 0] = vocab[char]
            feed = {self.input_data: x, self.initial_state:state}
            [state] = sess.run([self.final_state], feed)

        def weighted_pick(weights):
            t = np.cumsum(weights)
            s = np.sum(weights)
            return(int(np.searchsorted(t, np.random.rand(1)*s)))

        ret = prime
        char = prime[-1]
        for n in range(num):
            x = np.zeros((1, 1))
            x[0, 0] = vocab[char]
            feed = {self.input_data: x, self.initial_state:state}
            [probs, state] = sess.run([self.probs, self.final_state], feed)
            po = probs[0]

            if sampling_type == 0:
                sample = np.argmax(po)
            elif sampling_type == -1:
                sample = weighted_pick(po)
            else: # sampling_type == 1 default:
                scale = np.log(po) / sampling_type
                exp = np.exp(scale)
                soft = exp / np.sum(exp)
                sample = np.random.choice(len(soft), p=soft)
                #sample = weighted_pick(soft)

            pred = chars[sample]
            ret += pred
            char = pred
        return ret




    def rawsample(self, sess, chars, vocab, prime='The ',):
        state = sess.run(self.cell.zero_state(1, tf.float32))
        for char in prime[:-1]:
            x = np.zeros((1, 1))
            x[0, 0] = vocab[char]
            feed = {self.input_data: x, self.initial_state:state}
            [state] = sess.run([self.final_state], feed)

        ret = prime
        char = prime[-1]
        x = np.zeros((1, 1))
        x[0, 0] = vocab[char]
        feed = {self.input_data: x, self.initial_state:state}
        [probs, state] = sess.run([self.probs, self.final_state], feed)
        po = probs[0]
        return chars, po

