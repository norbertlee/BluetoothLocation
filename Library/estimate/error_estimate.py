#!home/suyexuan/anaconda3/envs/ib_model
# Encoding: UTF-8
"""
@license: MIT License Copyright (c) 2019 
@project:BluetoothToolsPlatform
@file: error_estimate.py
@author: suyexuan
@email:1479003073@qq.com
@software: PyCharm
@time: 19-4-23 下午3:07
@desc: 误差评估
"""
import numpy as np


def estimate_error(error_list, confidence):
    """
    误差评估
    :param error_list: list 误差list
    :param confidence: int 置信度(1-5)
    :return: dict
    """
    error_mean = np.array(error_list).mean()  # 均值
    error_std = np.array(error_list).std()  # 标准差
    error_absolute = error_mean + confidence * error_std()  # 置信区间最大值
    return {'mean': error_mean, 'std': error_std, 'error': error_absolute, 'confidence': confidence}


def calculate_error(result, target):
    """
    计算误差
    :param result: list 计算位置 [x,y,z]
    :param target: list 目标位置 [x,y,z]
    :return: float 误差
    """
    return np.linalg.norm(np.array(result) - np.array(target))
