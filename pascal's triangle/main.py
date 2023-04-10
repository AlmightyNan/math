def pascal_triangle(n):

    triangle = []                # create an empty list to store rows of the triangle
    for i in range(n):           # loop over each row of the triangle
        row = [1] * (i+1)        # create a new row with i+1 elements

        for j in range(1, i):    # fill in the elements of the row

            row[j] = triangle[i-1][j-1]\
                     + triangle[i-1][j]
            
        triangle.append(row)     # add the row to the triangle

    for row in triangle:         # print the triangle
        print(' '.join(str(x) for x in row).center(n*2))

n = int(input("How many number of rows to append?\n->  "))    # prompt the user for the number of rows
pascal_triangle(n)                                            # print the triangle


''' 
Author:     AlmightyNan
Project:    math
Repo:       https://github.com/AlmightyNan/math
'''