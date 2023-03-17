def binarySearch_1(list_in, value, offset=0):
    # FILL IN HERE
    mid = int(len(list_in)/2+0.4)
    left = list_in[0:mid]
    right = list_in[mid+1:len(list_in)]
    if mid > len(list_in)-1:
        return -1
    if list_in[mid] == value:
        return offset+mid
    elif list_in[mid] > value:
        return binarySearch_1(left, value, offset)
    else:
        return binarySearch_1(right, value, offset+mid+1)

def binarySearch_2(list_in, value, offset, length):
    # FILL IN HERE
    if length == 0:
        return -1
    mid = int(length/2+0.4)
    if list_in[offset+mid] == value:
        return offset+mid
    elif list_in[offset+mid] > value:
        return binarySearch_2(list_in, value, offset, mid)
    else:
        return binarySearch_2(list_in, value, offset+mid+1, length-mid-1)