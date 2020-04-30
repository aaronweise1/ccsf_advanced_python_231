#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
'''
explanation
if more than one statement was authorized I would do it as below:
pth ='/users/abrick/resources/english'
ct=0
t=0
fl=open(pth,"r") #read the file
lines=fl.readlines() # make it a []
for ln in lines: #loop for each line
    for word in ln.split(): split word in list
        t =t +1  #count number  of words
        if word == (word[::-1]):  #check if it is a palydrome
            ct = ct +1  #count number of palydromes

print("{} palydromes found ".format(ct)) #pring the number of palydromes

but to reduce the number of statements I will
a) suppress the variables such as pthn ,fl,etc.
replacing them with their value
b) use comprehension to flatten the for loops
a+b make a rather incomprehensible single line, but
it is one statement as requested for the home work
as shown below
'''
print("{} palydromes found ".format(len([ '1'  for  ln in open('/users/abrick/resources/english',"r").readlines()  if ln.strip('\n')  == (ln.strip('\n')[::-1]) ])))
