# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Class in heritence examples
# Single level inhertence

class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A): # inheriting from class A
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")


b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

# Multi level inhertence
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B: # inheriting from class A
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

class C(A,B):
    def feature5(self):
        print("This is feature 5")

c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()

# using super() constructor and MRO (Method Resolution Order)

le# ts say we want to access the __init__ of B from class D

class B:
    def __init__(self):
        print("This is init of B")

    def featureB(self):
        print("This is feature B")

class C(B):
    def __init__(self):
        super().__init__() # this super() constructor can help us access any methods / class level attributes (__init__)


c = C()
c

# multiple class level inheritence and using super() MRO example - the left most super class is always preferred.
class A:
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B:
    def __init__(self):
        print("This is init of B")

    def featureB(self):
        print("This is feature B")

class C(A,B):
    def __init__(self):
        super().__init__() # the init of B will be inherited as per MRO

    def inheritFeatB(self):
        super().featureB()
    def inheritFeatA(self):
        super().feature2()


c = C()
c.inheritFeatB()
c.inheritFeatA()


class B:
    def __init__(self):
        print("This is init of B")

    def featureB(self):
        print("This is feature B")

class A(B):
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

a = A() # the code look for A class's init method first and if found then execute else execute the super class B's init method


