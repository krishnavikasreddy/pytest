"""
My First Lstm network
"""
from __future__ import print_function, division
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

num_epochs = 100
total_series_length = 50000
truncated_backprop_length = 15
state_size = 4
num_classes = 2
echo_step = 3
batch_size = 5
num_batches = total_series_length//batch_size//truncated_backprop_length


def generate_data():
    """
    This generates the random data required
    """
    x_values = np.random.choice(2, total_series_length, p=[0.5, 0.5])
    y_values = np.roll(x_values, echo_step)
    y_values[0:echo_step] = 0
    x_values = x_values.reshape((batch_size, -1))
    y_values = y_values.reshape((batch_size, -1))
    return (x_values, y_values)

def tf_procession():
    batch_x_placeholder = tf.placeholder(tf.float32, [batch_size, truncated_backprop_length])
    batch_y_placeholder = tf.placeholder(tf.int32, [batch_size, truncated_backprop_length])
    init_state = tf.placeholder(tf.int32, [batch_size, truncated_backprop_length])
    W = tf.Variable(np.random.rand(state_size+1, state_size), dtype = tf.float32)
    b = tf.Variable(np.zeros((1, num_classes)), dtype=tf.float32)
    w2 = tf.Variable(np.random.rand(state_size, num_classes), dtype=tf.float32)
    b2 = tf.Variable(np.zeros((1, num_classes)), dtype=tf.float32)

if __name__ == "__main__":
    print("Hello world")
    generate_data()
