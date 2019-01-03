#from tos_env import Tos
from RL_brain import DeepQNetwork
from tos_env import Tos
from env_UI_pyg import gameWindow

import gym
import numpy as np
#def maincycle(ui):
#    brain.learn()

if __name__ == '__main__':
    # Get the environment and extract the number of actions
    #env = gym.make('CartPole-v0')
    #np.random.seed(123)
    #env.seed(123)


    #window = gameWindow("name",maincycle)
    env = Tos()
    #env.reset()
    brain = DeepQNetwork(env)

    brain.learn()

    #window.initWindow()
