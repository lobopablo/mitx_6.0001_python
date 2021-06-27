#%% Script information
# Name: problem1.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
#%% Delete this before handing in
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#%% Actual code
intrate = annualInterestRate / 12

mp = balance * monthlyPaymentRate
ub = balance - mp
interest = intrate*ub

for i in range(1,13):
    balance = ub + interest
    # print('Month',i,'Remaining balance: ',balance)  
    mp = balance * monthlyPaymentRate
    ub = balance - mp
    interest = intrate*ub
print('Remaining balance:',round(balance,2))