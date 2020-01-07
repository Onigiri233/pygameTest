#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 18:08
# @Author  : FanTuan
# @File    : objTest.py
import math
from gameobjects.vector2 import *



# class Vector2(object):
#     def __init__(self, x=0.0, y=0.0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return "(%s, %s)" % (self.x, self.y)
#     @classmethod
#     def from_points(cls, p1, p2):
#         return cls(p2[0]-p1[0],p2[1]-p1[1])
#     # 向量大小
#     def get_magnitude(self):
#         return math.sqrt(self.x ** 2 + self.y ** 2)
#     # 单位化
#     def normalize(self):
#         magnitude = self.get_magnitude()
#         self.x /= magnitude
#         self.y /= magnitude
#
#     def __add__(self, rhs):
#         return Vector2(self.x + rhs.x, self.y + rhs.y)
#
#     def __sub__(self, rhs):
#         return Vector2(self.x - rhs.x, self.y - rhs.y)
#
#     def __mul__(self, scalar):
#         return Vector2(self.x * scalar, self.y * scalar)
#
#     def __div__(self, scalar):
#         return Vector2(self.x / scalar, self.y / scalar)
# 我们可以使用下面的方法来计算两个点之间的向量
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print AB