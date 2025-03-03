# DEEP LEARNING [22AML161]

**_TEACHING MATERIAL AND REFERENCE IMPLEMENTATION FOR LABORATORY EXPERIMENTS._**

**Acknowledgement:** Author's original repository is available at https://github.com/ageron/handson-ml3. Relevant implementations were modified to suit the classroom learning.

## Experiments

**Deep Neural Networks Training:**

1. Self-regularized Network using SELU Activation Function `Tutorial`

2. Model Performance Improvement with Batch Normalization Layers

3. Transfer Learning for Improved Model with Less Data

**Convolutional Neural Networks:**

1. Building a Convolutional Neural Network (CNN) from Scratch

2. Building an Image Classifier using a Pretrained Xception Model on TensorFlow Flower Dataset

**Sequence Processing:**

1. Sequence Processing using Recurrent Neural Networks (RNNs)

**Text Processing**

1. Sentiment Analysis using Recurrent Neural Networks & Embeddings

_Coming up the remaining ones..._


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
