import numpy as np

# Create the array with the provided data
passengers = np.array([
    [1, 0, 3, 22],
    [2, 1, 1, 38],
    [3, 1, 3, 26],
    [4, 1, 1, 35],
    [5, 0, 3, 35],
    [6, 0, 3, 18],
    [7, 0, 1, 54],
    [8, 0, 3, 2],
    [9, 1, 3, 27],
    [10, 1, 2, 14],
    [11, 1, 3, 4],
    [12, 1, 1, 58],
    [13, 0, 3, 20],
    [14, 0, 3, 39],
    [15, 0, 3, 14],
    [16, 1, 2, 55],
    [17, 0, 3, 2],
    [18, 1, 2, 12],
    [19, 0, 3, 31],
    [20, 1, 3, 8],
    [21, 0, 2, 35],
    [22, 1, 2, 34],
    [23, 1, 3, 15],
    [24, 1, 1, 28],
    [25, 0, 3, 8],
    [26, 1, 3, 38],
    [27, 0, 3, 2],
    [28, 0, 1, 1],
    [29, 1, 3, 5],
    [30, 0, 3, 18],
    [31, 0, 1, 40],
    [32, 1, 1, 70],
    [33, 1, 3, 33],
    [34, 0, 2, 66],
    [35, 0, 1, 28],
    [36, 0, 1, 42],
    [37, 1, 3, 5],
    [38, 0, 3, 18],
    [39, 0, 3, 18],
    [40, 1, 3, 14],
    [41, 0, 3, 40],
    [42, 0, 2, 27],
    [43, 0, 3, 29],
    [44, 1, 2, 0],
    [45, 1, 3, 19],
    [46, 0, 3, 33],
    [47, 0, 3, 14],
    [48, 1, 3, 22],
    [49, 0, 3, 41],
    [50, 0, 3, 18]
])

# 1. Shape of the array
shape = passengers.shape
print("The shape of the array is:", shape)

# 2. Average age of the passengers
ages = passengers[:, 3]
average_age = np.mean(ages)
print("The average age of the passengers is:", average_age)

# 3. Passenger number of the oldest and youngest passengers
oldest_passenger_index = np.argmax(ages)
youngest_passenger_index = np.argmin(ages)

oldest_passenger_number = passengers[oldest_passenger_index, 0]
youngest_passenger_number = passengers[youngest_passenger_index, 0]

print("The passenger number of the oldest passenger is:", oldest_passenger_number)
print("The passenger number of the youngest passenger is:", youngest_passenger_number)

# 4. Percentage of passengers that survived
survived = passengers[:, 1]
percentage_survived = np.mean(survived) * 100
print("The percentage of passengers that survived is:", percentage_survived)

# 5. Percentage of passengers that survived based on passenger class
classes = np.unique(passengers[:, 2])
for cls in classes:
    class_passengers = passengers[passengers[:, 2] == cls]
    class_survival_rate = np.mean(class_passengers[:, 1]) * 100
    print(f"The survival rate for class {cls} is: {class_survival_rate:.2f}%")
