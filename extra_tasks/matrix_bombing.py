# TODO Find the proper lenght of the matrix!

from copy import deepcopy


def matrix_bombing(play_area):
    result_dict = {}
    for i in range(len(play_area)):
        cur_rotation = 0
        cur_matr = deepcopy(play_area)
        for row in range(len(cur_matr)):
            for col in range(len(cur_matr[row])):
                print("i = " + str(i))
                cur_rotation += 1
                if cur_rotation == i:
                    print("This is if cur_rotation == " + str(cur_matr[row][col]))


print(matrix_bombing([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
