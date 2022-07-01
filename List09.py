def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    x = list1.count(list1[0])
    return x == len(list1)


print(main([0, 0, 0, 0, 1]))
