#Bubble Sort is a comparison-based algorithm in 
#which each pair of adjacent elements is compared and the elements are swapped if they are not in order.




def BubbleSort(list):

    for i in range(len(list)):

        for j in range(len(list) - i - 1):

            if list[j] > list[j + 1]:

                list[j], list[j+1] = list[j+1], list[j]

    return list



if __name__ == '__main__':

    list = [3,2,6,5,8,4,9]

    print(BubbleSort(list))

