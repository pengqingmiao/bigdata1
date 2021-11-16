from PIL import Image
import matplotlib.pylab as plt
import numpy as np
import os.path


def pic_change(filename):
    img = Image.open('D:/YOLOv52/十大算法/knn手写体/pic/' + filename)  # 我的文件路径为E:/test/pic/下，可修改
    raw_data = img.load()  # 加载图片

    # 降噪部分
    for x in range(img.size[0]):  # x*y即像素值，x为行，y为列，遍历每个像素进行降噪
        for y in range(img.size[1]):
            if raw_data[x, y][0] < 90:  # 遍历像素，png图片每个像素有RGBA四个值，A值指透明度，透明度统一设为255
                raw_data[x, y] = (0, 0, 0, 255)

    # for x in range(img.size[1]):
    #     for y in range(img.size[0]):
    #         if raw_data[x, y][1] <136:
    #             raw_data[x, y] = (0, 0, 0, 255)
    #
    # for x in range(img.size[1]):
    #     for y in range(img.size[0]):
    #         if raw_data[x, y][2] > 0:
    #             raw_data[x, y] = (255, 255, 255, 255)

    resize_img = img.resize((32, 32), Image.LANCZOS)  # 修改图片大小为32*32像素
    resize_img.save('D:/YOLOv52/十大算法/knn手写体/new_/' + filename)  # 存储新图片，可删

    array = plt.array(resize_img)
    gray_array = np.zeros((32, 32))
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            Gray = array[x, y][0] * 0.299 + array[x, y][1] * 0.587 + array[x, y][2] * 0.114  # 灰度公式计算每个像素点，将图片的每个像素转为0或1
            if Gray == 255:
                gray_array[x, y] = 0
            else:
                gray_array[x, y] = 1
    testFileList = os.listdir('D:/YOLOv52/十大算法/knn手写体/testDigits/')
    mTest = len(testFileList)
    num = 0
    for i in range(mTest):  # 将转换好的图片存储在E:/test/testDigits文件夹下，这一部分为防止重名，对文件名中序号进行判断
        testName = testFileList[i].split('_')[0]
        if testName == filename.split('.')[0]:
            num = num + 1
    new_txt_name = filename.split('.')[0] + '_' + str(num + 1) + '.txt'  # 文件名格式为8_1.txt,8值这个数字的真实值，1为序号
    np.savetxt('D:/YOLOv52/十大算法/knn手写体/testDigits/' + new_txt_name, gray_array, fmt='%d', delimiter='')
    print(new_txt_name)
    return new_txt_name


pic_list = os.listdir('D:/YOLOv52/十大算法/knn手写体/pic')  # 未处理的图片放在E:/test/pic文件夹下，处理完成后放在E:/test/testDigits文件夹下
n = len(pic_list)  # 遍历，对每张图片进行处理
for k in range(n):
    print(pic_list[k])
    pic_change(pic_list[k])