import os
import tensorflow.compat.v1 as tf
from tensorflow.core.protobuf import saver_pb2
import driving_data
import model

tf.disable_v2_behavior()

class DataLogger:
    def __init__(self, logs_path):
        self.logs_path = logs_path
        self.summary_writer = tf.summary.FileWriter
        ...
