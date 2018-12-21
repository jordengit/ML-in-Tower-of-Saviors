#from tos_env import Tos
from RL_brain import DeepQNetwork

import gym
import numpy as np

if __name__ == '__main__':
    # Get the environment and extract the number of actions
    env = gym.make('CartPole-v0')
    np.random.seed(123)
    env.seed(123)

    brain = DeepQNetwork(env)
    brain.learn()
