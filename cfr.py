''' An example of learning a CFR Agent on No-Limit Texas Holdem
'''

import os

import rlcard
from rlcard.agents import CFRAgent
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed, tournament
from rlcard.utils import Logger

# Make environment
env = rlcard.make('leduc-holdem',
                  config={'seed': 0, 'allow_step_back': True})
eval_env = rlcard.make('leduc-holdem', config={'seed': 0})

# Set the iterations numbers and how frequently we evaluate the performance
evaluate_every = 100
evaluate_num = 1000
episode_num = 100000

# The intial memory size
memory_init_size = 1000

# Train the agent every X steps
train_every = 1

# The paths for saving the logs and learning curves
log_dir = './experiments/cfr_result/'

# Set a global seed
set_global_seed(0)

# Set up the agents
agents = []
for i in range(env.player_num):
    agent = CFRAgent(env=env)
    agents.append(agent)
random_agent = RandomAgent(action_num=eval_env.action_num)

env.set_agents(agents)
eval_env.set_agents([agents[0], random_agent])

# Init a Logger to plot the learning curve
logger = Logger(log_dir)

for episode in range(episode_num):
    for agent in agents:
        agent.train()
        
    print('\rIteration {}'.format(episode), end='')
    # Evaluate the performance. Play with random agents.
    if episode % evaluate_every == 0:
        agent.save()  # Save model
        logger.log_performance(
            env.timestep, tournament(eval_env, evaluate_num)[0])

# Close files in the logger
logger.close_files()

# Plot the learning curve
logger.plot('CFR')
