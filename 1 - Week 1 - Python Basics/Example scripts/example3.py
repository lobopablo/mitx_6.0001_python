#%% Script information
# Name: example3.py
# Author: Pablo Lobo, plobo@itba.edu.ar
#
#%% Script description
#
#%% Clear Console
# cls = lambda: print("\033[2J\033[;H", end='')
# cls()
#%%
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break