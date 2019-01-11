#from tos_env import Tos
from RL_brain import DeepQNetwork
from tos_env import Tos

import gym
import numpy as np
import argparse
import Maps

# command arguments
parser = argparse.ArgumentParser()
parser.add_argument('-map', type=int, help='Select the initial map you want. :)')
args = parser.parse_args()

if __name__ == '__main__':

    # build the virtual environment
    map_index = args.map
    env = Tos(Maps.maps[map_index])

    # build the neural network
    brain = DeepQNetwork(env)
    #brain.learn()
    brain.run_test('Weights//second_version_weights.h5f')
