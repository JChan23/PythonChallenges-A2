def binarysearch(array, target):
  low = 0
  high = len(array)-1
  while low <= high:
    mid = (high+low)//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

def insertionSort(alist):
    for i in range(1, len(alist)):
        position = i - 1
        currentvalue = alist[i]
        while position >= 0 and alist[position] > currentvalue: #=0???
            alist[position+1] = alist[position]
            position = position - 1
        alist[position+1] = currentvalue


MyArray = [5, 6, 1, 3, 2, 4]
item = int(input('Enter an item to search for in the array: '))
result = binarysearch(MyArray, item)
if result == -1:
    insertionSort(MyArray)
    result = binarysearch(MyArray, item)
    if result == -1:
        print("Can't find it!")
    else:
        print("Found it at position", result)
else:
  print("Found it at position", result)
