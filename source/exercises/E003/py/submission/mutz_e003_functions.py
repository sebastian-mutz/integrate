# This Python script contains 3 ways to calculate the arithmetic mean grade from a given array containing an anomalous value:
# 1. the list is modified by deleting the anomalous value entry, then the mean is calculated
# 2. the anomalous value is neglected using an if statement in a loop that sums up the values
# 3. like 2, but manually updating counter for remaining values (more primitive, works for all languages)
#
# Those methods are put in three separate function, which are nested in a function that is called externally.
#
#
# mean (option, g)
# ----------------
# Function to be called externally to calculate the mean grade. Passed arguments:
# 1. option - the option (1,2 or 3) determines which mean calculation will be used
# 2. g      - this is the list of grades to be used for the mean calculation
# Returns mean grade.
def mean(option, g):
#
    # 1st method (for one missing value, using list functions):
    # ---------------------------------------------------------
    def meanListFunctions(g):
        # prepare everything for calculation using some list functions
        mean = 0.0                      # we will store the sum and then the mean in this variable
        miss = g.index(-9999.0)         # save index value of the 1st missing students
        del g[miss]                     # delete anomalous entry from list of grades
        # calculate the mean grade
        for i in range(len(g)):         # loop through shortened list of remaining entries 
            mean = mean + g[i]          # we use the mean variable to sum up the remaining values in the grades list
        mean = mean/(len(g))            # we divide the sum by the number of remaining entries
        return mean                     # check our result
#
#
    # 2nd method (more flexible):
    # ---------------------------
    def meanLoopSum(g):
        # calculating the mean and taking missing students into consideration using if statements
        cnt  = g.count(-9999.0)         # count number of missing values 
        mean = 0.0                      # we will store the sum and then the mean in this variable
        for i in range(len(g)):         # loop through values in grades list
            if g[i] != -9999.0:         # if we are NOT dealing with a missing value
                mean = mean + g[i]      # we use the mean variable to sum up the remaining values in the grades list
        mean = mean/(len(g)-float(cnt)) # we divide the sum by the number of remaining entries and use float to convert the integer counter to a real        
        return mean                     # check our result
#
#
    # 3rd method (manual counting):
    # -----------------------------
    def meanLoopSumPrimitive(g):
        # calculating the mean and taking missing students into consideration using if statements
        cnt  = 0                        # resetting the counter that will count the number of non-missing students
        mean = 0.0                      # we will store the sum and then the mean in this variable
        for i in range(len(g)):         # loop through values in grades list
            if g[i] != -9999.0:         # if we are NOT dealing with a missing value
                cnt += 1                # update counter by 1, alernative: cnt = cnt + 1
                mean = mean + g[i]      # we use the mean variable to sum up the remaining values in the grades list
        mean = mean/float(cnt)          # we divide the sum by the number of remaining entries and use float to convert the integer counter to a real        
        return mean                     # check our result
#
    if option == 1:
        meanGrade = meanListFunctions(g)
    elif option == 2:    
        meanGrade = meanLoopSum(g)
    elif option == 3:    
        meanGrade = meanLoopSumPrimitive(g)
    else:
        print("invalid option")
#
#   return calculated mean grade
    return meanGrade    
