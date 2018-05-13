#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:53:44 2017

@author: nicholasf
"""

def f(x):
    print(x)
    while x>3:
        f(x+1)
     

def fats(x):
    a = []
    if x>0:
        a.append(x)
        f(x-1)




def Hello(x):
    print('hello')
    
    
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


#Midterm Question 4
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #YOUR CODE HERE
    n = 0
    v = 0
    
    for i in range(k):
        if v == k:
            break
        n += 1
        v += n
        
    if v == k:
        return True
    
    else:
        return False


#Midterm Question 5
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    string = ""
    
    for i in s:
        if i in ('a','e','i','o','u','A','E','I','O','U'):
            string = string
        else:
            string += i
            
    print(string)
    
#Midterm Question 6 - Copied Question

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    odd_times= {}
    maximum = 0
    for i in L:
        if i in odd_times:
            odd_times[i] += 1
        else:
            odd_times[i] = 1
            
    for i in odd_times:
        if odd_times[i] % 2 and i > maximum:
            maximum = i
        
    if maximum != 0:
        return maximum
    else:
        return None
    

#Midterm Question 6 - Nick's Attempted Solution
def largest_odd_times(L):  
    while len(L)>0:
        value = max(L)
        count = 0
        for i in L:
            if i == value:
                count +=1
            else:
                count = count
        if count == 0:
            return None
            break
        elif count%2!=0:
            return value
            break
        else:
            count = 0
            for i in L:
                L.remove(value)
            print(L)
    
    
    
def largest_odd_times(L):
        """ Assumes L is a non-empty list of ints
                Returns the largest element of L that occurs an odd number 
                of times in L. If no such element exists, returns None """

        # declaring odd hash for storing the frequency of each element
        oddHash = {}

        # storing the frequency of each element
        for each_elm in L:
                if each_elm in oddHash:
                        oddHash[each_elm] += 1
                else:
                        oddHash[each_elm] = 1

        # assigning max variable to None
        max = None

        # checking if each element occurred odd number of times and if the element is largest 
        for each_elm in oddHash:
                if oddHash[each_elm] % 2 and each_elm > max:
                        max = each_elm

        # if max is defined that means we have found max number which occurred odd number of times else return None
        if max:
                return max
        else:
                return None
    

#Midterm Question 8 - Nick's Answer


L = [1,2,3,4,10]

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    x=10
    length = len(L)-1
    total = 0
    print(length)
    
    for i in L:
        print(i)
        total += (i * (x**length))
        length -= 1
        print(length)
        print(total)
    return total
    
    
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE    
    def fun(x):
        length = len(L)-1
        total = 0
        for i in L:
            total += (i * (x**length))
            length -= 1
        return total
    
    return fun
    


#Midterm Question 9 - Nick's Answer

L1 = ['a', 'a', 'b']
L2 = ['a', 'b']


L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    list1 = {}
    list2 = {}
    count = 0
        
    for i in L1:
        if i in list1:
            list1[i] += 1
        else:
            list1[i] = 1

    for i in L2:
        if i in list2:
            list2[i] += 1
        else:
            list2[i] = 1
            
    if len(list1)  == 0 and len(list2)==0:
        return(None,None,None)
    
    elif len(list1) == len(list2):
        for i in list1:
            if list1[i]==list2[i]:
                count +=1
            else:
                count = count
        if len(list1) == count:
            v=list(list1.values())
            k=list(list1.keys())
            return(k[v.index(max(v))],max(v),type(k[v.index(max(v))]))
        else:
            return False
    else:
        return False


#Midterm Question 7 - Nick's Answer

d = {1:10, 2:20, 3:30, 4:30} --> {10: [1], 20: [2], 30: [3]}


d = {1:10, 2:20, 3:30, 4:30}

    for i in ikeys:
        inverse[i] = inverse[i].sort()
        
        
    ikeys=list(inverse.keys())
    print(ikeys)

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    inverse = {}
    values = list(d.values())
    keys = list(d.keys())
    
    for v in values:
        inverse[v]= []
    
    for k in keys:
        inverse[d[k]] += [k]
    
    ikeys=list(inverse.keys())

    for i in ikeys:
        inverse[i].sort()
    
    return inverse


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






    
    