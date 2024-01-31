class Gridworld:
    def __init__(self):
        self.grid = [[0 for _ in range(5)] for _ in range(5)]
        self.special_states = {'A': ((0, 1), 10, (4, 1)), 'B': ((0, 3), 5, (2, 3))}
        self.actions = ['north', 'south', 'east', 'west']

    def step(self, state, action):
        if state in [v[0] for v in self.special_states.values()]:
            for key, val in self.special_states.items():
                if state == val[0]:
                    return val[1], val[2]  # Return reward and new state
        else:
            new_state = self.move(state, action)
            reward = -1 if new_state == state else 0
            return reward, new_state

    def move(self, state, action):
        i, j = state
        if action == 'north' and i > 0:
            return (i-1, j)
        elif action == 'south' and i < 4:
            return (i+1, j)
        elif action == 'east' and j < 4:
            return (i, j+1)
        elif action == 'west' and j > 0:
            return (i, j-1)
        return state  # If the action would take the agent off the grid



