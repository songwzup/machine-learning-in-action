# -*- coding: utf-8 -*-
'''
Created on 2015年9月29日

@author: rains
'''
import matplotlib.pyplot as plt
import numpy as np

import kNN

#mat1,fab1 = kNN.file2matrix("datingTestSet.txt")

#查看训练集
# fig=plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(mat1[:,0],mat1[:,1],15.0*np.array(fab1),15.0*np.array(fab1))
# plt.show()

#测试归一化
#mat1 = kNN.autoNorm(mat1)

#测试简单的分类器准确率
kNN.datingClassTest()

#手写数字识别
#kNN.handwritingClassTest()
