
![](./images/pytorch.png)

# PyTorch Tutorial (in-progress)

## PREFACE

Welcome to the self-paced PyTorch tutorial. This collection of notebooks and exercises is designed for learners who want a practical, hands-on introduction to deep learning with PyTorch. Whether you're a student, researcher, or developer, these materials will guide you from core concepts to building and training neural networks using modern best practices.

What you will get from this tutorial:
- Clear, notebook-driven lessons that explain concepts with runnable code.
- Paired exercise notebooks so you can practice and consolidate learning.
- Notes on common pitfalls, tips for debugging models, and suggestions for next steps.

We encourage you to work through the notebooks in order and to try the exercises after each lesson.

## INTRODUCTION

### Why Use a Deep Learning Framework?

Deep learning systems involve complex model definitions, automatic differentiation, performance-sensitive tensor operations, and optionally, harware acceleration on GPUs and TPUs. A framework also handles model serialization and deployment ecosystems. Using a framework speeds up experimentation, reduces boilerplate, and helps you move from research to production faster.

### Popular Deep Learning Frameworks

Several frameworks are widely used in both research and industry:
- TensorFlow — mature ecosystem, strong production and tooling support.
- PyTorch — research-friendly imperative API, fast adoption for experimentation.
- JAX — composable function transformations and high performance for research.

Each framework has strengths; choice often depends on priorities like ease of prototyping, production tooling, or ecosystem integrations.

### Introduction to PyTorch

PyTorch is an open-source deep learning library that emphasizes a Pythonic, imperative programming model. Key features include:
- Tensors and fast GPU computation.
- Automatic differentiation (Autograd) required for building and training models.
- A modular neural network library (`torch.nn`) and optimization utilities (`torch.optim`).
- Strong community, extensive model zoo, and integrations with tooling (TorchScript, TorchVision, etc).

Why PyTorch Matters:
- Research-first Design: easy debugging and fast iteration using eager execution.
- Growing Adoption: many state-of-the-art research implementations are released in PyTorch.
- Industry Adoption: increasing use in production systems with maturation of deployment tools.

### Trends and adoption

In recent years PyTorch has seen rapid growth in both academia and industry. Many research papers publish reference implementations in PyTorch, and major platforms now provide pre-trained models and tooling for PyTorch workflows. While TensorFlow remains strong (particularly in production and mobile tooling), PyTorch's developer ergonomics and ecosystem have made it a leading choice for model development and research.

## Structure of The Tutorial

This tutorial is organized as a sequence of Jupyter notebooks. Each lesson notebook focuses on one topic and is paired with a companion exercises notebook so you can practice the concepts.

**How to Use the Materials:**

1. Follow the notebooks in the provided order. Each notebook builds on concepts from the previous ones.
2. After completing a lesson notebook, open the corresponding exercises notebook and try the problems. Solutions (where provided) are separated so you can attempt them first.
3. Use the provided datasets and code cells to run experiments locally. Notebooks are runnable end-to-end and assume a working PyTorch installation.

**Notebook Types and Naming Convention:**
- Lesson notebooks: `NN_<number>_<short-title>.ipynb` (the main teaching material).
- Exercise notebooks: `EX_<number>_<short-title>_exercises.ipynb` (practice problems matching the lesson).

**Example Sequence (illustrative):**
1. `NN_01_intro_and_tensor_basics.ipynb` + `EX_01_tensor_basics_exercises.ipynb`
2. `NN_02_autograd_and_optim.ipynb` + `EX_02_autograd_exercises.ipynb`
3. `NN_03_building_models.ipynb` + `EX_03_models_exercises.ipynb`

**Each Notebook Includes:**
- Learning objectives at the top.
- Background and motivation.
- Walk-through code cells with explanations.
- Practical exercises and suggested extensions.

## Next steps

- If you haven't already, install PyTorch following the official guide for your OS and CUDA configuration: https://pytorch.org/get-started/locally/
- Start with the first lesson notebook and try the paired exercises.

_Enjoy learning PyTorch!_
