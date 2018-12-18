from tos_env import Tos
from RL_brain import DeepQNetwork

def run_tos():
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset()

        while True:
            # fresh the environment
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1
    # end of game
    print ('Game over.')
    env.destroy()

if __name__ == '__main__':
    # tos game
    env = Tos()
    RL = DeepQNetwork()
    env.after(100, run_tos)
    env.mainloop()
    RL.plot_cost()
