# # 1.0 Reverse a string
# def reverse_string(a_string):
#        return a_string[::-1]
# test = reverse_string("tammy")
# print(test)

# Duplicate in a list
# def duplicates(numberlist):
#     result = []
#     numberlist.sort()
#     for i in range(1,len(numberlist)):
#         if numberlist[i] == numberlist[i-1]:
#             result.append(numberlist[i])
#     return result
# mylist = duplicates([2,4,6,4,3,7,5,6,8,7,4])
# # Unique Values
# list = set(mylist)
# print(list)


# def flip_vertical_axis(matrix):    
#     r = len(matrix) - 1
#     c = len(matrix[0]) - 1
#     temp = 0
#     i = 0
#     while i <= r:
#         j = 0
#         while j <= (c/2):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[i][c - j]     
#             matrix[i][c - j] = temp        
#             j = j + 1
#         i = i + 1
        
#     return matrix
# x = [[1,0]]
# s =flip_vertical_axis([[1,2]])

# # print(s)
# g =flip_vertical_axis([[2,4,7,9],[5,6,8,10]])
# print(g)
def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) +fib(n-2)

print(fib(6))