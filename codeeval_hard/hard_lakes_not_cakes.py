import sys

def fill_neighbors(row, col, id):
    global matrix
    global width
    global height
    for i in range(row-1, row+2):
        if i < 0 or height <= i:
            continue
        for j in range(col-1, col+2):
            if j < 0 or width <= j:
                continue
            #print("Fill Neigh: i={0} j={1}".format(i, j))
            if matrix[i][j] == 'o':
                matrix[i][j] = str(id)
                fill_neighbors(i, j, id)
                
def print_matrix():
    global matrix
    global width
    global height
    print("matrix size: %dx%d" % (width, height))
    for row in matrix:
        print(row)

with open(sys.argv[1], 'r') as test_cases:
    global matrix
    global width
    global height
    for test in test_cases:
        test = test.strip('\n')
        forest = test.split('|')
        matrix = []
        i = 0
        for partition in forest:
            matrix.append([])
            matrix[i] = [n for n in partition.split()]
            i += 1
        width = len(matrix[0])
        height = len(matrix)
        #print_matrix()
        cnt = 0
        for row in range(0, height):
            for col in range(0, width):
                #print("Main: row={0} col={1}".format(row, col))
                if matrix[row][col] == 'o':
                    cnt += 1
                    #print("cnt=%d" % cnt)
                    matrix[row][col] = str(cnt)
                    fill_neighbors(row, col, cnt)
        #print_matrix()
        print(cnt)