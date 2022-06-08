#In Linear Search, a sequential search is made over all items one by one. 
#Every item is checked and if a match is found then that particular item is returned, 
#otherwise the search continues till the end of the data structure.



def LinearSearch(array, element):

    for i in range(len(array)):

        if array[i] == element:
            print("The element is found at index : {}".format(i))
            return i
            
    return -1


if __name__ == '__main__':

    array = [10,6,3,7,4,9,2]

    element = 9

    LinearSearch(array,element)
