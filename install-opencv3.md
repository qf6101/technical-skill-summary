### 自动安装opencv3

```
conda install --channel https://conda.anaconda.org/menpo opencv3
```

https://github.com/menpo/conda-opencv3/blob/master/README.md

注意：低版本debian系统，会遇到glibc版本过低的问题（cuda驱动7.5安装可能也会遇到整个问题），需要手动安装opencv。

### 下载安装opencv3

从https://pypi.python.org/pypi/opencv-python/3.1.0.3#downloads 下载 opencv_python-3.1.0.3-cp35-cp35m-manylinux1_x86_64.whl 后pip install。

### 编译安装opencv3

* 把anaconda的头文件拷贝到同一目录下

拷贝/home/idm/.local/anaconda2/include下的.h文件及/home/idm/.local/anaconda2/include/python2.7/下所有文件至/home/idm/.local/anaconda2/include/build_for_opencv

拷贝/home/idm/.local/anaconda3/include下的.h文件及/home/idm/.local/anaconda3/include/python3.5m/下所有文件至/home/idm/.local/anaconda3/include/build_for_opencv

* 配置编译选项

opencv源码目录：/home/idm/Downloads/opencv/opencv-3.1.0

opencv build目录：/home/idm/Downloads/opencv/opencv-3.1.0/build

opencv安装目录：/home/idm/.local/opencv310

python2安装目录：/home/idm/.local/anaconda2

python3安装目录：/home/idm/.local/anaconda3

进入opencv build目录，执行下面命令：

```
cmake \
-D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/home/idm/.local/opencv310 \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D BUILD_EXAMPLES=ON \
-D WITH_CUDA=OFF \
-D PYTHON2_EXECUTABLE=/home/idm/.local/anaconda2/bin/python \
-D PYTHON2_INCLUDE_DIR=/home/idm/.local/anaconda2/include/build_for_opencv \
-D PYTHON2_LIBRARY=/home/idm/.local/anaconda2/lib/libpython2.7.so \
-D PYTHON2_PACKAGES_PATH=/home/idm/.local/anaconda2/lib/python2.7/site-packages/ \
-D PYTHON2_NUMPY_INCLUDE_DIRS=/home/idm/.local/anaconda2/lib/python2.7/site-packages/numpy/core/include \
-D PYTHON3_EXECUTABLE=/home/idm/.local/anaconda3/bin/python \
-D PYTHON3_LIBRARY=/home/idm/.local/anaconda3/lib/libpython3.5m.so \
-D PYTHON3_INCLUDE_DIR=/home/idm/.local/anaconda3/include/build_for_opencv \
-D PYTHON3_PACKAGES_PATH=/home/idm/.local/anaconda3/lib/python3.5/site-packages/ \
-D PYTHON3_NUMPY_INCLUDE_DIRS=/home/idm/.local/anaconda3/lib/python3.5/site-packages/numpy/core/include \
-D PYTHON_DEFAULT_AVAILABLE=/home/idm/.local/anaconda3/bin/python \
..
```

* 编译安装
```
make -j6
make install
```
