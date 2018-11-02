def ExamSort(array,n):
    mergeSort(array)
    
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            array[k] = left[i]
            i+=1
            k+=1
        
        while j < len(right):
            array[k] = right[j]
            j+=1
            k+=1
            
array = [15, 9, 60, 44, 12, 1, 4]
n = len(array)
ExamSort(array, n)
print(array)