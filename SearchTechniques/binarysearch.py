#Binary search follows a divide and conquer methodology. 
#It is faster than linear search but requires that the array be sorted before the algorithm is executed.




def BinarySearch(array, element):

    min = 0
    max = len(array) - 1

    index = -1
    while min <= max and (index == -1):
        
        mid = (min + max) // 2

        if array[mid] == element:
            index = mid

        else:

            if element < array[mid]:
                max = mid - 1

            else:
                min = mid + 1
    

    if index == -1:
        print("Element NOT found in the array")
    
    else:
        print("Element found at index : {}".format(index))

    return index



if __name__ == '__main__':


    array = [10,20,30,40,50]
    element = 20

    BinarySearch(array, element)
            