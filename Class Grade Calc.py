# should read class names and averages information from a text file (CSV)
# START_CLASS, name: Physics, id: randint + name, START CATEGORIES, {hw: None}, {final: None}, {instapolls: None}, END CATEGORIES, END CLASS
# do you want to save grades for all the categories, determine the grade you need in a category, or calculate later?
# are categories defined in percentages or points
# enter cutoffs for grades in percent or points (or use default cutoffs by leaving blank, type preview to see default cutoffs)
# which category do you want to calculate for?
# what grade do you want for the class?
# enter grades for all other categories


# allow categories to be left empty so they can be filled later
#  
# should be able to determine what grade is needed if you don't have info for a single category
# should be able to remove and add categories dynamically
# should be able to determine both based off a percent type distribution (add to 100) or a points based distribution (add to whatever)
# can add custom grade cut offs for points based distributions or percent, can use these 
# make default grade cut offs available for later use by storing in config file

import os.path

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

CLASS_DICT = {}

class CourseBuilder:

    def __init__(self, courseName = "No Course Name"):
        self.name = courseName
        self.categoryDict = {}

    def addCategory(self, categoryName, categoryPercent):
        self.categoryDict[categoryName] = categoryPercent

    def deleteCategory(self, categoryName):
        del self.categoryDict[categoryName]

    def showCategory(self):
        print(self.categoryDict)
    
    def shareCategory(self):
        return self.categoryDict.items()
    
    def exportCategory(self):
        self.categoryExport = ""
        for i in self.categoryDict.items():
            self.categoryExport += i[0]
            self.categoryExport += "\n"
            self.categoryExport += str(i[1])
            self.categoryExport += "\n"
        self.categoryExport += "END_CLASS"
        print( self.categoryExport )


    
myDict = {}
myDict[1] = CourseBuilder("Physics")
myDict[1].addCategory("hw", 0.10)
myDict[1].addCategory("final", 0.80)
myDict[1].addCategory("instapoll", 0.10)
myDict[1].showCategory()
myDict[1].shareCategory()
myDict[1].exportCategory()

 #   def createConfig(self, courseName):



def initialize():
    i = 0
    if not os.path.isfile("Class_Grade_Calc.config"):
        configFile = open("Class_Grade_Calc.config", "w")
    if os.path.isfile("Class_Grade_Calc.config"):
        configFile = open("Class_Grade_Calc.config", "r")
        while True:
            line = configFile.readline()
            if "START_CLASS" in line:
                line = configFile.readline()
                CLASS_DICT[i] = CourseBuilder(line)
                line = configFile.readline()

                i += 1
                

            


def addClass():
    print("In Progress")
    main()




def savedClasses():
    selection = "Yes"
    if os.path.isfile("Class_Grade_Calc.config"):
        print()
        selection = (input(RED + "You have classes saved. Would you like to use their information? (Y/n)" + RESET)).strip()
        if selection == "n" or selection == "no" or selection == "NO" or selection == "No":
            print()
            print("Returning to main menu")
            main()
        else:
            print("Saved Classes")
            print("---------------")
        
    else:
        print()
        print("No classes are saved.")
        print()
        input(RED + "Press enter to return to main menu" + RESET)
        main()



def calculateGrade():
    print("In Progress")
    main()

def settings():
    print("In Progress")
    main()




def main():
    selection = 0
    while True:
        print()
        print(GREEN + "---- Class Grades Calculator ----" + RESET)
        print()
        print("1 - Add a class")
        print("2 - Saved Classes")
        print("3 - Calculate grade for a class")
        print("4 - Settings")
        print("5 - Exit")
        print()

        selection = (str(input(RED + "Choose an Option: " + RESET))).strip()
        if selection == "1":
            addClass()
            selection = 0
            break

        elif selection == "2":
            savedClasses()
            selection = 0
            break

        elif selection == "3":
            calculateGrade()
            selection = 0
            break

        elif selection == "4":
            settings()
            selection = 0
            break

        elif selection == "5":
            print()
            return

        else:
            print()
            input(RED + "Please enter a valid option. Press enter to return to main menu." + RESET)
            selection = 0
            continue





main()