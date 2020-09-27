# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 17:47:48 2020

@author: Soaib
"""
# Ordinary Least Square
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_
