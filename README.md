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



To run the program follow the below instructions:


1. Command to run the program is : python q5.py < try.txt --n_items 7 --w_max 40 --iter 10000 <br>
2. Here the program takes input from the file try.txt
3. This file contains n_items lines entries. These represent the entries of the tables. 
4. We can change the parameters n_items and w_max, correspondingly change the no of entries in the file try.txt
5. The default iterations are 10000.
6. The arguments --n_items and --w_max are required while --iter is not mandatory to give as command line input. 
7. The output is Initial population with score of each sample along with it and the final population with each sample score.
8. We also output the initial population score and the final population score. 
