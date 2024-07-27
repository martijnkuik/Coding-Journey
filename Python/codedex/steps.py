import numpy as np

steps = np.array([[4008, 5450, 3468, 4417, 2763, 3151, 4361, 3151]])

print("Minimum steps are!",(np.min(steps)))   
print("Maximum steps are!",(np.max(steps)))      
print("Total steps a week was!",(np.sum(steps)))       
print("Average steps per day were!",round(np.average(steps))) 
