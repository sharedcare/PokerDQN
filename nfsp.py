''' An example of learning a NFSP Agent on No-Limit Texas Holdem
'''

import torch
import os

import rlcard
from rlcard.agents import NFSPAgentPytorch as NFSPAgent
from rlcard.agents import RandomAgent
from rlcard.utils import set_global_seed, tournament
from rlcard.utils import Logger

# Make environment
env = rlcard.make('leduc-holdem', config={'seed': 0})
eval_env = rlcard.make('leduc-holdem', config={'seed': 0})

# Set the iterations numbers and how frequently we evaluate the performance
evaluate_every = 10000
evaluate_num = 10000
episode_num = 100000

# The intial memory size
memory_init_size = 1000

# Train the agent every X steps
train_every = 64

# The paths for saving the logs and learning curves
log_dir = './experiments/nfsp_result/'

# Set a global seed
set_global_seed(0)

# Set up the agents
agents = []
# print(env.player_num)
for i in range(env.player_num):
    agent = NFSPAgent(scope='nfsp' + str(i),
                        action_num=env.action_num,
                        state_shape=env.state_shape,
                        hidden_layers_sizes=[512, 512],
                        anticipatory_param=0.1,
                        min_buffer_size_to_learn=memory_init_size,
                        q_replay_memory_init_size=memory_init_size,
                        train_every=train_every,
                        q_train_every=train_every,
                        q_mlp_layers=[512, 512])
    agents.append(agent)
random_agent = RandomAgent(action_num=eval_env.action_num)

env.set_agents(agents)
eval_env.set_agents([agents[0], random_agent])

# Init a Logger to plot the learning curve
logger = Logger(log_dir)

for episode in range(episode_num):

    # First sample a policy for the episode
    for agent in agents:
        agent.sample_episode_policy()

    # Generate data from the environment
    trajectories, _ = env.run(is_training=True)

    # Feed transitions into agent memory, and train the agent
    for i in range(env.player_num):
        for ts in trajectories[i]:
            agents[i].feed(ts)

    # Evaluate the performance. Play with random agents.
    if episode % evaluate_every == 0:
        logger.log_performance(
            env.timestep, tournament(eval_env, evaluate_num)[0])

# Close files in the logger
logger.close_files()

# Plot the learning curve
logger.plot('NFSP')

# Save model
save_dir = 'models/nfsp'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
state_dict = {}
for agent in agents:
    state_dict.update(agent.get_state_dict())
torch.save(state_dict, os.path.join(save_dir, 'model.pth'))
