# FaceDetection

采用库：opencv-python dlib numpy 

## 安装环境

### Windows

```shell
pip install opencv-python

pip install dlib==19.8.1
```

目前19.8.1及之前的版本支持.whl免编译安装，如果要安装最新版则需要采用编译安装的方式：

1. 确保有安装Visual Studio，因为boost在Windows下需要使用Visual Studio的组件编译安装。
2. 下载boost源文件解压后双击bootstrap.bat，在同目录下会生成b2.exe与bjam.exe两个文件。
3. 命令输入

```shell
bjam install --toolset=msvc-10.0 architecture=x86 address-model=64 --build-type=complete --prefix="E:\boost_1_64_0\boost_1_64_0\bin\vc10_x64" link=static runtime-link=shared threading=multi debug release
```

进行编译安装

参数解释：

- link=shared    可以生成dll。  （.\bjam.exe link=shared)
- - toolset=msvc-14.1 即VS2017    (我用的vs2017)                    
  - toolset=msvc-12.0 即VS2013                   
  - toolset=msvc-10.0 即VS2010                   
  - toolset=msvc-9.0  即VS2008 
- --with-xxxx                             如果你要编 chrono，就用  --with-chrono     
- --stagedir="./vc2017"            自己设定一个输出目录  
- address-model=64                 设定32或者64位模式

1. 下载安装CMake
2. 编译安装Dlib

```shell
pip install dlib
```



### Linux

```
sudo apt install cmake boost-dev
pip install opencv-python
pip install dlib
```



### Mac

```
brew install cmake brew install boost brew install boost-python --with-python3

pip install opencv-python

pip install dlib
```

