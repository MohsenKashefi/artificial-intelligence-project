import random
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from gridworld import *


class MonteCarloPolicyEvaluation:
    def __init__(self, gridworld, num_episodes, gamma=0.9):
        self.gridworld = gridworld
        self.num_episodes = num_episodes
        self.gamma = gamma
        self.V = np.zeros((5, 5))
        self.returns = {}  # Store returns for each state

    def generate_episode(self):
        episode = []
        state = (2, 0)  # Starting state
        while True:
            action = np.random.choice(self.gridworld.actions)  # Random policy
            reward, next_state = self.gridworld.step(state, action)
            episode.append((state, action, reward))
            if state in [v[0] for v in self.gridworld.special_states.values()]:
                break
            state = next_state
        return episode

    def evaluate_policy(self):
        for _ in range(self.num_episodes):
            episode = self.generate_episode()
            G = 0  # Initialize return
            for t in reversed(range(len(episode))):
                state, action, reward = episode[t]
                G = self.gamma * G + reward
                if state not in [s[0] for s in episode[:t]]:
                    if state not in self.returns:
                        self.returns[state] = []
                    self.returns[state].append(G)
                    self.V[state[0], state[1]] = np.mean(self.returns[state])

    def get_value_function(self):
        return self.V
