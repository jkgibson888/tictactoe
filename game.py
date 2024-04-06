def didWin(array):
    for x in array:
        #check horizontally
        if array[x][0] == array[x][1] and array[x][1] == array[x][2]:
            return array[x][0]

         #check vertically for win
        if array[0][x] == array[1][x] and array[1][x] == array[2][x]:
            return array[0][x]

    #check diagonally
    if array[0][0] == array[1][1] and array[1][1] == array[2][2]:
        return array[0][0]

    if array[0][2] == array[1][1] and array[1][1] == array[2][0]:
        return array[0][2]