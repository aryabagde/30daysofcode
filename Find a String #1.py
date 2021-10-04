"""After looking at question we can see that we need 5 iterations for finding a match between a substring(length 3) and string(length 7). Keep th count using whole.
"""
def count_substring(string, sub_string):
    whole = 0
    for i in range(len(string) - len(sub_string) + 1):
        if(string[i:i+len(sub_string)] == sub_string):
            whole = whole+1;
    return whole;  