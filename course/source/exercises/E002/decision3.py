# in this script, we decide on an action based on 1. our target and 2. on who we are

# let's assign some values to our variables
target='human'                    # here, we assign the value 'human' to the target variable
i_am='dalek'                      # here, we assign the value 'dalek' to our identity variable
action='do nothing'               # the default action is set to 'do nothing'

# in the code below, we determine our action based on the values of the 2 variables above
if target == 'human':                         # if the target is 'human', proceed down the lines of indented code
    if i_am == 'dalek' or i_am == 'cyberman': # if we are 'dalek' or 'cyberman'...
        action = 'a bad thing'                # we set our action to 'a bad thing'
    else:                                     # if one of the 2 conditions above are not met ...
        action = 'greet human'                # we set our action to 'greet human'

print(action)                                 # we display the result of our decision making process
