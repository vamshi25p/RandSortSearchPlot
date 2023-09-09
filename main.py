import random
import time
import psutil
import os
import sys
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
start_time = time.time()
print("GENERATION OF ELEMENTS")
number1=list(range(1,1001))
print(number1)
random_items1=random.sample(number1,1000)
print(random_items1)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number2=list(range(1000,2001))
print(number2)
random_items2=random.sample(number2,1000)
print(random_items2)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number3=list(range(2000,3001))
print(number3)
random_items3=random.sample(number3,1000)
print(random_items3)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number4=list(range(3000,4001))
print(number4)
random_items4=random.sample(number4,1000)
print(random_items4)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number5=list(range(4000,5001))
print(number5)
random_items5=random.sample(number5,1000)
print(random_items5)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number6=list(range(5000,6001))
print(number6)
random_items6=random.sample(number6,1000)
print(random_items6)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number7=list(range(6000,7001))
print(number7)
random_items7=random.sample(number7,1000)
print(random_items7)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number8=list(range(7000,8001))
print(number8)
random_items8=random.sample(number8,1000)
print(random_items8)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number9=list(range(8000,9001))
print(number9)
random_items9=random.sample(number9,1000)
print(random_items9)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("---------------------------")
number10=list(range(9000,10001))
print(number10)
random_items10=random.sample(number10,1000)
print(random_items10)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)


start_time = time.time()
print("*************************************************************")
print("COMBINING OF ELEMENTS")
#set1 denotes set of 1-1000 random numbers
#set2 denotes set of 1-2000 random numbers and so on
set1=list(random_items1)
print(set1)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set2=list(random_items1 + random_items2)
print(set2)
list2=random.sample(set2,2000)
print(list2)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set3=list(random_items1 + random_items2 + random_items3)
print(set3)
list3=random.sample(set3,3000)
print(list3)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set4=list(random_items1 + random_items2 + random_items3 + random_items4)
print(set4)
list4=random.sample(set4,4000)
print(list4)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set5=list(random_items1 + random_items2 + random_items3 + random_items4 + random_items5)
print(set5)
list5=random.sample(set5,5000)
print(list5)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set6=list(random_items1 + random_items2 + random_items3 + random_items4 + random_items5 + random_items6)
print(set6)
list6=random.sample(set6,6000)
print(list6)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set7=list(random_items1 + random_items2 + random_items3 + random_items4 + random_items5 + random_items6 + random_items7)
print(set7)
list7=random.sample(set7,7000)
print(list7)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set8=list(random_items1 + random_items2 + random_items3 + random_items4 + random_items5 + random_items6 + random_items7 + random_items8)
print(set8)
list8=random.sample(set8,8000)
print(list8)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set9=list(random_items1 + random_items2 + random_items3 + random_items4 + random_items5 + random_items6 + random_items7 + random_items8 + random_items9)
print(set9)
list9=random.sample(set9,9000)
print(list9)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("-----------------------------------------")
set10=list(random_items1 + random_items2 + random_items3 + random_items4 + random_items5 + random_items6 + random_items7 + random_items8 + random_items9 + random_items10)
print(set10)
list10=random.sample(set10,10000)
print(list10)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
print("********************************************************************")
print("SORTING OF ELEMENTS")
# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

