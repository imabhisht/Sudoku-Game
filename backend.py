
def solve(alpha):
    find = find_empty(alpha)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(alpha, i, (row, col)):
            alpha[row][col] = i

            if solve(alpha):
                return True

            alpha[row][col] = 0

    return False


def valid(alpha, num, pos):
    for i in range(len(alpha[0])):
        if alpha[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(alpha)):
        if alpha[i][pos[1]] == num and pos[0] != i:
            return False

    alphax_x = pos[1] // 3
    alphax_y = pos[0] // 3

    for i in range(alphax_y*3, alphax_y*3 + 3):
        for j in range(alphax_x * 3, alphax_x*3 + 3):
            if alpha[i][j] == num and (i,j) != pos:
                return False

    return True


def print_alphaard(alpha):
    for i in range(len(alpha)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(alpha[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(alpha[i][j])
            else:
                print(str(alpha[i][j]) + " ", end="")


def find_empty(alpha):
    for i in range(len(alpha)):
        for j in range(len(alpha[0])):
            if alpha[i][j] == 0:
                return (i, j)  
    return None
