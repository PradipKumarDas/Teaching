# MACHINE LEARNING [23AML145]

Contains teaching material and reference implementation for practical experiments.

Author's original repository ia available at https://github.com/ageron/handson-ml3. Relevant implementations were modified to suit the classroom learning. 

All experiments were tested on
- Python 3.12.8
- Scikit-Learn 1.5.1
- Numpy 1.26.4
- Pandas 2.2.2
- Tensorflow 2.17.0
- Keras 3.6.0

## EXPERIMENTS

**Introduction to Machine Learning**
1. Predicting Life Satisfaction Index
2. Simple End-to-End Machine Learning Project `Tutorial`
3. Data Preprocessing

**Linear Models**

Linear Models for Classification:
1. Breast Cancer Detection using Linear Model `Tutorial`
2. Handwritten Digit Prediction using Linear Model

Linear Models for Regression:
1. California House Price Prediction using Different Regression Techniques

**Non-Linear Models**

Support Vector Machines:
1. Wine Class Prediction using Linear and Kernelized Support Vector Machine

Decision Trees:
1. Iris Flower Species Prediction using Decision Tree

**Ensembling**

1. Handwritten Digit Prediction using Voting Classification
2. Stacked Ensembling Implementation for Classification


## Setting-up Development Environment on Windows

Refer to the below steps to setup the development environment on Windows.

1. Install Anaconda Data Science platform by downloading Windows installer from the official website and restart Windows for changes to take place.

2. Open **Anaconda Prompt** by clicking _**Start --> Anaconda (64-bit) --> Anaconda Prompt**_. Note that for non-administrator user, this console needs to be opened as administrator.

3. Execute `conda update conda` to get the conda package manager updated.

4. Execute `conda create -n MLLab01 python=3.12.8` to create environment called **MLLab01**.

5. After the successful creation of the environment, activate that by executing `conda activate MLLab01`.

5. From that environment,

    i) execute `conda install jupyterlab matplotlib pandas scikit-learn conda-forge::transformers` to install the mentioned packages mandaged by conda.

    ii) execute `pip install tensorflow-hub tensorflow tensorboard tensorflow-datasets` to install the mentioned packages managed by pip.

6. Now, withing the same environment, execute `jupyter notebook` or `jupyter lab` to open Jupyter Notebook or Jupyter Lab editor. The later one is recommended out of the two.

**NOTE:** Everytime Anaconda Prompt is opened, it activates **base** environment by default. The target environment **MLLab01** has to be activated by entering command `conda activate MLLab01`.


## Alternatives for Editor

### Visual Studio Code

Though Jupyter Notebook or Jupyter Lab should be sufficient for all the above-mentioned experiments, Visual Studio Code is also one of the most popular code editors. This can be installed by downloading Windows installer from official website and running the setup. Default setup should be fine for most cases.

**Required Extensios**

After successful installation of Visual Studio Code (VS Code), it should be launched, and two below mentioned extensions should be installed from its _Extensions_ window.

1. Python 

    _[Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.]_

2. Jupyter

    _[Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more.]_

**Connecting to Kernel**

For VS Code to connect the kernel installed in the environment that was setup in the previous steps, 

1. click on **Select Kernel** located on the top right of the editor,

2. select **Another kernel...**,

3. select **Python Environments...**,

4. select **MLLab01 (Python 3.12.8)**.

The VS Code editor should be ready for coding.