start_time = time.time()
process = psutil.Process(os.getpid())
memory_start = process.memory_info().vms
print("------------------------------------------")
print("Unsorted Array 1")
print(set1)
quickSort(set1, 0, 999)
print('Sorted Array in Ascending Order:')
print(set1)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 2")
print(list2)
quickSort(list2, 0, 1999)
print('Sorted Array in Ascending Order:')
print(list2)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 3")
print(list3)
quickSort(list3, 0, 2999)
print('Sorted Array in Ascending Order:')
print(list3)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 4")
print(list4)
quickSort(list4, 0, 3999)
print('Sorted Array in Ascending Order:')
print(list4)
end_time = time.time()
total_time = end_time - start_time
start_time = time.time()
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 5")
print(list5)
quickSort(list5, 0, 4999)
print('Sorted Array in Ascending Order:')
print(list5)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 6")
print(list6)
quickSort(list6, 0, 5999)
print('Sorted Array in Ascending Order:')
print(list6)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 7")
print(list7)
quickSort(list7, 0, 6999)
print('Sorted Array in Ascending Order:')
print(list7)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 8")
print(list8)
quickSort(list8, 0, 7999)
print('Sorted Array in Ascending Order:')
print(list8)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 9")
print(list9)
quickSort(list9, 0, 8999)
print('Sorted Array in Ascending Order:')
print(list9)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
start_time = time.time()
print("------------------------------------------")
print("Unsorted Array 10")
print(list10)
quickSort(list10, 0, 9999)
print('Sorted Array in Ascending Order:')
print(list10)
end_time = time.time()
total_time = end_time - start_time
print("Total Execution time:", total_time)
memory_end = process.memory_info().vms
memory_used = memory_end - memory_start
print("Memory used:", memory_used, "bytes")

print("************************************************************************")
print("************************************************************************")

print("BINARY SEARCH BEGINS")
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

# Example usage:

def binary_size(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    size = sys.getsizeof(arr) + sys.getsizeof(low) + sys.getsizeof(high) + sys.getsizeof(mid)
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # x is present at mid
        else:
            return size
print("BINARY SEARCH FOR 1-1000 ELEMENTS")
ts1 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(set1, x)
size1 = binary_size(set1,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te1 = time.time()
t1 = te1 - ts1
print("Total Execution time:", t1)
print("Space complexity:",size1,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-2000 ELEMENTS")
ts2 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list2, x)
size2 = binary_size(list2,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te2 = time.time()
t2 = te2 - ts2
print("Total Execution time:", t2)
print("Space complexity:",size2,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-3000 ELEMENTS")
ts3 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list3, x)
size3 = binary_size(list3,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te3 = time.time()
t3 = te3 - ts3
print("Total Execution time:", t3)
print("Space complexity:",size3,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-4000 ELEMENTS")
ts4 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list4, x)
size4 = binary_size(list4,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te4 = time.time()
t4 = te4 - ts4
print("Total Execution time:", t4)
print("Space complexity:",size4,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-5000 ELEMENTS")
ts5 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list5, x)
size5 = binary_size(list5,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te5 = time.time()
t5 = te5 - ts5
print("Total Execution time:", t5)
print("Space complexity:",size5,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-6000 ELEMENTS")
ts6 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list6, x)
size6 = binary_size(list6,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te6 = time.time()
t6 = te6 - ts6
print("Total Execution time:", t6)
print("Space complexity:",size6,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-7000 ELEMENTS")
ts7 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list7, x)
size7 = binary_size(list7,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te7 = time.time()
t7 = te7 - ts7
print("Total Execution time:", t7)
print("Space complexity:",size7,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-8000 ELEMENTS")
ts8 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list8, x)
size8 = binary_size(list8,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te8 = time.time()
t8 = te8 - ts8
print("Total Execution time:", t8)
print("Space complexity:",size8,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-9000 ELEMENTS")
ts9 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list9, x)
size9 = binary_size(list9,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te9 = time.time()
t9 = te9 - ts9
print("Total Execution time:", t9)
print("Space complexity:",size9,"bytes")
print("********************************************************")
print("BINARY SEARCH FOR 1-10000 ELEMENTS")
ts10 = time.time()
x=int(input("Enter the element to be searched:"))
result = binary_search(list10, x)
size10 = binary_size(list10,x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in given sequence")
te10 = time.time()
t10 = te10 - ts10
print("Total Execution time:", t10)
print("Space complexity:",size10,"bytes")
print("********************************************************")

# create the GUI window
root = tk.Tk()
root.title("Binary Search For 10000 Elements")

# sample data
x = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
y = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10]

# create the plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.xlabel('RANGE OF ELEMENTS')
plt.ylabel('TIME COMPLEXITY')

# add the plot to the GUI window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# run the GUI event loop
root.mainloop()



print("***********************************************************************")
print("***********************************************************************")
print("***********************************************************************")








