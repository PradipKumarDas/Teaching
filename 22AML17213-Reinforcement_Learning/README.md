# Reinforcement Learning with Farama Gymnasium

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

### 4. Luner Lander v3 [IN PROGRESS]
- Box2D (two-dimentional physics engine) based classic rocket trajectory optimization problem
- Immplementation: Q-Network using TensorFlow/Keras

## Setting up Development Environment

**1. Create a new conda environment.**
```bash
conda create -n reinforcement_learning python=3.13.7

conda activate reinforcement_learning
```

**2. Install build essentials.**

For Linux (Debian/Ubuntu-based):
```bash
sudo apt update

sudo apt install build-essential
```

For macOS:
```bash
xcode-select --install
```

For Windows:

Install a C++ compiler suite like MinGW-w64 or Microsoft Visual C++ Build Tools. These typically include g++ or a compatible C++ compiler. You will also need to ensure the compiler's path is added to your system's environment variables.

**3. Install required packages.**
```bash

# Installs Farama Gymnasium that provides APIs for reinforcement learning with a diverse collection of reference environments. Also installs Pygame which is a cross-platform set of Python modules designed for writing video games. It includes computer graphics and sound libraries designed to be used with the Python programming language.

pip install "gymnasium[all]"  # May take several minutes to complete

conda install ipykernel       # Provides the IPython kernel for Jupyter

conda install seaborn         # Additional data visualization library based on matplotlib

# For CPU users (installs Tensorflow 2.20.0 or later for neural network based agent implementation)
pip install tensorflow

# For GPU users
pip install tensorflow[and-cuda]

# OPTIONAL
conda install conda-forge::jupyterlab   # Installs JupyterLab editor. Users using other editors may skip this installation.
```

## Usage

**1. Activate the environment.**
```bash
conda activate reinforcement_learning       # Activates conda environment
```

**2. Launch editor.**
```bash
jupyter lab     # Or open any other editor of your choice, but make sure to select kernel created in the above steps.
```

**3. Navigate to specific environment folders and run the notebooks**

## Requirements
- Python
- Gymnasium
- IPyKernel
- NumPy
- TensorFlow
- Matplotlib
- Seaborn
- Jupyter Notebook
