def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    letter=0
    digits=0
    idx=0
    while idx<len(txt):
        if txt[idx].isalpha():
            letter+=1
        if txt[idx].isdigit():
            digits+=1
        idx+=1
    count={letter:digits}
    return count
print(count_all("Asus pro max 3000"))