# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:26:32 2017

@author: Administrator
"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  result = 0
  for score in scores:
    variance = variance + ((average - score)**2)
  result = variance / float(len(scores))
  
  return result

def grades_std_deviation(variance):
  return(variance**0.5)

variance = 0
print_grades(grades)
print ( "Sum of Grades =" + str(grades_sum(grades)))
print ( "Average Grade =" + str(grades_average(grades)))
variance = grades_variance(grades)
print ( "Variance = " + str(variance))
print ( "Std Devication=" + str(grades_std_deviation(variance)))