# in this script, we decide on an action based on 1. our target and 2. on who we are

# let's assign some values to our variables
target='human'                    # here, we assign the value 'human' to the target variable
i_am='dalek'                      # here, we assign the value 'dalek' to our identity variable
action='do nothing'               # the default action is set to 'do nothing'

# in the code below, we determine our action based on the values of the 2 variables above
if target == 'human':             # if the target is 'human', proceed down the lines of indented code
    if i_am == 'dalek':           # if we are 'dalek' ...
        action = 'exterminate'    # we set our action to 'exterminate'
    elif i_am == 'cyberman':      # if we are not 'dalek', but we are 'cyberman' ...
        action = 'upgrade'        # we set our action to 'upgrade'
    else:                         # if both checks for our identity came out negative (if we are neither 'dalek' nor 'cyberman') ...
        action = 'greet human'    # we set our action to 'greet human'

print(action)                     # we display the result of our decision making process - note that this function will be executed in disregard of the results of the decision making above, because it is an unindented code block and therefore outside the if statement.
