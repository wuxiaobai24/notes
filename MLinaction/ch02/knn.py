import numpy as np
import operator
from os import listdir


def createDateSet():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # 欧式距离计算
    diffMat = np.tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistance = sqDiffMat.sum(axis=1)
    distances = sqDistance**0.5
    #找出前k个距离最小的sample
    sortedDistIndicies = distances.argsort() # 这里返回的是indicies
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), 
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 将文本记录到转换NumPy的解析程序
def file2matrix(filename):
    with open(filename) as f:
        arrayOfLines = f.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = np.zeros((numberOfLines, 3)) #3是因为有三个特征
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFormLine = line.split('\t')
        returnMat[index, :] = listFormLine[0:3]
        classLabelVector.append(int(listFormLine[-1])) #Label
        index += 1
    return returnMat, classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0) #参数是指定axis，所以返回的是一个array
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1)) #不是矩阵除法，而是逐项相除
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:],\
                                    datingLabels[numTestVecs:m], 3)
        print('the classifyer came back with %d, the real answer is %d' \
             % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / numTestVecs))


def classifyPerson():
    resultList = ['not at all', 'in samll doses', 'in lager doses']
    percentTats = float(input("percentage of time spent playing video games"))
    ffMiles = float(input("frequent flier miles earned per years?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
    normMat, ranges, minVals, = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classiferResult = classify0((inArr-minVals)/ranges, 
                                normMat, datingLabels, 3)
    print("You will probably like this person: ", \
         resultList[classiferResult - 1])

# 图片转向量
def img2vector(fileName):
    returnVect = np.zeros((1, 1024))
    with open(fileName) as f:
        i = 0
        for line in f:
            for j in range(32):
                returnVect[0, 32*i + j] = int(line[j])
    return returnVect

def hardwritingClassTest():
    hwLabels = []
    traingFileList = listdir('trainingDigits')
    m = len(traingFileList)
    traingFileMat = np.zeros((m, 1024))
    for i in range(m):
        fileNameStr = traingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumber = int(fileStr.split('_')[0])
        hwLabels.append(classNumber)
        traingFileMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumber = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector("testDigits/%s" % fileNameStr)
        classiferResult = classify0(vectorUnderTest, \
                                   traingFileMat, hwLabels, 3)
        print("the classifer came back with: %d, the real answer is: %d" \
             % (classiferResult, classNumber))
        if (classiferResult != classNumber): errorCount += 1.0
    print("\nthe total number of error is %d" % errorCount)
    print("\nthe total error rate is %f", (errorCount/float(mTest)))



