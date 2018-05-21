# # 1.0 Reverse a string
# def reverse_string(a_string):
#        return a_string[::-1]
# test = reverse_string("tammy")
# print(test)

# Duplicate in a list
def duplicates(numberlist):
    result = []
    numberlist.sort()
    for i in range(1,len(numberlist)):
        if numberlist[i] == numberlist[i-1]:
            result.append(numberlist[i])
    return result


mylist = duplicates([2,4,6,4,3,7,5,6,8,7,4])
list = set(mylist)
print(list)





# def dupi_items(numbers):
#     result = []
#     numbers.sort()
#     for i in range(1,len(numbers)):
#         if numbers[i] == numbers[i-1]:
#             result.append(numbers[i])
#     return result

# print(dupi_items([1,2,4,5,6,6]))
# def duplicate_items(list_numbers): 
#     result = []
#     # Sort the array
#     list_numbers.sort()
#     # Iterate over the list
#     for i in range(1,len(list_numbers)):
#         # If previous element is the same as current, its the duplicate element
#         if list_numbers[i] == list_numbers[i - 1]:
#             result.append(list_numbers[i])

#     return result