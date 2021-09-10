# Step 1 take in user input as str1 split it separate it's numbers

str1 = input().split(' ')

# Step 2 initialize the perfect set to later compare it with the input set

perfectSet = [1, 1, 2, 2, 2, 8]
i = 0

# Step 3 create empty list to store the difference between perfect set and input set
correction = []

# Step 4 subtract the indexes of perfect set from the same index of the input set and add to the empty list
while i < len(perfectSet):
    a = int(perfectSet[i]) - int(str1[i])
    correction.append(a)
    i = i + 1
# Step 5 print the list on one line
print(*correction)
