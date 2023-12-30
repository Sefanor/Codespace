'''
Write 2 Python functions to: 

show the list content. 
find the max value in the list.
Sample List : [10, 2, 3, 4, 7]
'''

sample_list = [10, 2, 3, 4, 7]

def show_list(my_list):
    print(f"The content of the list is: {my_list}")

def max_list(my_list):
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    print(f"The max value in the list: {max}")


show_list(sample_list)
max_list(sample_list)
