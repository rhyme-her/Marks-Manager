# Marks Manager.py

# by Rhyme Her
# Created: 2017-01-27

#Procedure

#1. Start with getting a small window through graphics.
#2. The window can take inputs (create a classroom, open a class, info, or exit).
#3. Have the window alternate menus when each button is clicked.
    # 3.1 All menus (except for exit) should be able to return the program back to the
        # intial menu.
    # 3.2. ALL menus (except for exit) shoudl have an exit button.

#4. Create a classroom will create a fresh classroom.
#5. Open a classroom will first prompt if a class will be made through a file.

# --------------------------------------------------------------------------------

# Saving Students and Auto Save

# HAVE EVERY STUDENT IN AS A CLASS.

# Everytime an action is saved, have the program update the data in a text file
    # After wiping it of course.

# for i in student:
    # (self).mark = getText
# --------------------------------------------------------------------------------

#   Class Student:
    # First, it must have its own Entry Box on the screen.
        # That way we can retrieve its value every time the program refreshes.
    # Second, it must be able to count the amount of marks it has and store each one.
        # So it's like a dictionary of students, which have a dictionary of MARKS.
    # Third, it must be able to sort alphabetically by last name and worse grade.


# Adding Categories
    # Make the first lines of the document consist of the categories (in short form)
    # On the second line, have the extended names divided by a comma (so we can do .split(,)
    # On the third line, have the weight value. (CHECK AS NUMBER. IF NOT SEND A POP UP TO CHANGE IT)
    # On the fourth line, have the mark (SAME AS ABOVE WITH CHECKING)
    # On the fifth line, list general category weights.

    # For the students have the format like:
        # STUDENT NAME, Mark, Mark, Mark    (Split into a list through (,). Then for the name index it with list[1] and split it with [" "]

# Notes on how getting final scores were done.
#For final scores on tests assignments and tests:
    # First, gather the marks for each student.
    # Second, gather the outofmarks and weights for each category.
    # Get averages of students in a category and compile them.

    #For getting the final grade. Take all the averages we got of the students before, apply a weight factor and print out the final product.

    #For the TOTAL AVERAGE OF EVERYTHING, just take the total average of all students and print it.

from graphics import *
from button import *

