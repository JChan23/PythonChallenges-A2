nums = [5, 73, 4, 29, 82, 17, 95, 38, 62, 41, 56, 87, 14, 39, 48, 67, 23, 91, 10, 75, 53, 88, 31, 27, 63, 94, 52, 18, 71, 5, 84, 26, 33, 76, 45, 92, 19, 68, 9, 54, 80, 12, 60, 21, 49, 72, 97, 11, 42, 85, 16, 6, 28, 77, 69, 13, 50, 40, 70, 57, 22, 64, 83, 3, 57, 99, 8, 25, 32, 51, 65, 86, 43, 30, 100, 46, 90, 66, 2, 58, 20, 93, 7, 79, 24, 81, 47, 59, 15, 98, 44, 26, 18]

def insertionSort(alist):
    for i in range(1, len(alist)):
        position = i - 1
        currentvalue = alist[i]
        while position >= 0 and alist[position] > currentvalue: #=0???
            alist[position+1] = alist[position]
            position = position - 1
        alist[position+1] = currentvalue
    print(alist)

insertionSort(nums)
