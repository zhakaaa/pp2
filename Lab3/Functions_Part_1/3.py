# Calculate number of chicken and rabbits 

numheads = 35
numlegs = 94

def solve(numheads, numlegs) :
    y =  numlegs / 2 - numheads
    x = 35 - y 
    answer = "Chicken: {}\nRabbits: {}"
    print(answer.format(int(x),int(y)))
    
solve(numheads, numlegs)