import numpy as np


size = 100
tosses = np.random.choice (["H", "T"], size=size )
#print (F"{size} Coin Tosses: {tosses}")

print ("Number of Heads:", np.count_nonzero(tosses == "H"))
print ("Number of Tails:", np.count_nonzero(tosses == "T"))