list_input = [-1,-1,0,1,1,0]

def pivot(list_input):
    for i in range(0, len(list_input)):
        list_left = sum(list_input[:i])
        list_right = sum(list_input[i+1:])
        
        if list_left == list_right:
            return i
    return -1

print(pivot(list_input))