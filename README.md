### Bike2Car

# 2020XILINX 暑期学校项目  team:Bike2Car











NOTE:数据集百度云盘链接：
[here](https://pan.baidu.com/s/1T_M1QsgLPP7PS1eXq9i1cA) 
提取码：c9fx

> 该项目使用了spooNN中的hls-nn-lib的hls加速库，参考了mnist-cnn的深度学习网络结构。
>
> 下面步骤在ubuntu18.04中完成。

## 1. Train

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



> `$ vivado_hls -f ~/Bike2Car/scripts/create_hls.tcl -tclargs "hls_project" "~/Bike2Car/hls/" "~/Bike2Car/hls-nn-lib/"`



