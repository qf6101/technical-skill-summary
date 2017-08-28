# Install Prerequisites

```
apt-get install graphviz-dev graphviz htop pkg-config pv parallel byobu tmux build-essential libboost-all-dev zlib1g-dev maven git linux-headers-amd64 libatlas-base-dev libopencv-dev
apt-get install freeglut3-dev libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev
```

# Install Cuda Toolkit

Follow the 'Runfile Installer' section: http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

# Install CuDNN

Download and extract the cuDNN archive from https://developer.nvidia.com/cudnn.

Copy the files to /usr/local/cuda directory and re-create soft link.

```
tar zxvf cudnn-8.0-linux-x64-v5.1.tgz
cp cuda/include/* /usr/local/cuda/include/
cp cuda/lib64/* /usr/local/cuda/lib64/
cd /usr/local/cuda/lib64
rm libcudnn.so.5
rm libcudnn.so
ln -s libcudnn.so.5.1.5 libcudnn.so.5
ln -s libcudnn.so.5 libcudnn.so
```

# Install Anaconda

Download the Anaconda 3.5.x and install it.

```
mv $ANACONDA_HOME/bin/../lib/libgomp.so.1 $ANACONDA_HOME/bin/../lib/libgomp.so.1.bak
mv $ANACONDA_HOME/bin/../lib/libstdc++.so.6 $ANACONDA_HOME/bin/../lib/libstdc++.so.6.bak
```

Create ~/.pip/pip.conf with the following content to speed up the downloading.
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn/simple/
```

# Install MXNet

Follow the documents: https://github.com/dmlc/mxnet

```
git clone https://github.com/dmlc/mxnet.git --recursive
```

Modify 'mxnet/make/config.mk' with USE_CUDA = 1 and USE_CUDA_PATH = /usr/local/cuda.

```
cd mxnet
make clean
make -j4
cd python & python setup.py install
```
# Install Tensorflow

Follow the documents: https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#test-the-tensorflow-installation

```
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc2-cp35-cp35m-linux_x86_64.whl
pip install --upgrade $TF_BINARY_URL
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/protobuf-3.0.0-cp3-none-linux_x86_64.whl
```

# Install Theano

```
pip install Theano
```

Create .theanorc file in $HOME.
```
[global]
floatX = float32
device = cuda0

[lib]
cnmem = 1

[nvcc]
flags=-D_FORCE_INLINES

```

# Install Keras

```
pip install keras
```

# Install Tensorlayer

```
export QT_QPA_PLATFORM=offscreen
```
