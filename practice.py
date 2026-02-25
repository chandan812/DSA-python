def reverse_array(arr):
    left,right = 0, len(arr)-1

    while left<right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    return arr

arr=[1,2,3,4,5,6,7,8,9]
print(reverse_array(arr))