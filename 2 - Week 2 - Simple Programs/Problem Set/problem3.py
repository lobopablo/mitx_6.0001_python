#%% Script information
# Name: problem3.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
#%% Delete this before handing in
balance = 999999
annualInterestRate = 0.18

#%% Actual code
intrate = annualInterestRate / 12
finalbalance = balance

highguess = (balance * (1+intrate)**12)/12
lowguess = balance / 12
monthlypay = (highguess + lowguess)/2
totalpay = monthlypay*12
diff = abs(finalbalance - totalpay)

while diff>0.12:
    for i in range(0,13):
        if i==0:
            balanceval = balance
            ub = balanceval - monthlypay
            interest = intrate*ub
        else:
            balanceval = ub + interest
            ub = balanceval - monthlypay
            interest = intrate*ub

    if balanceval > 0.12:
        lowguess = monthlypay
        monthlypay = (highguess + lowguess)/2
        balanceval = balance
    elif balanceval < -0.12:
        highguess = monthlypay
        monthlypay = (highguess + lowguess)/2
        balanceval = balance
    else: 
        break
        
print('Lowest Payment:',round(monthlypay,2))