import numpy as np
import os.path


def img32_to_1024(filename):
    returnVec = np.zeros((1, 1024))  # 生成1行，1024列的矩阵向量，便于计算
    file = open('E:/test/' + filename, 'r')
    linestr = file.readlines()
    for i in range(32):
        for n in range(32):
            returnVec[0, i * 32 + n] = int(linestr[i][n])
    return (returnVec)


def test(index, k):  # KNN计算部分函数，传入测试数据向量和k值
    dataSetSize = m
    diffMat = index - trainingMat  # 以下四行即欧式公式计算距离
    diffMat1 = diffMat ** 2
    diffMat2 = diffMat1.sum(axis=1)
    distances = diffMat2 ** 0.5
    sortedDistances = distances.argsort()  # 计算结果排序
    classCount = {}
    for i in range(k):  # 计算K个数据中哪个数字是最多的
        voteIlabel = handWriteLabels[sortedDistances[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), reverse=True)
    return sortedClassCount[0][0]  # 返回计算出的手写数字值


# 训练数据集处理
handWriteLabels = []
trainingFileList = os.listdir('E:/test/trainingDigits')
m = len(trainingFileList)
trainingMat = np.zeros((m, 1024))
for i in range(m):
    fileNameStr = trainingFileList[i]
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    handWriteLabels.append(classNumStr)
    trainingMat[i, :] = img32_to_1024('trainingDigits/' + fileNameStr)

# 测试数据集处理
testFileList = os.listdir('E:/test/testDigits')
errorCount = 0.0  # 用于计算错误率
mTest = len(testFileList)
realLabel = []
testLabel = []
for i in range(mTest):
    fileNameStr = testFileList[i]
    fileStr = fileNameStr.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    vectorUnderTest = img32_to_1024('testDigits/' + fileNameStr)
    testLabel = test(vectorUnderTest, 1)  # 1为k值，可修改为2、3、4……
    print('识别出的数字为:' + str(testLabel) + '真实数字为:' + str(classNumStr))
    if (testLabel != classNumStr):
        errorCount += 1.0

print('错误率' + str(errorCount / mTest))

