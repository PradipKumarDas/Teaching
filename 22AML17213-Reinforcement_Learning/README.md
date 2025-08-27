# Reinforcement Learning with OpenAI Gymnasium

This repository contains implementations of reinforcement learning algorithms for various Gymnasium environments. Each environment demonstrates different aspects of RL algorithms.

## Environments

### 1. Blackjack-v1
- Simple card game environment
- Implementations: Q-Learning agent (`blackjack-v1.ipynb`)

### 2. CartPole-v1
- Classic control problem
- Implementations:
  - Q-Learning with state discretization (`cartpole-v1.ipynb`)
  - Q-Network using TensorFlow/Keras

### 3. Taxi-v3
- Grid-world navigation problem
- Implementations: Q-Learning agent (`taxi-v3.ipynb`)

## Environment Setup

1. Create a new conda environment:
```bash
conda create -n reinforcement_learning python=3.13.5
conda activate reinforcement_learning
```

2. Install required packages:
```bash

# Installs Farama Gymnasium that provides APIs for reinforcement learning with a diverse collection of reference environments. Also installs Pygame which is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.
pip install gymnasium[classic-control] 

pip install moviepy         # Dependency for video recording
conda install matplotlib
conda install seaborn

# For neural network based agent implementation
pip install tensorflow      # For CPU users. Install Tensorflow 2.20.0 or later

# or
pip install tensorflow[and-cuda]		# For GPU users

# OPTIONAL
conda install conda-forge::jupyterlab   # Install JupyterLab editor. Users using other editors may skip this installation.
```

## Usage

1. Activate the environment:
```bash
conda activate reinforcement_learning       # Activates conda environment
```

2. Launch editor:
```bash
jupyter lab     # User using other editor may skip this step
```

3. Navigate to specific environment folders and run the notebooks

## Requirements
- Python
- Gymnasium
- NumPy
- TensorFlow (for DQN)
- Matplotlib
- Jupyter Notebook
