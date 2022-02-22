# Genetic-algorithm-knapsack-with-penalty
This repository attempts to solve the knapsack problem using Genetic algorithm. It is a 0-1 knapsack and there is an added penalty of not taking specific items. <br>


Let’s say, you are going to spend a month in the wilderness. Only thing you are carrying is the
backpack which can hold a maximum weight of 40 kg. Now you have different survival items, each
having its own “Survival Points” (which are given for each item in the table). Some of the items are so
essential that if you do not take them, you incur some additional penalty.




| Item  | Weight | Value | Penalty if not taken |
| :------------ |:---------------:| -----:| -----:|
| Sleeping Bag     | 30 | 20 | 0 |
| Rope      | 10       |   10 | 0|
| Bottle | 5        |    20 | 0 |
| Torch | 15       |    25 | -20 |
| Glucose | 5        |    30 | 0 |
| Knife | 10        |    15 | -10 |
| Umbrella | 20       |    10 | 0 |


Formulate this as a genetic algorithm problem where your objective is to maximise the survival points.
Write how you would represent the chromosomes, fitness function, crossover, mutation etc. And then
write a python program to find the solution of this problem using GA. The program should have the
capability to handle a different number of items with different values than what is given in the table.
