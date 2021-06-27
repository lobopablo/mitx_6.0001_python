#%% Script information
# Name: problem2.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
cls = lambda: print("\033[2J\033[;H", end='')
cls()
#%% Delete this before handing in
balance = 999999
annualInterestRate = 0.18

#%% Actual code
intrate = annualInterestRate / 12
monthlypay = 0
finalbalance = balance


while finalbalance>0:
    monthlypay += 10
    for i in range(0,13):
        if i==0:
            balanceval = balance
            ub = balanceval - monthlypay
            interest = intrate*ub
        else:
            balanceval = ub + interest
            ub = balanceval - monthlypay
            interest = intrate*ub
        finalbalance = balanceval
        
print('Lowest Payment:',monthlypay)