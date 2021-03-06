# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".

    # Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(lst):
    for x in range(len(lst)):
        if (lst[x] > 0):
            lst[x] = "big"
    return lst

biggie_size([-1, 3, 5, -5])

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
    # Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
    # Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(lst):
    count = 0
    for x in range(len(lst)):
        if (lst[x] > 0):
            count = count + 1
    lst[len(lst)-1] = count
    return lst

count_positives([-1,1,1,1])
count_positives([1,6,-4,-2,-7,-2])

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
    # Example: sum_total([1,2,3,4]) should return 10
    # Example: sum_total([6,3,-2]) should return 7

def sum_total(lst):
    sum = 0
    for x in range(len(lst)):
        sum = sum + lst[x]
    return sum

sum_total([1,2,3,4])
sum_total([6,3,-2])

# Average - Create a function that takes a list and returns the average of all the values.x
    # Example: average([1,2,3,4]) should return 2.5

def average(lst):
    sum = 0
    for x in range(len(lst)):
        sum = sum + lst[x]
    return sum/len(lst)

average([1,2,3,4])

# Length - Create a function that takes a list and returns the length of the list.
    # Example: length([37,2,1,-9]) should return 4
    # Example: length([]) should return 0

def length(lst):
    return len(lst)

length([37,2,1,-9])
length([])

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
    # Example: minimum([37,2,1,-9]) should return -9
    # Example: minimum([]) should return False

def minimum(lst):
    for x in range(1,len(lst),1):
        min = lst[0]
        if (lst == '[]'):
            return False
        if (lst[x]< min):
            min = lst[x]
        return min

minimum([37,2,1,-9])

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
    # Example: maximum([37,2,1,-9]) should return 37
    # Example: maximum([]) should return False

def maximum(lst):
    for x in range(1,len(lst),1):
        max = lst[0]
        if (lst[x] == '[]'):
            return False
        if (lst[x] > max):
            max = lst[x]
        return max

maximum([37,2,1,-9])

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
    # Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(lst):
    sum = 0
    max = lst[0]
    min = lst[0]
    for x in range(len(lst)):
        sum = sum + lst[x]
        if (lst[x]< min):
            min = lst[x]
        if (lst[x] > max):
            max = lst[x]
    some_dict = {}
    some_dict["sumTotal"] = sum
    some_dict["average"] = sum/len(lst)
    some_dict["minimun"] = min
    some_dict["maximum"] = max
    some_dict["length"] = len(lst)
    return some_dict

ultimate_analysis([37,2,1,-9])


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
    # Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(lst):
    for x in range(0, int(len(lst)/2)):
        temp = lst[x]
        lst[x] = lst[len(lst)-1-x]
        lst[len(lst)-1-x] = temp
    return lst

reverse_list([37,2,1,-9])