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

MyArray = [1, 2, 3, 4, 5, 6]
item = int(input('Enter an item to search for in the array: '))
result = binarysearch(MyArray, item)
if result == -1:
  print("Can't Find it!")
else:
  print("Found it at position", result)
