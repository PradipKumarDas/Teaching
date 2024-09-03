# DEEP LEARNING [21AML171]

## Teaching material and reference implementation for laboratory experiments.

**Acknowledgement**

Author's original repository is available at https://github.com/ageron/handson-ml3. Relevant implementations were modified to suit the classroom learning. 

### Package Installation
For _Anaconda_ Data Science platform, it is recommended to use its default package manager _Conda_ to install all required packages over the other package managers such as _Pip_ that may create package conflict across environments. But package installation using Conda may require administrative privilege. Package installation on local computers in Windows is recommeded over _Anaconda Prompt_ available in _Start -> Anaconda_ menu.

#### TensorFlow

Conda Installation:
`conda install conda-forge::tensorflow`

Pip Installation:
`pip install tensorflow`

#### TensorBoard

Conda Installation:
`conda install conda-forge::tensorboard`

Pip Installation:
`pip install tensorboard`

NOTE: After successful installation, TensorBoard can be loaded into the Jupyter notebook over the following commands.

```python
%load_ext tensorboard
%tensorboard --logdir <logdir>
```
In case of any concern loading TensorBoar inline in local computer, it can also be loaded externally over an web browser following the below mentioned steps.

Type following command in command prompt and copy the value of _Location_ property.
`pip show tensorboard`

Then append "/tensorboard/main.py" to the _Location_ property value and pass the complete tensorboard program path to the following command along with path to the log directory.
`python <copied_location>/tensorboard/main.py --logdir <logdir>`

Then copy the service TensorBoard URL to the browser to open it.

### Google Colaboratory (Google Colab)

There are few Jupyter notebook in this repository that are suggested to run on a Graphics Processing Unit (GPU) rather than on a Central Processing Unit (CPU) for faster model training. One of the providers that allows access to GPU over cloud is Google and it is available at https://colab.research.google.com. It provides free access to a GPU runtime up to certain amount of time before the runtime resets. Existing Google account is needed to login into Google Colab.

A new notebook can be created from the _Open notebook_ dialog. From the same dialog, an existing notebook can also be opened browsing from the available sources such as Google Drive and GitHub. A notebook located from local machine can also be uploaded from the _Upload_ option available in _File_ menu.

Before model training, an appropriate runtime needs to be selected. For all specific notebooks in this repository are suggested to select runtime type as _Python_ and _Hardware accelerator_ as _T4 GPU_ from the dialog _Change runtime type_. By default, Google Colab, stores all new notebook in a folder named _Colab Notebooks_ in connected Google Drive. 

#### TensorFlow Datasets

Few of the notebooks in this repository use TensorFlow datasets. But, few data science platforms do not come TensorFlow datasets preinstalled. To install the same, follow the package manager specific commands below.

Pip Installation:
`pip install tensorflow-datasets`

Conda Installation:
`conda install conda-forge::tensorflow-datasets`

### Other Datasets

Unless otherwise specified, datasets required for experiments are stored into folder _Data_ located in the root folder in this repository.

