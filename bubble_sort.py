def bubble_sort(element):
    size=len(element)
    for i in range(size-1):
        for j in range(size-1-i):
            if element[j]>element[j+1]:
                temp=element[j]
                element[j]=element[j+1]
                element[j+1]=temp

if __name__== '__main__':
    element=[2,5,8,93,78,6,73,9]
    bubble_sort(element)
    print(element)