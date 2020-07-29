import os
import struct
import numpy as np
import matplotlib.pyplot as plt
def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels.idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images.idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels


fig, ax = plt.subplots(
    nrows=2,
    ncols=5,
    sharex=True,
    sharey=True, )
X_train,y_train = load_mnist("./","t10k")


number =9  #0~9
num_style = 8 #0~5948 不同笔迹  //t10k 0~10000


ax = ax.flatten()
for i in range(90,100,1):
    img = X_train[y_train == 9][i].reshape(28, 28)      #img可以储存下来,单个的图片
    ax[i%10].imshow(img, cmap='Greys', interpolation='nearest')
print(X_train.shape)
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
