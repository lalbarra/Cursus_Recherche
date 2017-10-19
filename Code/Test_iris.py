# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:50:29 2017

@author: loic
"""

from sklearn.datasets import load_iris
data = load_iris()
data.target[[10, 25, 50]]
array([0, 0, 1])
list(data.target_names)
['setosa', 'versicolor', 'virginica']