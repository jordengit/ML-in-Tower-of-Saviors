import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

class DeepQNetwork:
    def __init__(self, env):
        self.env = env
        self.nb_actions = self.env.action_space.n
        self.model = self.build_net()

    def build_net(self):
        model = Sequential()
        model.add(Flatten(input_shape=(1,) + self.env.observation_space.shape))
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(self.nb_actions))
        model.add(Activation('linear'))

        return model

    def learn(self):
        memory = SequentialMemory(limit=50000, window_length=1)
        policy = BoltzmannQPolicy()
        dqn = DQNAgent(model=self.model, nb_actions=self.nb_actions, memory=memory, nb_steps_warmup=10, target_model_update=1e-2, policy=policy)
        dqn.compile(Adam(lr=1e-3), metrics=['mae'])

        dqn.fit(self.env, nb_steps=50000, visualize=True, verbose=2)
        dqn.save_weights('dqn_weights.h5f', overwrite=True)

        # Finally, evaluate our algorithm for 5 episodes.
        dqn.test(self.env, nb_episodes=5, visualize=True)
