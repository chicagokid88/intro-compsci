#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:08:25 2017

@author: nicholasf
"""


#Final Exam - Question 3

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here

    numbers = ("1","2","3","4","5","6","7","8","9")
    sum = 0
    
    for i in s:
        if i in numbers:
            sum += int(i)
    
    return sum
     

#Final Exam - Question 3 (attempt 2)

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    

    try:
        type(s) == str
    except 
    

    numbers = ("1","2","3","4","5","6","7","8","9")
    sum = 0
    
    for i in s:
        if i in numbers:
            sum += int(i)
    
    return sum       


def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    # Your code here
    max=0
    
    for i in t:
        if type(i)==int:
            if i > max:
                max = i
                
        elif type(i)==list:
            if max_value(i) > max:
                max = max_value(i)
                
        elif type(i)==tuple:
             if max_value(i) > max:
                max = max_value(i)
                
        else:
            pass
        
    return max
        
        
        
        
        
        
#Final Exam - Question 5

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    key_code = {}
    decoded = ""
    
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
        
    for j in code:
        decoded += key_code[j]
    
    
    return (key_code, decoded)
        
        
#Final Exam - Question 6

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
        
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
            
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
        

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        if e in self.vals.keys():
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        if e not in self.vals.keys():
            return 0
        else:
            return self.vals[e]
        
    def __add__(self, other):
        new_dict = other.vals.copy()  # copy required to prevent updating `other.vals`
        for e in self.vals.keys():
            if e in other.vals.keys():
                new_dict[e] += self.vals[e]
            else:
                new_dict[e] = self.vals[e]
    
        # Create a new instance and populate it with new_dict
        new_instance = Bag()
        new_instance.vals.update(new_dict)
        return new_instance
    
    def __str__(self):
        # Use self.vals here not sef.new_dict
        s1 = ""
        for i in sorted(self.vals.keys()):
            s1 += str(i)+":"+str(self.vals[i])+"\n"
        return s1


class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        if e in self.vals.keys():
            del self.vals[e]
        
        

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        if e in self.vals.keys():
            return True
        else:
            return False

            
            
            
        
        
        
        