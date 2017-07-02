# https://codeburst.io/python-friday-code-challenge-0-59802b8c21e
# Given csv of hourly temperature logs over several days, find out the largest temperature recorded

import pandas as pd

df = pd.read_csv('challenge0_testdata.csv')
print(df[df['temperature'] == max(df['temperature'])])


'''
Output:
     time        date  temperature
14  14:00  06-01-2017           99
'''