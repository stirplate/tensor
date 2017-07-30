import input_data
mnist = input_data.read_data_sets ("/temp/data", one_hot = True)

import tensorflow as tf 

#set parameters
learning_rate =0.01
traning_iteration = 30
batch_size = 100
display_step =2 
