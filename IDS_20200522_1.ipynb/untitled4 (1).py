# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bMQzvJXMO_HbKIwvAbimHvvME4w-CtbK
"""

x = int(input("請輸入起始的正整數:"))
y = int(input("請輸入終止的正整數:"))
odds = []
for i in range(x, y+1):
    mod = i % 2
    if mod == 1:
        odds.append(i)
    #print(i)
print(odds)      #奇數為何
print(len(odds)) #記數
print(sum(odds)) #加總