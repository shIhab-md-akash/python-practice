def is_list_item_unique():     

    lst= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return len(lst) == len(set(lst))
print(is_list_item_unique())  # Output: True


