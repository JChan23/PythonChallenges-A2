def binarysearch(array, low, high, target):
  while low <= high:
    mid = (high+low)//2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      return binarysearch(array, mid + 1, high, target)
    else:
      return binarysearch(array, low, mid - 1, target)

  return -1

MyArray = [1, 2, 3, 4, 5, 6]
low_index = 0
high_index = len(MyArray)-1
item = int(input('Enter an item to search for in the array: '))
result = binarysearch(MyArray, low_index, high_index, item)
if result == -1:
  print("Can't Find it!")
else:
  print("Found it at position", result)

