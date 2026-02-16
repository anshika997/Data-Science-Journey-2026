import matplotlib.pyplot as plt 
# years = [1990 , 1992 , 1994 , 1996 , 1998 , 2000 , 2003 , 2005 , 2007 , 2010]
# runs = [500 , 700 , 1100 , 1500 , 1800 , 1200 , 1700 , 1300 ,900 ,1500] 
# plt.plot(years,runs)
# plt.xlabel(" Years ")
# plt.ylabel(" Runs Scored ")
# plt.title(" Sachin Tendulkar’s Runs Over Time ")
# plt.show()
import numpy as np 
for i in range(50):
    plt.plot(np.random.rand(100),linewidth=3)
plt.title("too much data can confusing")
plt.grid(True)
plt.tight_layout()
plt.show()