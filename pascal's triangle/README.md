# Math - Pascal's Triangle
- Using python to print pascal's triangle along n rows as per user input.

# Usage
- ```python main.py```

# Working
This code allows you to generate and print Pascal's triangle with a number of rows specified by the user.

The program begins by prompting the user to input the desired number of rows. It then reads in this input as an integer using the input() and int() functions.

Next, a function is called with the number of rows as an argument. This function creates the triangle using a list of lists. It iterates through each row of the triangle, generating a new row with i+1 elements. The elements of each row are then filled in by adding adjacent elements from the previous row. Once each row is complete, it is added to the triangle list.

Finally, the triangle is printed using a loop over each row of the triangle. To ensure each row is displayed neatly and aligned, the center() function is used.

Overall, this code utilizes an algorithm to create and print Pascal's triangle based on the number of rows specified by the user.

# Authors
- AlmightyNan