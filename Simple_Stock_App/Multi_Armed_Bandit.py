# Create a bandit with 4 arms using python and np
import numpy as np
import tensorflow as tf
# Multi armed badnit: comes form 1 arm bandit to describe a slot machine
# YOu pull and either win or lose (+ 1 or -1) 
#Imagine if you have multiple slot mahcines, each with a probabiltiy
# You can either use 1 to see what it pays out
# OR you can explore several machines
# THis is called the exploration exploitation trade off

class MultiARmedBandit:
    def __init__(self):
        self.bandit = [.2,.0,.1,-4.0] # WE will generate a random number every time with each probability 
        # 4th arm (Or forth value of teh array) has the highest ammount to pay off
        self.num_actions = 4
    def pull(self,arm):
        return i if np.random.randn(1) > self.bandit[arm] else -1

class Agent:
    def __init__(self,actions=4):
        self.num_actions = actions
        self.reward_in = tf.placeholder(tf.float32,[1],name='reward_in')
        self.action_in = tf.placeholder(tf.int32,[1]. name='action_in')
        
        self.W = tf.get_variable('W', [self.num_actions])