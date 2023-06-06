#1.6
def sum_two_number(num_1, num_2):
    total = num_1 + num_2
    print(total)
    return total

def substract_two_number(num_1, num_2):
    substract = num_1 - num_2
    print(substract)
    return substract

#1.7
def print_array(arr):
    print("All elements in the array:", end = " ")
    for elem in arr:
        print(elem, end = ' ')

#1.8
def print_max(arr):
    maximum = arr[0]
    for elem in arr:
        if elem > arr:
            maximum = elem
    print(maximum)
    
#1.9
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    return arr
    