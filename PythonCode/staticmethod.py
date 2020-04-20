# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 11:20
# @Author  : Chensy Cao
# @Email   : chensy.cao@zjtlcb.com
# @FileName: staticmethod.py
# @Software: PyCharm


class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化