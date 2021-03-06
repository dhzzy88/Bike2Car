### Bike2Car

## 2020XILINX 暑期学校项目  
# team:Bike2Car

1、本系统是基于[spooNN](https://github.com/fpgasystems/spooNN)的基础上使用我们自己的训练集和测试集在pynq-z2平台上对交通标志的检测。

2、系统整体是由： 图像采集模块、图像处理模块和结果显示模块构成

3、使用lenet网络基于tensorflow框架在训练交通标志牌数据集上进行训练。
同时修改lenet网络，在卷积层后引入BN层，加快网络是收敛；制作数据集，选用交通标志数据集；对于lenet网络进行训练负责同学使用远程服务器，显卡型号Titan V,运行环境Ubuntu16.04.

4、通过使用vivado_hls工具将编写好需要加速的神经网络模型综合，导出IP以后添加到vivado工程中。在综合时我们将训练好的参数文件和配置文件添加到神经网络中去。

5、将生成bit流的tcl,bit，hwh文件存储到pynq jupyter文件夹下（事先已经安装2.5镜像文件），pynq-z2启动以后，我们将python的notebook文件打开以后进行检测。



> 该项目使用了spooNN中的hls-nn-lib的hls加速库，参考了mnist-cnn的深度学习网络结构。
>
> 下面步骤在ubuntu18.04中完成。

##  Train

- 训练CNN网络模型参数，需要构建一套tensorflow的框架（建议使用GPU版本）。

> `$ git clone https://github.com/dhzzy88/Bike2Car.git`
>
> `$ cd Bike2Car`
>
> `$ cp -r tensorflow_data/ ~`

- 训练模型

> `$ cd training/`
>
> `$ python3 ./cnn.py 1`
>
> ` $ python3 ./cnn.py 2 --meta ./train_log/mnist-cnn/*.meta --model ./train_log/mnist-cnn/*data-00000-of-00001 --output weights.npy`

## 生成RTL工程

> `$ vivado_hls -f ~/Bike2Car/scripts/create_hls.tcl -tclargs "hls_project" "~/Bike2Car/hls/" "~/Bike2Car/hls-nn-lib/"`

在生成的RTL工程可以导出IP、安装IP后生成bitstream，通过PYNQ部署到PYNQ-Z2中。

