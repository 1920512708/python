# -*- coding: utf-8 -*-

#coding=utf-8
from numpy import *

#计算两个向量的距离，用的是欧几里得距离
def distEclud(vecA, vecB):   
    return sqrt(sum(power(vecA - vecB, 2)))

#随机生成初始的质心,在数据范围内随机选择或选择随机数据中的点，以下是数据范围内的点   
def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(array(dataSet)[:,j]) - minJ)#生成距离范围
        centroids[:,j] = minJ + rangeJ * random.rand(k,1)#生成质点
    return centroids
    
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))#建立mX2维矩阵存放个样本点
                                     
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:#各簇样本不再变化则clusterChanged=false
        clusterChanged = False
        for i in range(m):#把所有样本点分到距离最近的质点
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])#求样本与质点间的距离
                if distJI < minDist:#如果距离小于最小距离则改变该样本点簇的归属
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: #如果该样本点划分的簇值改变，则clusterChanged变为ture，继续迭代
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        print(centroids)
        for cent in range(k):#重新计算质点
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]#获取该簇的所有样本点
            centroids[cent,:] = mean(ptsInClust, axis=0) # 求数据各维均值
    return centroids, clusterAssment
    
def show(dataSet, k, centroids, clusterAssment):
    from matplotlib import pyplot as plt  
    numSamples, dim = dataSet.shape  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
    for i in xrange(numSamples):  
        markIndex = int(clusterAssment[i, 0])  
        plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    for i in range(k):  
        plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)  
    plt.show()
      
def main():
    dataMat = mat(zeros( (m,n) ))
    myCentroids, clustAssing= kMeans(dataMat,4)
    print myCentroids
    show(dataMat, 4, myCentroids, clustAssing)  
    
    
if __name__ == '__main__':
    main()
