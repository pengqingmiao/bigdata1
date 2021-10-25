import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0,np.pi/2,100)
# x = np.linspace(-2*np.pi,2*np.pi,1000)
# y = np.linspace(-2,2,1000)
# 创建一张画布
# figure1 = plt.figure()
# plt.plot(x,2*x*x*x*x+3*x*x*x+2*x*x+x+1,label="a")
# plt.plot(x,x*x,label="a")
# plt.plot(x,2*np.sin(2*x+np.pi/4),label="a")
# plt.plot(x,2*np.cos(2*x+np.pi/4),label="b")
# plt.plot(x,np.tan(x),label="b")
# plt.plot(x,x*x,label="y=sin(x)")
# plt.plot(x,x*x,label="y=sin(x)")
# plt.legend()
# plt.show()
# 构建两个列表
# a = [1,3,5,6,7]
# b = [1,2,4,6,8]
# c = [2,3,4,5,8]
# d = [8,4,6,9,7]


# 创建一张画布
# plot 折线图，
# figure1 = plt.figure()
# plt.plot(a,b,label="a")
# plt.plot(c,d,label="b")
# plt.legend()
# # plt.show()
# figure2 = plt.figure()
# plt.plot(a,b,label="c")
# plt.plot(c,d,label="d")
# plt.legend()
# figure3 = plt.figure()
# figure4 = plt.figure()
# figure5 = plt.figure()
# figure6 = plt.figure()

# 去掉边框
ax = plt.gca()
# get current axis获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置中心的为（0,0）的坐标轴
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
# plt.xticks(rotation=45)
plt.xlim(-3.0,3.0)
plt.ylim(-1,1)
plt.show()
