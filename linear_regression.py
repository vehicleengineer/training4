%matplotlib inline    #适用于jupter notebook，直接将图像嵌入到console界面
from IPython import display  
from matplotlib import pyplot as plt #绘图命令
from mxnet import atuograd, nd   #自动求梯度
import random

#生成数据集
num_inputs = 2
num_examples = 1000
true_w = [2,-3.4]
true_b = 4.2
features = nd.random.normal(scale=1, shape=(num_examples,num_inputs))
labels = true_w[0] * features[:, 0] + true_w[1] * features[:, 1] + trure_b
labels += na.random.normal(scale=0.01, shape=labels.shape)

#读取数据
def data_iter(batch_size, features,labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)   #shuffle打乱数据顺序
    for i in range(0, num_examples, batch_size):
        j = nd.array(indices[i:min(i+batch_size,num_examples)])
        yield features.take(j), labels.take(j)

#初始化模型参数
w = nd.random.noraml(scale=0.01, shape=(num_inputs,1))
b = nd.zeros(shape=(1,))
#声明哪个变量需要求梯度
w.attach_grad()
b.attach_grad()

#定义模型
def linreg(X, w, b):
    return nd.dot(X,w) + b

#定义损失函数
def squared_loss(y_hat, y):
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

#定义迭代迭代优化算法
def sgd(params, lr ,batch_size):
    for param in params:
        param[:] = param - lr * param.grad / batch_size

#训练模型
lr = 0.03
num_epochs = 3   #hyperparamter 人为调参
net = linreg
loss = squared_loss

for epoch in range(num_epochs):
    for X,y in data_iter(batch_size, features, labels):
        with autograd.record():
            l = loss(net(X,w ,b), y)
        l.backward()
        sgd([w, b], lr, batch_size)
    train_l = loss(net(features,w,b),labels)
    print('epoch %d, loss %f' % (epoch +1,train_l.mean().asnumpy()))
