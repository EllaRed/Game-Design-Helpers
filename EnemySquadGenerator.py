import random 
import itertools

# Say you want to make a hundred levels of a game
# and you have a bunch of unique (or generic) AI monsters 
#you want in a pool  to be instantiated per level
#This little algo will print out a list of AI monsters (stored as strings)
#paired with a number that will serve as the number of instances for that level

#this list is the min and max numbers you want for a total number of instances
numbers  = [1,2,3,4,5,6,7,8,9]

#this function handles the grouping of random elements in a list, lenght being the
#size of the group
#you can set it to 2 to always get a pair

def random_pairs(arg_list,length):
    pairs= random.sample((arg_list), length)
    return pairs
    
#heres where  you set how many levels you want to make pairs for 
n = 70
count=0
#heres the string list of monsters
mons_list=["goblin","slime","apple","worm"]

#this loop prints out a monster with its instance number
while count <n:
    length=random.randint(2,4)
    pairs=random_pairs(numbers,length)
    #this if statement checks if the elements in number group are 
    #equal to 10 because I want the total number of AI in a level to
    #always be ten. You can change this number to the size of your own level pool
    if sum(pairs)==10:
        # so if the total number of instances is not 10,
        #the loop runs again without moving forward
        count+=1
        mons=(random_pairs(mons_list,length))
        print(count)
        for i in range(len(pairs)):
            print ( "@"+str(mons[i]) +"-"+str(pairs[i]))
			
			
