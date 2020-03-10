import random
from matplotlib import pyplot as plt
import numpy as np

"""
The objective of this exercise was to write a script containing 
2 functions to simulate genetic drift and the plot the results.

Task 1: the first part of the script models genetic drift where 
each individual has one copy of a gene with two possible alleles, 
'A' or 'B'. 
"""

#arguments for the function: population size, max. no of generations
#def task1(pop_size, generations)
#return plot.show()

# generate population and initate variables
pop_array1 = ["A", "B"] * 50

A_drift = []
B_drift = []


#loop to iterate once per generation
for i in range(0,1000):

	# a random selection(with replacement) of 100 alleles taken 
	# from the previous generation to create the new generation
	pop_array1 = random.choices((pop_array1), k=100)

	#frequencey of each allele counted
	A_freq = pop_array1.count("A")
	B_freq = pop_array1.count("B")

	#allele frequencey of current generation is added to the list
	A_drift.append(A_freq)
	B_drift.append(B_freq)

	#if either allele is lost, no further generations are completed
	if "A" not in pop_array1 or "B" not in pop_array1:
		break
	
# After the generations have been completed, the drift for each allele
# is plotted against generations.
plt.plot(A_drift, label = "Allele A")
plt.plot(B_drift, label = "Allele B")
plt.xlabel("Generations")
plt.ylabel("Allele frequencey")
plt.title("Allele drift in population of 100 individuals")

plt.legend()
plt.show()


"""
Task 2: the second part of the script models genetic drift where
each individual has two copies of a gene with two possible alleles, 
"A" or "a".
"""

#generate population and initiate vairables
pop_array2 = np.array([["A","A"],["A","a"],["A","a"],["a","a"]]*25)

AA_drift = []
Aa_drift = []
aa_drift = []


#loop to iterate once per generation. 
for i in range(0,500):
    next_gen = []
    pop_size = 0
    
    AA = 0
    Aa = 0
    aa = 0
    aa_count = 0
    
    """
    A while loop is used to restrain popultation size to 100.
    'random.sample' generates two different random numbers which
    represent two different individuals in the population.     
    """

    # while loop to restrain population size to 100
    while pop_size < 100:
        
        #randomly choose (without replacement) which parents the alleles come from
        parent_1, parent_2 = random.sample(range(0,100), k=2)
        
        #randomly choose which allele to choose from each parent
        allele_1 = random.randint(0,1)
        allele_2 = random.randint(0,1)
        
        #use random numbers to find alleles from pop_array2 and generate offspring
        offspring = pop_array2[parent_1, allele_1], pop_array2[parent_2, allele_2]
        
        #keep track of allele frequences
        if offspring == ('A','A'):
            AA +=1
            pop_size +=1
        elif offspring ==('A','a') or offspring == ('a','A'):
            Aa += 1
            pop_size +=1
        elif offspring == ('a','a'):
            aa_count += 1
            if aa_count % 5 != 0:
                aa +=1
                pop_size +=1
            
        #add that offspring to the generation
        next_gen.append(offspring)

  	#if the 'a' allele is lost, no further generations are completed.
    if AA == 100:
        break
        
    pop_array2 = np.array(next_gen)
    
    AA_drift.append(AA)
    Aa_drift.append(Aa)
    aa_drift.append(aa)

        

plt.plot(AA_drift, label = "Genotype AA")
plt.plot(Aa_drift, label = "Genotype Aa")
plt.plot(aa_drift, label = "Genotype aa")
plt.xlabel("Generations")
plt.ylabel("Drift")
plt.title("Genotype drift in population of 100 individuals")

plt.legend()

plt.show()