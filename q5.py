import argparse
import random

# create initial population 
# selection -> new population
# crossover 
# mutation 
# final fitness score 


population_size = 0






def create_init_population(entries, w_max):

    global population_size

    population = []

    n = len(entries)

    if (((n // 2)%2) == 0):
        population_size = n//2
    else:
        population_size = (n//2) + 1

    for i in range(population_size):

        temp = []

        for j in range(n):

            cur_val = random.randint(0,1)
            temp.append(cur_val)

        temp_sample = Sample(temp,entries,w_max)

        population.append(temp_sample)


    return population




class Solver:

    def __init__(self,entries, w_max, iterations):

        self.w_max = w_max
        self.entries = entries
        self.iterations = iterations
        self.init_pop = create_init_population(entries, w_max)
        self.init_score = self.pop_fitness(self.init_pop)
        self.current_pop = self.init_pop
        
        self.final_score = self.train()



    def print_pop(self, pop):

        n = len(pop)

        for i in range(n):
            print(pop[i].values, pop[i].fs, "\n")

        print("\n")
        


    def train(self):

        self.print_pop(self.current_pop)

        for i in range(self.iterations):

            self.selection()
            # self.print_pop(self.current_pop)
            self.crossover()
            # self.print_pop(self.current_pop)

            self.mutation()
            # self.print_pop(self.current_pop)

        self.print_pop(self.current_pop)

        final_fitness = self.pop_fitness(self.current_pop)

        return final_fitness

    


    def selection(self):

        # returns a selection of the population removing the sample with the least fitness score

        # sort the current population with fitness scores in reverse
        # remove the last and append the first  

        temp_sorted = sorted(self.current_pop, key = lambda x : x.fs, reverse = True)

        # print(len(temp_sorted))

        temp_sorted.pop()

        temp_sorted.append(temp_sorted[0])

        self.current_pop = temp_sorted


    def unit_crossover(self,unit):

        a = unit[0]
        b = unit[1]

        n = len(a.values)

        temp_a_val = []
        temp_b_val = []

        split = random.randint(0,n-2)

        # print(split, " hello")

        for i in range(n):

            if i <= split:
                temp_a_val.append(a.values[i])
                temp_b_val.append(b.values[i])
            else:
                temp_a_val.append(b.values[i])
                temp_b_val.append(a.values[i])

        # print(a.values, " ", temp_a_val)
        # print(b.values, " ", temp_b_val)

        new_a = Sample(temp_a_val, self.entries, self.w_max)
        new_b = Sample(temp_b_val, self.entries, self.w_max)

        return (new_a,new_b)


    def crossover(self):

        temp_pop = []

        n = len(self.current_pop)

        for i in range(n-1):

            if (i%2 != 0):
                continue

            sen_tup = (self.current_pop[i],self.current_pop[i+1])
            ret_tup = self.unit_crossover(sen_tup)

            temp_pop.append(ret_tup[0])
            temp_pop.append(ret_tup[1])

        
        self.current_pop = temp_pop


    def mutation(self):

        n = len(self.current_pop)

        temp_pop = []

        for i in range(n):

            if (i%2==0):

                val = random.randint(0,n-1)
                temp_lis = self.current_pop[i].values
                
                current_bit = temp_lis[val]

                if current_bit:
                    temp_lis[val] = 0
                else:
                    temp_lis[val] = 1
                
                temp_samp = Sample(temp_lis, self.entries, self.w_max)

                temp_pop.append(temp_samp)

            else:
                temp_pop.append(self.current_pop[i])


        self.current_pop = temp_pop

    
    def pop_fitness(self, pop):

        score = 0

        for s in pop:

            score = score + s.fs

        
        return score










class Sample():

    def __init__(self, values, entries, w_max):

        self.entries = entries
        self.w_max = w_max
        self.values = values
        self.fs = self.calculate_fs()


    def calculate_fs(self):

        weight = 0
        penalty = 0
        score = 0

        for i,val in enumerate(self.values):

            if val:

                weight = weight + self.entries[i][1]
                score = score + self.entries[i][2]
            else:
                penalty = penalty + self.entries[i][3]

        if weight > self.w_max:
            score = score - (weight - self.w_max)

        score = score + penalty   #as penalty is in negative

        return score
        
        


if __name__ == "__main__":

    #parse input 
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_items', type=int, required= True)
    parser.add_argument("--w_max", type = int, required= True)
    parser.add_argument("--iter", type = int, default= 10000)
    args = parser.parse_args()
    n_items = int(args.n_items)
    w_max = int(args.w_max)
    iterations = int(args.iter)

    entries = []

    for i in range(n_items):

        temp = input("Enter the table entry\n").split()
        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])

        # print(temp)

        entries.append(temp)

    solve = Solver(entries,w_max,iterations)

 

    print("Initial Score:", solve.init_score)

    print("Final Score:", solve.final_score)


    

    


        














