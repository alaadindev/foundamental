def max_substring(str):
    char_map = {} #char_map store all occuring char indices 'right'
    left = 0
    max_length = 0
    for right in range(len(str)):
        # check if char repeated
        if str[right] in char_map:
            # assign left to max between left, and 
            #the last index of the char stored in char_map
            left = max(left, char_map[str[right]]+1)
        #we store the current char and index
        char_map[str[right]] = right
        #assign max between old max and length between left and right index + 1
        max_length = max(max_length, right - left +1)

    return max_length

print(max_substring("abcabcbb"))