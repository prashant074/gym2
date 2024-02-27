from model.groupExercise import GroupExercise
from model.member import Member
from model.trainer import Trainer

groupList = []
memberList = []
trainerList = []

# Auto create all objects
def create():
    userInput = input('Press enter to create 2 GroupExercise objects, 5 Member objects and 2 Trainer objects.\n')
    global groupList
    global memberList
    global trainerList
    
    # Create the objects for groups, members, and trainers
    groupList = [GroupExercise('Swimming', 3), GroupExercise('Running', 3)]
    memberList = [Member('Haochen', 'Zhu'), Member('Lu', 'Lu'), Member('Yang', 'Yang'), Member('Silver', 'Wang'), Member('Leo', 'Zhao')]
    trainerList = [Trainer('Bill','Gates', 'Swimming'), Trainer('Elon','Musk', 'Running')]

    return ('All objects created!')

# Checking all objects
def show():
    if groupList != [] and memberList != [] and trainerList != []:
        input('Press enter to show groups')
        for index, group in enumerate(groupList):
            print(index, group)
        
        input('\nPress enter to show members')
        for index, member in enumerate(memberList):
            print(index, member)

        input('\nPress enter to show trainers')
        for index, t in enumerate(trainerList):
            print(index, t)

        input('\nPress enter to return')
    else:
        input('\nPlease create objects first!')

# Choose a class and assign a trainer.
def assignTrainer():
    if groupList != [] and trainerList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            for index,t in enumerate(trainerList):
                print(f'{index} {t.firstName} {t.lastName}')
            trainerInput = int(input('Please choose the trainer. Number only.\n'))

            #validate object 
            if (0 <= groupInput < len(groupList)) and (0 <= trainerInput < len(trainerList)):
                trainerList[trainerInput].enrol(groupList[groupInput])
                return input(groupList[groupInput].assignTrainer(trainerList[trainerInput]))
            
            else:
                print('Incorrect index!')
    else:
        return input('No class has been created.\n')
            
# set the class fee as int                
def setClassFee():
    if groupList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')
            feeInput = input('Please input the fee per person. Number only.\n')

            #validate group and fee
            if (0 <= groupInput < len(groupList)) and feeInput.isnumeric():
                return input(groupList[groupInput].setFee(int(feeInput)))
            else:
                print('Incorrect index or fee!')

    else:
        return input('No class has been created.\n')
    
# Add member to a class
def addMember():
    # Same logic as assignTrainer, but for members
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            for index,t in enumerate(memberList):
                print(f'{index} {t.firstName} {t.lastName}')
            memberInput = int(input('Please choose the member. Number only.\n'))

            #validate object 
            if (0 <= groupInput < len(groupList)) and (0 <= memberInput < len(memberList)):
                result = groupList[groupInput].enrol(memberList[memberInput])
                #add groupObject to memberClass if success
                if result[1] == 1:
                    memberList[memberInput].enrol(groupList[groupInput])

                return result[0]

            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Removes a member from a class
def removeMember():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # show members
            if (0 <= groupInput < len(groupList)):
                for index,member in enumerate(groupList[groupInput].memberAll):
                    print(index, member)
                memberInput = input('Please choose the member to remove. Number only.\n')

                if (0 <= int(memberInput) < len(groupList[groupInput].memberAll)) and memberInput.isnumeric():
                    groupList[groupInput].memberAll[int(memberInput)].cancelEnrol(groupList[groupInput])
                    result = groupList[groupInput].removeMember(groupList[groupInput].memberAll[int(memberInput)])

                    return input(result[0])
                else:
                    input('Incorrect index!')
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Marks a member as present in a class
def checkinMember():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # choose members
            if (0 <= groupInput < len(groupList)):
                for index,member in enumerate(groupList[groupInput].memberAll):
                    print(index, member)
                memberInput = input('Please choose the member to checkin. Number only.\n')

                if (0 <= int(memberInput) < len(groupList[groupInput].memberAll)) and memberInput.isnumeric():
                    return input(groupList[groupInput].markAttendance(groupList[groupInput].memberAll[int(memberInput)]))
                else:
                    input('Incorrect index!')
            else:
                input('Incorrect index!')

    else:
        return input('No class or member has been created.\n')

# Lists all members enrolled in a particular class
def listMemberInClass():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = input('Please choose the class. Number only.\n')
            print('----------')

            # show members
            if (0 <= int(groupInput) < len(groupList)):
                print('The follwoing members are enrolled in ' + groupList[int(groupInput)].className)
                for member in groupList[int(groupInput)].memberAll:
                    print(member.firstName)
                return input('Press enter to return.')
            else:
                input('Incorrect index!')
    
    else:
        return input('No class or member has been created.\n')

# Lists all members on the waitlist for a particular class
def listMemberWaitClass():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # choose members
            if (0 <= groupInput < len(groupList)):
                print('The follwoing members are waitlisted in ' + groupList[groupInput].className)
                for member in groupList[groupInput].memberWaitlist:
                    print(member)
                return input('Press enter to return.')
            else:
                input('Incorrect index!')
    
    else:
        return input('No class or member has been created.\n')

# Shows the number of available slots in a class    
def classSlotNumber():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= groupInput < len(groupList)):
                return input(groupList[groupInput].numberAvailable())
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Shows the number of enrolled members in a class    
def classEnrolledNumber():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= groupInput < len(groupList)):
                return input(groupList[groupInput].numberEnrolled())
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Shows the number of members on the waitlist for a class
def classWaitNumber():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= groupInput < len(groupList)):
                return input(groupList[groupInput].numberWait())
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Shows the number of attendees in a class    
def classAttendNumber():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= groupInput < len(groupList)):
                return input(groupList[groupInput].numberAttend())
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Shows the attendance rate for a class    
def classAttendRate():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= groupInput < len(groupList)):
                return input(groupList[groupInput].attendanceClass())
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Calculates the total payment for a class
def totalPayment():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(groupList):
                print(index, i.className)
            groupInput = int(input('Please choose the class. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= groupInput < len(groupList)):
                return groupList[groupInput].totalPayment()
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

 # Displays the classes a member is enrolled in    
def memberClass():
    if groupList != [] and memberList != []:
        while True:
            for index, i in enumerate(memberList):
                print(index, i.firstName)
            memberInput = int(input('Please choose the member. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= memberInput < len(memberList)):
                return memberList[memberInput].enrolClassDisplay()
            else:
                input('Incorrect index!')
    else:
        return input('No class or member has been created.\n')

# Displays the classes a trainer is enrolled in
def trainerClass():
    if groupList != [] and trainerList != []:
        while True:
            for index, i in enumerate(trainerList):
                print(index, i.firstName)
            trainerInput = int(input('Please choose the member. Number only.\n'))
            print('----------')

            # using class method
            if (0 <= trainerInput < len(trainerList)):
                return trainerList[trainerInput].enrolClassDisplay()
            else:
                input('Incorrect index!')
    else:
        return input('No trainer has been created.\n')



            

