### Bike2Car

## 2020XILINX 暑期学校项目  
# team:Bike2Car

1、本系统是基于[spooNN](https://github.com/fpgasystems/spooNN)的基础上使用我们自己的训练集和测试集在pynq-z2平台上对交通标志的检测。

2、系统整体是由： 图像采集模块、图像处理模块和结果显示模块构成

3、使用lenet网络基于tensorflow框架在训练交通标志牌数据集上进行训练。
同时修改lenet网络，在卷积层后引入BN层，加快网络是收敛；制作数据集，选用交通标志数据集；对于lenet网络进行训练负责同学使用远程服务器，显卡型号Titan V,运行环境Ubuntu16.04.

4、通过使用vivado_hls工具将编写好需要加速的神经网络模型综合，导出IP以后添加到vivado工程中。在综合时我们将训练好的参数文件和配置文件添加到神经网络中去。

5、将生成bit流的tcl,bit，hwh文件存储到pynq jupyter文件夹下（事先已经安装2.5镜像文件），pynq-z2启动以后，我们将python的notebook文件打开以后进行检测。















NOTE:数据集百度云盘链接：
[here](https://pan.baidu.com/s/1T_M1QsgLPP7PS1eXq9i1cA) 
提取码：c9fx
