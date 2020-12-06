def matrixElementsSum(matrix):
    forbidden = []
    options = []
    for level in matrix:
        for i in range(len(level)):
            if level[i] == 0:
                forbidden.append(i)
            if i in forbidden:
                pass
            else:
                options.append(level[i])
    return sum(options)