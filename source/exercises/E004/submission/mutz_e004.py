class mob:
    """
    The mob class is a class for mobile NPC units in a computer game.
    """    
    def __init__(self,id,name,kind,disposition):
        self.id   = id              # ID assigned to element by A.I.        
        self.name = name            # name of mob
        self.kind = kind            # kind of mob
        self.disp = disposition     # disposition toward player, 0 = neutral, 1 = hostile

    def describe(self):
        """
        returns a short summary of the object as text
        """
        txt = 'name; %s, kind: %s, disposition %s' % (self.name, self.kind, self.disp)
        return txt

    def reaction(self, action):
        """
        changes the disposition of the mob if attacked or left alone
        """      
        if action == 1:   # if attacked
            self.disp = 1   
        elif action == 0: # if left alone
            self.disp = 0  
        else:
            print("not a valid option")

# create class instance                            
mephisto=mob(1,'mephisto','final boss', 0)

# game loop
while True:
    print("You ran into: ", mephisto.describe())
    action = input("What do you do? Attack [1] or Leave alone [0]: ")  # get player input
    mephisto.reaction(int(action))                                     # let mephisto react
    if mephisto.disp == 1:                                             # get the reaction of mephisto based on your action
        print("You died. Game over.")
        break
