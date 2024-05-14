import random

def foo(x,y,z):
    return 6*x** 3 + 9*y** 2 + 90 * z -25


def fitness(x,y,z):
    ans = foo(x,y,z)
    
    if ans == 0:
        return 9999
    else:
        return abs(1/ans)

solution= []
for s in range(1000):
    solution.append((random.uniform(0,10000), 
                    random.uniform(0,10000),
                    random.uniform(0,10000)))

for i in range(10000):
    
    rankedsolution = []
    for s in solution:
        rankedsolution.append((fitness(s[0], s[1], s[2]),s))
    rankedsolution.sort()
    rankedsolution.reverse()
    
    print(f"== Genn {i} best solution ===")
    if rankedsolution[0][0] > 999:
        break
    print(rankedsolution[0])
    
    bestsolution  = rankedsolution[:100]
    
    elements = []
    
    for s in bestsolution:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
    newGen = []
    for s in range(1000):
        es1 = random.choice(elements) * random.uniform(0.99, 1.01)
        es2 = random.choice(elements) * random.uniform(0.99, 1.01)
        es3 = random.choice(elements) * random.uniform(0.99, 1.01)
        
        newGen.append((es1, es2, es3))
        
    solution = newGen
    
