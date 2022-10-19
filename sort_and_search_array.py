import array as arr
'''
Program: sort_and_search_array.py
Author: Joshua M McGinley
Last Date Modified: 10/19/2022

Make a new file sort_and_search_array.py in Module 8. For this assignment, you can hard-code a list you pass to the sort_array() and search_array().

    Write 2 functions sort_array() and search_array().
        search_array()
            Returns the index of the object in the list or a -1 if the item is not found
        sort_array() will sort the list
            What is the return statement?
                Write a comment explaining why you included return OR
                Write a comment explaining why your code has no return statement.

'''
a = arr.array('I', [1,2,3,4,5,6,7,8,27,30,68,95,21,12,5,44,30,20,50,80,75,6,666,3,9,20])
def sort_array():
    # print(a)
    a_list = a.tolist()
    # print(a_list)
    a_list.sort()
    return a_list


def search_array():
    try:
        to_find = int(input('What are you looking for? '))
        found = a.index(to_find)
    except:
        found = -1
    return found

if __name__=='__main__':
    print(a)
    looking_for = search_array()
    print(looking_for)
    now_sorted = sort_array()
    print(now_sorted)

## I have included a return statement because I have converted the array into a list and sorted it...
## inorder to be able ot access the list outside of the function I returned it. By doing so it will be mantained in
## in memory.
