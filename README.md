# Monte Carlo Policy Evaluation for Gridworld

This repository contains a Python implementation of Monte Carlo Policy Evaluation applied to a simple gridworld environment.

## Gridworld

The `Gridworld` class represents a 5x5 grid environment with special states ('A' and 'B'), each having specific rewards and transition dynamics. The agent can take actions ('north', 'south', 'east', 'west') to navigate through the grid.

## Monte Carlo Policy Evaluation

The `MonteCarloPolicyEvaluation` class is designed to evaluate the state values using the Monte Carlo method. It randomly generates episodes using a random policy and updates the state values based on the observed returns.

## Usage

To run the Monte Carlo Policy Evaluation on the gridworld, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/MohsenKashefi/artificial-intelligence-project.git
Navigate to the project directory:


