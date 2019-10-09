s = [3, 1, 0, 2, 4]

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
     
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        #find smallest elemnt to the right of index 0

        for j in range (i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        #swap this element with index[0]

        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

        print(f"sssss {arr}")

        # TO-DO: swap
    
    return arr

selection_sort(s)
print(f"s{s}")


# TO-DO:  implement the Bubble Sort function below
# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.


# g = [3, 1, 0, 2, 4]

# def bubble_sort( arr ):

#     for i in range(0, len(arr) - 1):
#         temp = arr[i]
#         j = i + 1
#         if arr[j] < arr[i]:
#             arr[i] = arr[j]
#             arr[j] = temp
        
#         print(f"gggggggg {arr}")

#     return arr

# bubble_sort(g)
# print(f"g {g}")


b = [3, 1, 0, 2, 4] 

def bubble_sortYO(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"bbbbbbb {arr}")

    return arr


bubble_sortYO(b)
print(f"b {b}")


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr




# def bubble_sort( arr ):
#     has_swapped = True
#     counter = 0
#     while has_swapped:
#         has_swapped = False
#         for i in range(len(arr) - 1):
#             counter += 1
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 has_swapped = True
#     print(counter)
#     return arr


