###Yaxin
import math
def benefit(socLevel):
	return 10*math.log(socLevel+1)

def cost(socLevel):
	return 2*socLevel

def profit(socLevel):
	return benefit(socLevel)-cost(socLevel)
	
import numpy as np	
import matplotlib.pyplot as plt

socLevelRange = np.array(range(0,21))

b = map(benefit, socLevelRange)
c = map(cost, socLevelRange)
p = map(profit, socLevelRange)

print b
print c
print p

plt.plot(socLevelRange,b)
plt.plot(socLevelRange,c)
plt.plot(socLevelRange,p)
plt.legend(['benefit','cost','profit'],loc='upper left')
plt.show()





