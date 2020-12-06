''' An example of playing Nolimit Texas Hold'em with random agents
'''

import rlcard
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed

# Make environment
env = rlcard.make('no-limit-holdem', config={'seed': 0})
episode_num = 2

# Set a global seed
set_global_seed(0)

# Set up agents
agents = []
for i in range(env.player_num):
    agent = RandomAgent(action_num=env.action_num)
    agents.append(agent)

env.set_agents(agents)

for episode in range(episode_num):

    # Generate data from the environment
    trajectories, _ = env.run(is_training=False)

    # Print out the trajectories
    print('\nEpisode {}'.format(episode))
    for i in range(env.player_num):
        for ts in trajectories[i]:
            print('State: {}, Action: {}, Reward: {}, Next State: {}, Done: {}'.format(
                ts[0], ts[1], ts[2], ts[3], ts[4]))
