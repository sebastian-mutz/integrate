# This is a Python script calling a mean function to calculate the arithmetic means of passed grades.
#
g = [1.7, 2.0, -9999.0, 2.3, 1.3, 1.0, 1.3, 3.3, 1.7, 1.0]     # list of grades 
#
import mutz_e002_functions as calc      # import module as calc
meanGrade = calc.mean(1,g)              # calculate the mean grade by calling the second mean function in the loaded module
print(meanGrade)                        # display the mean grade
