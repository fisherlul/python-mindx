arr = [-1, 2, -3, 4, 5, -6, -8]
def quick_sort(arr: list):
    # for i in range(len(arr)):
    #     for j in range(len(arr)-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    # return arr
    j = len(arr) - 1
    i = 0
    while i != j:
        if arr[i] > arr[j] and arr[i] > 0:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[i] <=  0:
            i += 1
        else:
            j -= 1
            

    return arr        
print(quick_sort(arr))
            