class People :
    name = ""
    age = 0
    height = 0
    familyMembers = 0
    def prepareToWriteInFile(self) :
        line = self.name + "|" + str(self.age) + "|" + str(self.height) + "|" + str(self.familyMembers)
        return line
newPeople = People()
loop = 1
choice = 'Y'
while loop <= 10 and ( choice == 'Y' or choice =='y' ) :
    newPeople.name = input("Please Enter your Name : ")
    print("Hello " + newPeople.name + "!")
    newPeople.height = int(input("Enter your height : "))
    newPeople.age = int(input("Enter your Age : "))
    newPeople.familyMembers = int(input("Enter number of familyMembers : "))
    lineForFile = newPeople.prepareToWriteInFile()
    print(lineForFile)
    print(lineForFile, file=open('C:/Test/peopleInfoDB.txt','a'))
    choice = input("Do You want to enter more details :\nPress Y/N\t:")
    loop = loop + 1
print("Thanks You for entering details")
print(input(""))
                       
