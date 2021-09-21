# 导入相应的模块
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
# 加载数据
fashion_mnist=keras.datasets.fashion_mnist
# 进行训练集与测试集的划分
(train_images,train_lables),(test_images,test_lables)=fashion_mnist.load_data()
# 数据预处理
train_images=train_images/255.0
test_images=test_images/255.0
# 搭建简单的神经网络模型
def create_model():
#     创建神经网络模型
    model=tf.keras.models.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation="relu"),
        keras.layers.Dense(10)
    ])
#     编译模型
    model.compile(
        optimizer="adam",
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=tf.metrics.SparseCategoricalAccuracy()
    )
#     返回模型
    return model
# 构造模型
new_model=create_model()
# 训练模型
new_model.fit(train_images,train_lables,epochs=10)
# 保存模型
new_model.save("model/my_model3.h5")
