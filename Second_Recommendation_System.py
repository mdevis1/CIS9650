#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 22:19:39 2020

@author: kristkikina
"""
#Second Recommendation System where user will input their interests on hobbies listed below on a scale of 1-10

#The program will then find all observations of people who share the same interests and will print out their age and field of work/study

#This program takes into consideration interests that are also: 1 minus the interest input by the user and 1 plus the interest input by the user
#Meaning if user input an interest of 5 for sports, the program will find matches whose interest is 4 , 5 , or 6 for sports


import pandas as pd
master = pd.read_csv("speed-dating2_V3.csv")
print(master)

gender = input("Enter your gender: ")
preferance = input("Enter your preferance: ")

if (gender=="male"):
    if (preferance=="female"):
        date_gender="female"
    else:
        date_gender="male"
else:
    if (preferance=="male"):
        date_gender="male"
    else:
        date_gender="female"

select = master[master['gender'] == date_gender]


# input interests in hobbies
int_sports = int(input("Enter your interest in sports: "))
int_exercise = int(input("Enter your interest in exercise: "))
int_dining = int(input("Enter your interest in dining: "))
int_art = int(input("Enter your interest in art: "))
int_clubbing = int(input("Enter your interest in clubbing: "))
int_music = int(input("Enter your interest in music: "))
int_shopping = int(input("Enter your interest in shopping: "))

#for loop to filter the qualified people
lst=[]
for i in select.index:
    if (select["sports"][i] in range(int_sports-1, int_sports+2)):
        if (select["exercise"][i] in range(int_exercise-1, int_exercise+2)):
            if (select["dining"][i] in range(int_dining-1, int_dining+2)):
                if (select["art"][i] in range(int_art-1, int_art+2)):
                    if (select["music"][i] in range(int_music-1, int_music+2)):
                        if (select["shopping"][i] in range(int_shopping-1, int_shopping+2)):
                            lst.append(i) 
                
                

#output                
if date_gender == "male":
    print_name = "Male"
else:
    print_name = "Female"
count = 0    
for i in lst:
    count += 1
print("\nWe found",count,"potential matches:")
count = 0
for i in lst:
    count += 1
    print("Match",count,print_name +" age "+ str(master["age"][i]),"working in",(master["field"][i]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    