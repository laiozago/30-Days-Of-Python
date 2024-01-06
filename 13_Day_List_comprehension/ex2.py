"""Flatten the following list of lists of lists to a one dimensional list :"""
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list = [number for sublist in list_of_lists for subsublist in sublist for number in subsublist]

print(list)