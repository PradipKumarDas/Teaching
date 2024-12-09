# ADVANCED MACHINE LEARNING [22AML154]
***TEACHING MATERIAL AND REFERENCE IMPLEMENTATION FOR LABORATORY EXPERIMENTS.***

**Acknowledgement**

Author's original repository is available at https://github.com/ageron/handson-ml3. Relevant implementations were modified to suit the classroom learning. 

## Package Installation
For _Anaconda_ Data Science platform, it is recommended to use its default package manager _Conda_ to install all required packages over the other package managers such as _Pip_ that may create package conflict across environments. But package installation using Conda may require administrative privilege. Package installation on local computers in Windows is recommeded over _Anaconda Prompt_ available in _Start -> Anaconda_ menu.

### Keras Tuner

Conda Installation:
`conda install conda-forge::keras-tuner`

Pip Installation:
`pip install keras-tuner`


### TensorFlow

Conda Installation:
`conda install conda-forge::tensorflow`

Pip Installation:
`pip install tensorflow`

### TensorBoard

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


