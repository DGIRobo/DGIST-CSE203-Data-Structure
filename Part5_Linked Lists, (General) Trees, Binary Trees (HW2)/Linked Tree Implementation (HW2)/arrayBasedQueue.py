# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 00:20:38 2023

@author: fist5
"""

class ArrayBasedQueue:
    def __init__(self):
        self._arraySize = 10
        self._L = [None]*self._arraySize
        self._f = 0
        self._r = 0
        
    def size(self):
        return (self._arraySize - self._f + self._r) % self._arraySize
    
    def resize(self):
        self._arraySize = self._arraySize * 2
        newArray = [None]*self._arraySize
        for i in range(0,self._arraySize//2 - 1):
            newArray[i] = self._L[(self._f + i) % (self._arraySize//2)]
        self._L = newArray
        self._f = 0
        self._r = self._arraySize//2 - 1
    
    def enqueue(self, o):
        if self.size() == self._arraySize - 1:
            self.resize()
        self._L[self._r] = o
        self._r = (self._r + 1) % self._arraySize
    
    def dequeue(self):
        value = self._L[self._f]
        self._L[self._f] = None
        self._f = (self._f + 1) % self._arraySize
        return value

Q = ArrayBasedQueue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(1)
Q.enqueue(2)