#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:49:32 2017

@author: nicholasf
"""


#problem set 2, problem 1
# Define a function that computes the balance after one year of paying minimum payments at a minPayment rate
# and with an annualInterestRate that compounds monthly

def annualBalance(balance,annualInterestRate,monthlyPaymentRate,months):
    monthlyInterestRate = annualInterestRate/12.0
    minPayment= monthlyPaymentRate*balance
    for i in range(0,months):
         balance = balance - minPayment
         balance = balance + monthlyInterestRate*balance
         minPayment = monthlyPaymentRate*balance
    print(round(balance,2))

    
    
#problem set 2, problem 2
# find the minimum balance 
# monthly payment is a multiple of 10 and must be the same for all months


balance = 3329
annualInterestRate = 0.2


def annualBalanceMin(balance,annualInterestRate,months):
    
    monthlyInterestRate = annualInterestRate/12.0
    balanceTemp = balance
    minPayment=0
    
    while True:
        minPayment += 10           
        for i in range(0,months):
            balanceTemp = balanceTemp - minPayment
            balanceTemp = balanceTemp + monthlyInterestRate*balanceTemp
        if balanceTemp <=0:
            break
        else:
            balanceTemp = balance

    print(minPayment)

