# PALB-python-Programming
arr = [10,5,12,45,91]

min = arr[0]
max = arr[0]

for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

print("Minimum element:", min)
print("Maximum element:", max)
