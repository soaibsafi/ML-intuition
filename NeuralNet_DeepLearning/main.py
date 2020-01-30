#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:10:25 2020

@author: soaib
"""

import data_loader
import pickle

training_data, validation_data, test_data = data_loader.load_data_wrapper()

import network1
net = network1.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data = test_data)
clf = net.SGD(training_data, 30, 10, 0.001, test_data = test_data)
s=pickle.dumps(clf)
clf2=pickle.loads(s)
print(clf2)
