#Merge sort first divides the array into equal halves and then combines them in a sorted manner.



def MergeSort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)


        i = j = k = 0

        while i < len(L) and j < len(R):

            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


    return arr



if __name__ == '__main__':

    arr = [12,11,14,5,7,6]

    print("Given array is", arr)
    print("The Sorted array",MergeSort(arr))
