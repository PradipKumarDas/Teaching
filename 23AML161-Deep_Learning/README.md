# DEEP LEARNING [23AML161]

**_TEACHING MATERIAL AND REFERENCE IMPLEMENTATION FOR LABORATORY EXPERIMENTS._**

**Acknowledgement:** Author's original repository is available at https://github.com/ageron/handson-ml3. Relevant implementations were modified to suit the classroom learning.

**Refresher on Artificial Neural Networks**

Notebooks located in the folder [refresher-on-artificial-neural-networks](https://github.com/PradipKumarDas/Teaching/tree/master/23AML161-Deep_Learning/refresher-on-artificial-neural-networks) are highly recommended to be practiced before getting into following experiments.

## Experiments

**Deep Neural Networks Training**

1. [Model Performance Improvement with Batch Normalization & Self-regularization](https://github.com/PradipKumarDas/Teaching/blob/master/21AML171-Deep_Learning/1_dnn_training-practical_1.ipynb)

2. [Transfer Learning to Build a Descent Model with Less Data](https://github.com/PradipKumarDas/Teaching/blob/master/23AML161-Deep_Learning/transfer_learning.ipynb)

**Convolutional Neural Networks**

3. [A Simple Convolutional Neural Network (CNN) from Scratch](https://github.com/PradipKumarDas/Teaching/blob/master/21AML171-Deep_Learning/2_cnn-practical_1.ipynb)

4. [Simple Single Object Detection - A Naive Approach](https://github.com/PradipKumarDas/Teaching/blob/master/23AML161-Deep_Learning/simple-single-object-detection-naive-approach.ipynb)


**Sequence Processing**

5. [Univariate Forecasting using Simple & Deep Recurrent Neural Networks](https://github.com/PradipKumarDas/Teaching/blob/master/21AML171-Deep_Learning/3_sequence_processing-practical_1.ipynb)

6. [Multivariate Forecasting using Simple & Deep Recurrent Neural Networks](https://github.com/PradipKumarDas/Teaching/blob/master/21AML171-Deep_Learning/3_sequence_processing-practical_2.ipynb)

**Text Processing**

7. [Sentiment Analysis using Recurrent Neural Networks & Embeddings](https://github.com/PradipKumarDas/Teaching/blob/master/21AML171-Deep_Learning/4_sentiment_analysis-practical_1.ipynb)

8. [Text Generation using Pretrained Transformer-based Language Model](https://github.com/PradipKumarDas/Teaching/blob/master/22AML161-Deep_Learning/text_generation_using_pretrained_transformer-based_language_model.ipynb)

**Representation Learning** 

9. [Reconstructing Noisy Images using Denoising Autoencoder](https://github.com/PradipKumarDas/Teaching/blob/master/22AML161-Deep_Learning/reconstructing_noisy_images_using_denoising_autoencoder.ipynb)

10. [Generating Images using Variational Autoencoder](https://github.com/PradipKumarDas/Teaching/blob/master/22AML161-Deep_Learning/generating_images_using_variational_autoencoder.ipynb)


## Setting-up Development Environment

This section describes how to setup development environment both in a local host and a in a container. The user can refer to any one of these approaches based on personal preference.

### Setting-up Development Environment on Windows

Refer to the below steps to setup the development environment on Windows.

1. Install Anaconda Data Science platform by downloading Windows installer from the official website and restart Windows for changes to take place.

2. Open **Anaconda Prompt** by clicking _**Start --> Anaconda (64-bit) --> Anaconda Prompt**_. Note that for non-administrator user, this console needs to be opened as administrator.

3. Execute `conda update conda` to get the conda package manager updated.

4. Execute `conda create -n deep-learning python=3.13.2` to create environment called **deep-learning**.

5. After the successful creation of the environment, activate that by executing `conda activate deep-learning`.

5. From that environment,

    i) execute `conda install jupyterlab matplotlib pandas scikit-learn conda-forge::transformers pydot statsmodels seaborn` to install the mentioned packages mandaged by conda

    ii) execute `pip install tensorflow-hub tensorflow tensorboard tensorflow-datasets keras-tuner keras-hub tf-keras` to install the mentioned packages managed by pip

    iii) execute `pip3 install torch torchvision tensorflow-datasets`

6. Now, within the same environment, execute `jupyter notebook` or `jupyter lab` to open Jupyter Notebook or Jupyter Lab editor. The later one is recommended out of the two.

**NOTE:** Everytime Anaconda Prompt is opened, it activates **base** environment by default. The target environment **deep-learning** has to be activated by entering command `conda activate deep-learning`.


**Visual Studio Code as an Editor**

Though Jupyter Notebook or Jupyter Lab should be sufficient for all the above-mentioned experiments, Visual Studio Code is also one of the most popular code editors. This can be installed by downloading Windows installer from official website and running the setup. Default setup should be fine for most cases.

**Required Extensions**

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

4. select **deep-learning (Python 3.13.2)**.

The VS Code editor should be ready for coding.



## Appendix

### TensorBoard

**In Jupyter Notebook/Lab**
Magic command to start TensorBoard inline within the Jupyter Notebook/Lab web editor

```
%load_ext tensorboard
%tensorboard --logdir=<logs_path> --port=6006 --bind_all
```

**Terminal**
If initialization for TensorBoard fails from the Jupyter notebook or lab., try executing the following command from terminal.

```
tensorboard --logdir=<logs_path> --port=6006 --bind_all
```


