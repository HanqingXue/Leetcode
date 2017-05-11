#coding=utf-8
from matplotlib import pylab as plt
#--*-- coding:utf-8 --*--
from pylab import *
mpl.rc_params['font']

points = [[1,2], [2,3], [4,9], [5, 10], [3, 8], [8, 3], [4, 4], [0, 9], [0, 0],[-1, 2], [1, -3], [9, 9]]

plt.subplot(121)
plt.title(u'是凸包上点')
plt.scatter([x[0] for x in points], [x[1] for x in points], c='r')
plt.plot([1, 8], [-3, 3])
plt.subplot(122)
plt.title(u'不是凸包上点')
plt.scatter([x[0] for x in points], [x[1] for x in points], c='r')
plt.plot([4, 9], [4, 9])
plt.savefig('1.png')
plt.show()
