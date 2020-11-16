import numpy as np

class student:
    """
    The student class.
    """    
    def __init__(self,id,name,grades):
        self.id   = id              # student ID        
        self.name = name            # name of student
        self.grades = grades        # list of grades of student
        self.avg    = 999           # average grade

    def summary(self):
        """
        returns a short summary of the student and their average grade
        """
        self.mean(self.grades)
        txt = 'name; %s, average grade: %s' % (self.name, self.avg)
        return txt

    def mean(self,grades):
        """
        calculates mean grade
        """
        self.avg=np.mean(grades)

# create object list and objects       
students = [] # list containing all student objects
students.append(student(2,'Hans-Peter',[]))
students.append(student(41,'Klaus-Karl',[]))

# read grades
dat = np.genfromtxt('grades.asc')
grades = dat[1:len(dat)]   # 1st line is student ID, line 2 to end are grades

# update grades, assign grades to correct student using ID
for i in range( len(students) ):
    if students[i].id == int(dat[0,i]):        # if student id matches id from file (1st line in file)
        students[i].grades = dat[1:len(dat),i] # line 2 to last line are grades

# create lines of text output for student summaries
lines_out = [None]*len(students)
for i in range( len(students) ):
    lines_out[i] = students[i].summary()
    
# write output    
np.savetxt('summary.asc', lines_out, fmt="%s")    # format = string
