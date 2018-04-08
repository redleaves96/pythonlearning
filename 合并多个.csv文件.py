# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 20:17:52 2018

@author: ASUS
"""
import glob

def hebing():
   csv_list = glob.glob('E:\\round1\\*.csv')
   print(u'共发现%s个CSV文件'% len(csv_list))
   print(u'正在处理............')
   for i in csv_list:
      fr = open(i,'r').read()
      with open('E:\\allstock\\alltest.csv','a') as f:
          f.write(fr)
hebing()