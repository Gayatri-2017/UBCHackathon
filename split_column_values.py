# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:18:16 2019

@author: Suguna Menon
"""

import numpy as np
from itertools import chain
import pandas as pd


df = pd.read_csv("ubc_course_calendar_data.csv")
df

s = df['INSTRUCTORS'].str.split(';').apply(pd.Series, 1).stack()
s.index = s.index.droplevel(-1)
s.name = 'INSTRUCTORS'
s

del df['INSTRUCTORS']
df_new = df.join(s)

#x = df_new[(df_new["COURSE_NUMBER"] == '300') & (df_new["COURSE_TITLE"] == 'INTRO TO PCOL')]

df_new.to_csv('ubc_course_calendar_data_new.csv', sep=',', encoding='utf-8', index = False)