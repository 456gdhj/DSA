def linear_search(list_num,number):
    for index,element in enumerate(list_num):
        if element==number:
            return index
    return -1

def binary_search(list_num,number):
    left_index=0
    mid_index=0
    right_index=len(list_num)-1
    
    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=list_num[mid_index]

        if mid_number==number:
            return mid_index
        if mid_number>number:
            right_index=mid_index-1
        else:
            left_index=mid_index+1    
    return -1


if __name__== '__main__':
    list_num=[1,3,5,7,9,23,56,78,90]
    number=3
    index=binary_search(list_num,number)
    print(f"i find the number in index {index}")