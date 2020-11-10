import math
import collections

arr = [56, 98, 1, 4, 10, 67, 5, 6, 100, 167]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

x = 5
r = -1

a = 0
b = len(arr) - 1

while a <= b:
    v = a + (b - a) // 2
    if arr[v] == x:
        r = v
        break
    elif arr[v] < x:
        a = v + 1
    else:
        b = v - 1
    
if r != -1:
    print(f"Element is available at: {r}")
else:
    print("Element is not available")


arr = [56, 98, 1, 4, 10, 67, 5, 6, 100, 167]

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] < arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

x = 1
r = -1

a = 0
b = len(arr) - 1

while a <= b:
    v = a + (b - a) // 2
    if arr[v] == x:
        r = v
        break
    elif arr[v] > x:
        a = v + 1
    else:
        b = v - 1
    
if r != -1:
    print(f"Element is available at: {r}")
else:
    print("Element is not available")
 
 # 2

array = [56, 98, 1, 4, 10, 67, 5, 6, 100, 167]

for iteration in range(2):
    for index in range(len(array) - 1):
        for current_index in range(len(array) - index - 1):
            if (iteration == 0 and array[current_index] > array[current_index + 1]) or (iteration == 1 and array[current_index] < array[current_index + 1]):
                temporary_variable = array[current_index]
                array[current_index] = array[current_index+1]
                array[current_index+1] = temporary_variable
        r = -1
    if iteration == 0:
        contant_variable = 5
    elif iteration == 1:
        contant_variable = 1
    a = 0
    b = len(array) - 1
    while a <= b:
        v = a + (b - a) // 2
        if array[v] == contant_variable:
            r = v
            break
        elif array[v] < contant_variable and iteration == 0:
            a = v + 1
        elif array[v] > contant_variable and iteration == 1:
            a = v + 1
        else:
            b = v - 1
    if r != -1:
        print(f"Element is available at: {r}")
    else:
        print("Element is not available")

