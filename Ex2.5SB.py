# This code replicates Fig. 2.2 in the book. I have used the same code thrice to give results for epsilon=0.1,0.01 and greedy method.

import matplotlib.pyplot as plt
import numpy as np
import random
from tqdm import tqdm

num_of_bandits = 10
epsilon = 0.1
loop_max_iterations = 1000
total_runs = 2000

rewards = [0]*num_of_bandits
rewards += np.random.normal(loc = 0.0, scale = 1, size = 10)
total_rewards_all_runs = [0]*loop_max_iterations

for run_counter in tqdm(range(total_runs)):
    value_func = [0]*num_of_bandits
    step_counter = [0]*num_of_bandits
    loop_counter = 0
    total_reward = 0
    rewards_this_run = [0]*loop_max_iterations
    while(loop_counter < loop_max_iterations):
        action_selected = -1
        reward = 0
        
        greedy_action_index = value_func.index(max(value_func))
        random_action_index = random.randrange(10)
        if random.random() > epsilon:
            reward = np.random.normal(loc = rewards[greedy_action_index], scale = 1)
            action_selected = greedy_action_index
        else:
            reward = np.random.normal(loc = rewards[random_action_index], scale = 1)
            action_selected = random_action_index
        step_counter[action_selected] += 1
        value_func[action_selected] += 1/step_counter[action_selected]*(reward - value_func[action_selected])

        rewards_this_run[loop_counter] = reward
        loop_counter += 1
    total_rewards_all_runs = [sum(z) for z in zip(total_rewards_all_runs, rewards_this_run)]

average_rewards_all_runs = [total_rewards_all_runs[i]/total_runs for i in range(loop_max_iterations)]

# np.set_printoptions(precision=2)
# print("total_rewards_all_runs")
# print(np.array(total_rewards_all_runs))
# print("average_rewards_all_runs")
# print(np.array(average_rewards_all_runs))
print(rewards)
print(value_func)
plt.plot([0]+average_rewards_all_runs,'b',label='epsilon = 0.1')


num_of_bandits = 10
epsilon = 0.01
loop_max_iterations = 1000
total_runs = 2000


total_rewards_all_runs = [0]*loop_max_iterations

for run_counter in tqdm(range(total_runs)):
    value_func = [0]*num_of_bandits
    step_counter = [0]*num_of_bandits
    loop_counter = 0
    total_reward = 0
    rewards_this_run = [0]*loop_max_iterations
    while(loop_counter < loop_max_iterations):
        action_selected = -1
        reward = 0
        # rewards += np.random.normal(loc = 0.0, scale = 0.01, size = 10)
        greedy_action_index = value_func.index(max(value_func))
        random_action_index = random.randrange(10)
        # print(random.random())
        if random.random() > epsilon:
            reward = np.random.normal(loc = rewards[greedy_action_index], scale = 1)
            action_selected = greedy_action_index
        else:
            reward = np.random.normal(loc = rewards[random_action_index], scale = 1)
            action_selected = random_action_index
        step_counter[action_selected] += 1
        value_func[action_selected] += 1/step_counter[action_selected]*(reward - value_func[action_selected])

        rewards_this_run[loop_counter] = reward
        loop_counter += 1
    total_rewards_all_runs = [sum(z) for z in zip(total_rewards_all_runs, rewards_this_run)]

average_rewards_all_runs = [total_rewards_all_runs[i]/total_runs for i in range(loop_max_iterations)]

print(rewards)
print(value_func)
plt.plot([0]+average_rewards_all_runs,'r',label='epsilon=0.01')





num_of_bandits = 10
epsilon = 0
loop_max_iterations = 1000
total_runs = 2000

total_rewards_all_runs = [0]*loop_max_iterations

for run_counter in tqdm(range(total_runs)):
    value_func = [0]*num_of_bandits
    step_counter = [0]*num_of_bandits
    loop_counter = 0
    total_reward = 0
    rewards_this_run = [0]*loop_max_iterations
    while(loop_counter < loop_max_iterations):
        action_selected = -1
        reward = 0
        # rewards += np.random.normal(loc = 0.0, scale = 0.01, size = 10)
        greedy_action_index = value_func.index(max(value_func))
        random_action_index = random.randrange(10)
        # print(random.random())
        if random.random() > epsilon:
            reward = np.random.normal(loc = rewards[greedy_action_index], scale = 1)
            action_selected = greedy_action_index
        else:
            reward = np.random.normal(loc = rewards[random_action_index], scale = 1)
            action_selected = random_action_index
        step_counter[action_selected] += 1
        value_func[action_selected] += 1/step_counter[action_selected]*(reward - value_func[action_selected])

        rewards_this_run[loop_counter] = reward
        loop_counter += 1
    total_rewards_all_runs = [sum(z) for z in zip(total_rewards_all_runs, rewards_this_run)]

average_rewards_all_runs = [total_rewards_all_runs[i]/total_runs for i in range(loop_max_iterations)]


print(rewards)
print(value_func)
plt.plot([0]+average_rewards_all_runs,'g', label = 'Greedy')
plt.legend()
plt.annotate(rewards, (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()