################################################################################
################################################################################
################################################################################
################################################################################
try:

    def capitalization(word):
        """ Returns a string with each word capitalized """
        finalword = ""
        word = word.split()
        for i in range(len(word)):
            tempword = word[i].capitalize()                         # Ensures each word is capitalized properly.
            finalword += tempword + " "                             # Adds them back into the classroom name.
        return finalword

    def isadigit(number):
        """Checks for the occurances of letters"""
        try:
            x = float(number)
            x = True

        except ValueError:
            x = False
        if x == True:
            return True
        else:
            return False

    def isamark(number):
        """Checks if the mark is NR or numbers"""
        try:
            x = float(number)
            x = True

        except ValueError:
            x = False

        if x == True or number == "NR":
            return True
        else:
            return False

    def getMedian(l):
        """Returns the median of a list"""
        srting = sorted(l)
        midnum = len(l)//2
        if len(l) % 2:  #If only one value remains.
            return (srting[midnum])
        elif len(l) == 2:
            if l[1] == 0:
                return 0
            else:
                return l[0]/l[1]
        else:
            midnum = (srting[midnum] + srting[midnum+1]) / 2
            return midnum

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################

    class StudentMarks:
        """Class to be used alongside Student to store marks."""
        def __init__(self,win,text,studentnumber,categorynumber):
            self.markentrybox = Entry(Point(19+6*categorynumber,80-3*studentnumber),4)
            self.markentrybox.setText(text)
            self.markentrybox.draw(win)

        def returnmark(self):
            return self.markentrybox.getText()

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################

    class categoryTotals:
        """ Class used to create an object featuring category and weight""" # Willl allow final weight calculations.

        def __init__(self,name,weight):
            self.name = name
            self.weight = weight

        def __repr__(self):
            return '{} {}'.format(self.name,self.weight)

        def drawData(self,win,number):
            """ Draws a label and entry box for entering the final weights. """
            self.box = Entry(Point(19+6*number,89),4)
            self.box.setText(self.weight)
            self.box.draw(win)
            Text(Point(19+6*number,92),self.name).draw(win)

        def returnName(self):
            return self.name

        def getWeight(self):
            self.weight = self.box.getText()

        def returnWeight(self):
            return self.weight


    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################

    class Student:
        """ Creates a student. """
        def __init__(self,name,marks):
            self.name = capitalization(name)
            self.marks = marks.split()
            self.markslist = []
            self.average = []

        def __repr__(self):                                         # Allows the list to be displayed.
            return '{}'.format(self.name)

        def boxmark(self,win,text,studentnumber,categorynumber):
            markentrybox = Entry(Point(19+6*categorynumber,80-3*studentnumber),4)
            markentrybox.setText(text)
            markentrybox.draw(win)

        def entrybox(self,win,studentnumber):                       # Student Number is a position.
            """Creates an entry box"""
            self.box = Entry((Point(8,80-3*studentnumber)),13)
            self.box.setSize(10)
            self.box.setText(self.name)
            self.box.draw(win)

            self.markslist = []                                    # Resets the list (to avoid multiplying the list size)
            for i in range(len(self.marks)):
                v = StudentMarks(win,self.marks[i],studentnumber,i)
                self.markslist.append(v)

        def addnewcategory(self):
            """Add a new category and mark."""
            self.marks.append("0")

        def returnValues(self):
            """ Student Name changes"""
            self.name = capitalization(self.box.getText())
            for i in range(len(self.markslist)):
                v=self.markslist[i].returnmark()
                if isamark(v) == True:
                    self.marks[i] = v.upper()

        def returnMark(self,iteration):
            return self.marks[iteration]

        def returnName(self):
            return self.name

        def createAverages(self,listofmarks,listoutof,listofweights):
            """ Generates an average of all categories. Omits not received"""
            self.average = []
            for i in range(len(listofmarks)):
                if listofmarks[i] == "NR" or listoutof[i] == "" or listoutof[i]=="0":
                    self.average.append("N/A")
                else:
                    x = float(listofmarks[i])
                    x2 =float(listoutof[i])
                    self.average.append((x/x2)*100)

        def returnAverage(self,iteration):
            return self.average[iteration]

        def returnAllAverages(self):
            return self.average

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################


    class Marks:
        """ Allows categories and marks to be stored as objects"""
        def __init__(self,shortname,name,weight,outofmark):
            self.name = name
            self.shortname = shortname
            self.weight = weight
            self.outofmark = outofmark

        def __repr__(self):                                         # Allows the list to be displayed.
            return '{} {} {} {}'.format(self.name,self.shortname,self.weight, self.outofmark)

        def entrybox(self,win,number):
            """ Draws new category. """
            self.number = Text(Point(19+6*number,95),number+1)
            self.category = Entry(Point(19+6*number,92),4)
            self.category.setText(self.shortname)
            self.weightbox = Entry(Point(19+6*number,89),4)
            self.weightbox.setText(self.weight)
            self.outofmarkbox = Entry(Point(19+6*number,86),4)
            self.outofmarkbox.setText(self.outofmark)
            return self.category.draw(win), self.weightbox.draw(win),self.outofmarkbox.draw(win),self.number.draw(win)

        def returnValues(self):
            """ Returns all values in the boxes and updates."""
            self.shortname = self.category.getText().upper()
            if isadigit(self.weightbox.getText()) == True:          # Checks if it is a number.
                self.weight = self.weightbox.getText()
            if isadigit(self.outofmarkbox.getText()) == True:
                self.outofmark = self.outofmarkbox.getText()

        def returnOutOf(self):
            return self.outofmark

        def returnMark(self):
            """ Returns Mark"""
            return self.outofmark

        def returnName(self):
            """Returns short name"""
            return self.shortname

        def returnFullName(self):
            """Returns full name"""
            return self.name

        def returnWeight(self):
            """Returns weight"""
            return self.weight

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################

    def classroom(win,file):
        """ Turns the Window into a clasroom. Not a literal window though. """
        close,menu,file = False,False, file
        l,name,categories,categorylist,extendedname,mark,weight,ccompressed, ccompressedlist = [], [], [], [], [], [], [], [], []    # Pre-defined lists.
        ccompressedweight = []

    # --------------------- FILE READ AND LIST EDITING
        if file == True:    # If there is a file to open.
            filename = input("Input the .txt filename (no extension):")
            filer = open(filename+".txt",'r')
            classname = capitalization(filer.readline())
            categories = filer.readline().upper().split()
            extendedname = filer.readline().split(",")              # Splits through commas first.
            for i in range(len(extendedname)):                      # Capitalized every word.
                extendedname[i] = capitalization(extendedname[i])
            weight = filer.readline().split()
            mark = filer.readline().split()
            ccompressedweight = filer.readline().split()
            names = filer.read().split('\n')
            numofstud,numofcategories = len(names),len(categories)   # Num of Categories and Students
            filer = filer.close()

        else:                                                       # No file.
            classname = "Classroom Name"                            # DEFAULT CLASS NAME.
            numofstud, numofcategories = 0,0                        # Number of students for button drawing.

    # ------------ Modifying and refreshing lists.


        if numofstud != 0:
            for i in names:
                string = i.split(",")                              # See comment at the top about formats.
                v = Student(string[0],string[1])                        # Create students. Don't draw.
                l.append(v)                                             # Added to a list.

        if numofcategories != 0:
            for i in range(len(categories)):
                v = Marks(categories[i],extendedname[i],weight[i],mark[i])  # Add Category, don't draw.
                categorylist.append(v)                                  # Addded to a list.



    # --------------------- WHILE STATEMENT BELOW
        # ------------ Draw Assets

        while close == False:                                       # While the window hasn't closed yet.
            new = False         # Later tells the program to add a new weight.

            ccompressed, ccompressedlist,ccount = [],[],0           # CCount keeps track of what position ccompressedweight should index.
            if len(categories) != 0:
                for i in range(len(categories)):
                    c = categories[i]
                    if ccompressed.count(c) == 0:                   # Compiles a list of categories. Ex. Test, Exam, Assignment.
                        v = categoryTotals(c,ccompressedweight[ccount])
                        ccompressedlist.append(v)
                        ccompressed.append(c)
                        ccount += 1

            l.sort(key=lambda student:(student.name,))
            win.delete('all')                                       # Clears the entire window.

            classtext = Text(Point(6,98),"Classroom:").draw(win)
            marktext = Text(Point(6,95),"Mark").draw(win)
            categorytext = Text(Point(6,92),"Category").draw(win)   # Draws labels.
            weightext = Text(Point(6,89),"Weight").draw(win)
            outoftext = Text(Point(6,86),"Out of").draw(win)

            for i in range(5):
                Line(Point(0,96.5-3*i),Point(100,96.5-3*i)).draw(win)    # Draw line segments.


            if numofstud < 20:
                Line(Point(0,75-3*numofstud),Point(100,75-3*numofstud)).draw(win)   # Line under ADD STUDENT
                Line(Point(16,96.5),Point(16,69-3*numofstud)).draw(win)       # Vertical Line separating first + second column.
            else:
                Line(Point(0,19),Point(100,19)).draw(win)
                Line(Point(16,96.5),Point(16,12)).draw(win)

            if numofcategories != 0:
                if numofstud < 20:  # Drawing line under students.
                    for i in range(numofcategories):
                        Line(Point(22+6*i,93.5),Point(22+6*i,69-3*numofstud)).draw(win) #
                else:
                    for i in range(numofcategories):
                        Line(Point(22+6*i,93.5),Point(22+6*i,72-3*numofstud)).draw(win)


        # ---------------------------- Drawin buttons and boxes.

            exitbutton = Button(win,Point(95,5),8,5,"Exit")        # Exit Button.
            menubutton = Button(win,Point(85,5),8,5,"Menu")
            menubutton.activate()
            exitbutton.activate()

            if numofstud < 20:
                addstudent = Button(win,Point(8,(78-3*numofstud)),13,5,"ADD STUDENT")    # Add Student Button (MAX 20)
                addstudent.activate()

            if numofcategories < 7:                                 # Maximum 7 (13 Categories could fit, but 7 prevents having too little space or too many values to calculate.
                addcategory = Button(win,Point(20+6*numofcategories,95),4,3,"ADD")
                addcategory.activate()

            classroomname = Entry(Point(20,98),20)                  # Name of Classroom.
            classroomname.setText(classname)                        # Sets text.
            classroomname.draw(win)                                 # Draw to window.

            if numofstud != 0:                                      # Doesn't loop if no students are available.
                for i in range(len(l)):                             # Draws every student.
                    v = l[i].entrybox(win,i)                        # All student names will be displayed as entries
                    Text(Point(2,80-3*i),str(i+1)).draw(win)

            if numofcategories != 0:                                # Drawing categories + Weights
                for i in range(numofcategories):
                    vc = categorylist[i].entrybox(win,i)
                for i in range(len(ccompressed)):
                    vcc = ccompressedlist[i].drawData(win,i+numofcategories)



            # ---------------- Averaging Marks
            if numofstud == 20:
                Text(Point(10,17),"AVERAGE").draw(win)
                Text(Point(10,14),"MEDIAN").draw(win)
            else:                                          # DONE OUTSIDE
                Text(Point(10,73-3*(len(l))),"AVERAGE").draw(win) # TO PREVENT MULTIPLE DRAWINGS
                Text(Point(10,70-3*(len(l))),"MEDIAN").draw(win)

            if numofcategories != 0 and numofstud != 0:
                for i in range(numofcategories):
                    marklist = []

                    for i2 in range(len(l)):
                        v = l[i2].returnMark(i)
                        if isadigit(v) == True:         # Find integers.
                            marklist.append(v)

                    for i3 in range(len(marklist)):
                        marklist[i3] = float(marklist[i3])    # Turn the marks into floats.

                    if int(categorylist[i].returnMark()) != 0:      # Drawing totals and median.
                        tempvalue = (sum(marklist)) / ((int(categorylist[i].returnMark())) * (len(marklist)))
                        total = "{0:.0f}".format( tempvalue * 100)
                        median = "{0:.0f}".format(getMedian(marklist))
                        if numofstud == 20:
                            Text(Point(19+6*i,17),total).draw(win)
                            Text(Point(19+6*i,14),median).draw(win)
                        else:

                            Text(Point(19+6*i,73-3*len(l)),total).draw(win)
                            Text(Point(19+6*i,70-3*len(l)),median).draw(win)

                for i in range(len(l)): #Drawing the averages under the general categories for each student.
                    outoflist, listofmarks,listofweights = [],[],[]
                    for i2 in range(len(ccompressed)):
                        currentcategory = ccompressed[i2]
                        for i3 in range(len(categorylist)):

                            if categorylist[i3].returnName() == currentcategory:
                                outoflist.append(categorylist[i3].returnOutOf())    # Return the outof for i3(the category number/name)
                                listofmarks.append(l[i].returnMark(i3))     # Return the mark of a category (i3)
                                listofweights.append(categorylist[i3].returnWeight())   # Return the weight.

                    l[i].createAverages(listofmarks,outoflist,listofweights)

            # DRAWING THE FINAL AVERAGES HERE

            Text(Point(24+6*(len(categories)+len(ccompressed)),89),"AVERAGE").draw(win)
            finalaverages = []

            for i in range(len(l)):
                finalnumbers = [] # Final Average for student.
                value = 0
                for x in range(len(ccompressed)):    # First getting individual categories.
                    temporarylist,wlist=[],[] #Student mark averages with weight. Total Weight.
                    position = []   # Store index positions.
                    glist = []

                    for y in range(len(categorylist)):
                        if categorylist[y].returnName() == ccompressed[x]:   # If the names match
                            position.append(y)      # Add position
                            g = l[i].returnAverage(value)
                            w = float(categorylist[y].returnWeight())
                            if isadigit(g) == True and isadigit(w) == True or g != "N/A":

                                glist.append(g*w)
                                wlist.append(w)
                                value += 1              # The averages for the student are auto sorted together, but not the weights.
                    if wlist != []:
                        finalnumbers.append(sum(glist) / sum(wlist))  # Total Average for a category

                floatweight = []    # List of total category weights
                for i2 in range(len(ccompressedweight)):
                    tempw = float(ccompressedweight[i2])
                    if tempw == 0 and tempw == "" and finalnumbers != []:

                        finalnumbers[i2].remove(finalnumbers[i2])       # Does not count that value if there is no weight.
                    else:
                        floatweight.append(tempw)
            # ---
                tempv = []
                for i2 in range(len(finalnumbers)):
                    tempv.append((finalnumbers[i2]) * (floatweight[i2])/100)
                finalaverages.append(sum(tempv))

            # NOW DRAWING ALL THE AVERAGES!
            for i in range(len(l)):
                Text(Point(24+6*(len(categories)+len(ccompressed)),80-3*i),"{0:.0f}".format(finalaverages[i])).draw(win)

            if len(l) != 0:
                Text(Point(24+6*(len(categories)+len(ccompressed)),73-3*(len(l))),"{0:.0f}".format(sum(finalaverages)/len(finalaverages))).draw(win)
                Text(Point(24+6*(len(categories)+len(ccompressed)),70-3*(len(l))),"{0:.0f}".format(getMedian(finalaverages))).draw(win)


    # ------------------------------ MOUSE CLICK BELOW

            p = win.getMouse()

            if exitbutton.clicked(p):
                close = True
            elif menubutton.clicked(p):
                menu = True
            elif addstudent.clicked(p) and numofstud != 20:
                numofstud += 1                                      # Expand class length.
                emptymarks = "0 " * numofcategories
                v = Student("Student".format(numofstud),emptymarks)
                v.entrybox(win,numofstud)                                  # Create new student.
                l.append(v)

            elif addcategory.clicked(p):
                numofcategories += 1                                # Expands category count.
                cname = "Category {}".format(numofcategories)
                cshort = "C{}".format(numofcategories)
                cweight, cmark = "0", "0"
                vc = Marks(cshort,cname,cweight,cmark)
                vc.entrybox(win,numofcategories)
                categorylist.append(vc)
                categories.append(cshort)
                new = True                      # Tells the program to add a new weight after saving.
                for i in range(len(l)):                             # Adds the new categories to the students.
                    l[i].addnewcategory()


    # ------------------------------------- SAVING AND REOBTAINING

            classname = capitalization(classroomname.getText())                                     # Resets the class name.

            if numofstud != 0:
                for i in range(len(l)):                             # Update the names. (IF THERE IS STUDENTS)
                    l[i].returnValues()                               # Returns name alongside capitalization

            categories = []
            ccompressedweight = []
            initialnumofcat =  len(ccompressed)#Initial Number of General Categories

            if numofcategories != 0:
                for i in range(len(categorylist)):
                    categorylist[i].returnValues()
                    categories.append(categorylist[i].returnName())
                for i in range(len(ccompressedlist)):
                    ccompressedlist[i].getWeight()
                    v = ccompressedlist[i].returnWeight()
                    ccompressedweight.append(v)


            if len(categories) != 0:
                for i in range(len(categories)):
                    c = categories[i]
                    if ccompressed.count(c) == 0:                   # If a category name is modified, adds a new weight.
                        ccompressedweight = ["0"] + ccompressedweight

            if new == True:
                ccompressedweight.append("0")

        # ------------------------- WRITE TO A FILE
            filew = open(classname.rstrip()+".txt","w")
            filew.seek(0)           # ERASE ALL CONTENTS
            filew.truncate()

            filew.write("{}\n".format(classname))

            for i in range(len(categories)):    # Writing Categories
                filew.write(categories[i]+" ")
            filew.write("\n")

            for i in range(len(categories)):    # Category Full Names
                if i == len(categories)-1:
                    filew.write(categorylist[i].returnFullName().rstrip())
                else:
                    filew.write(categorylist[i].returnFullName().rstrip()+",")
            filew.write("\n")
            for i in range(len(categories)): # Return Weight
                filew.write(categorylist[i].returnWeight()+" ")
            filew.write("\n")

            for i in range(len(categories)): # Return out of.
                filew.write(categorylist[i].returnOutOf()+" ")
            filew.write("\n")

            for i in range(len(ccompressed)):   # Return general categories (assignments, exams, tests)
                filew.write(ccompressedweight[i]+" ")
            filew.write("\n")

            for i in range(len(l)): #Now compiling every students mark and name.
                filew.write(l[i].returnName().rstrip()+",")
                for i2 in range(len(categories)):
                        filew.write(l[i].returnMark(i2)+" ")
                if i != len(l)-1:
                    filew.write("\n")
            filew.close()
            if close == True:
                win.close()

            elif menu == True:
                win.delete('all')
                mainscreen(win)

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################
    def information(win):
        exitbutton = Button(win,Point(95,5),8,5,"Exit")        # Exit Button.
        menubutton = Button(win,Point(85,5),8,5,"Menu")
        menubutton.activate()
        exitbutton.activate()
        Text(Point(50,95),"MARKS MANAGER").draw(win)
        Text(Point(50,85),"This program is designed to record user inputs.").draw(win)
        Text(Point(50,80),"It will auto-save upon every click.").draw(win)
        buttonpress = False

        while buttonpress == False:
            p = win.getMouse()
            if exitbutton.clicked(p):
                win.close()
                buttonpress = True

            elif menubutton.clicked(p):
                win.delete('all')
                mainscreen(win)
                buttonpress = True

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################

    def mainscreen(win):
        """ The main menu of the Marks Manager."""
        buttonpress = False # Waiting for a button press.

        cc = Button(win,Point(25,40),40,15,"Create")            # Create a Classroom
        oc = Button(win,Point(75,40),40,15,"Open")              # Open a Classroom
        info = Button(win,Point(25,20),40,15,"Info")            # Information
        exitbutton = Button(win,Point(75,20),40,15,"Exit")

        title = Text(Point(50,80),"MARKS MANAGER")
        title.setSize(20)
        title.draw(win)

        Text(Point(50,75),"CODED BY GARY HER").draw(win)

        cc.activate()
        oc.activate()
        info.activate()
        exitbutton.activate()

        while buttonpress == False:

            p = win.getMouse()                                  # Wait for mouse click.
            if cc.clicked(p):
                classroom(win,False)
                buttonpress = True                              # Stops while loop.

            elif oc.clicked(p):
                classroom(win,True)
                buttonpress = True                              # Stops while loop.


            elif info.clicked(p):
                win.delete('all')                               # Clears screen.
                information(win)
                buttonpress = True                              # Stops while loop.


            elif exitbutton.clicked(p):
                buttonpress = True                              # Stops while loop and prevents erorr.
                win.close()                                     # Close

    ################################################################################
    ################################################################################
    ################################################################################
    ################################################################################

    def startup():
        """Creates a window that will be transfered to the main menu."""
        win = GraphWin("Marks Manager",1024,800)
        win.setCoords(0,0,100,100)
        mainscreen(win)

    startup()

except:
    pass