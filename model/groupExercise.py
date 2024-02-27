import model.member as modelMember
import model.trainer as modelTrainer

class GroupExercise:
    def __init__(self, className, maxCapacity):
        self.__className = className
        self.__trainer = None
        self.__maxCapacity = maxCapacity
        self.__memberAll = []
        self.__memberWaitlist = []
        self.__fee = None
        self.__memberCheckin = []

    # String representation of the class
    def __str__(self):
        return (f'This is {self.__className} class.\n{self.__trainer} is the trainer.\n\
Max {self.__maxCapacity} students allowed.\n')
    
    #----------------------------------------------
    # getter and setter for each attributes

    @property
    def className(self):
        return self.__className
    
    @className.setter
    def className(self, value):
        if not isinstance(value, str):
            raise ValueError('Class name must be a string!')
        self.__className = value

    @property
    def trainer(self):
        return self.__trainer
    
    @trainer.setter
    def trainer(self, value):
        if not isinstance(value, modelTrainer):
            raise ValueError('Trainer must be a trainer object!')
        self.__trainer = value

    @property
    def maxCapacity(self):
        return self.__maxCapacity
    
    @maxCapacity.setter
    def maxCapacity(self, value):
        if not isinstance(value, int):
            raise ValueError('Max Capacity of the class must be an integer!')
        self.__maxCapacity = value

    @property
    def memberAll(self):
        return self.__memberAll
    
    @memberAll.setter
    def memberAll(self, value):
        if not isinstance(value, list):
            raise ValueError('Class member list must be a list!')
        self.__memberAll = value

    @property
    def memberWaitlist(self):
        return self.__memberWaitlist
    
    @memberWaitlist.setter
    def memberWaitlist(self, value):
        if not isinstance(value, list):
            raise ValueError('The waitlist must be a list!')
        self.__memberWaitlist = value

    @property
    def fee(self):
        return self.__fee
    
    @fee.setter
    def fee(self, value):
        if not isinstance(value, int):
            raise ValueError('Fee must be a number!')
        self.__fee = value

    @property
    def memberCheckin(self):
        return self.__memberCheckin
    
    @memberCheckin.setter
    def memberCheckin(self, value):
        if not isinstance(value, list):
            raise ValueError('Checked-in member list must be a list!')
        self.__memberCheckin = value

    #----------------------------------------------
    # methods below
    # Methods specific to the GroupExercise class

    # Constant for status
    __success = 1
    __fail = 2
    __other = 3
    
    # Enroll a member to the class or add to waitlist if full
    def enrol(self, member):
        if member not in self.__memberAll and member not in self.__memberWaitlist:
            currentCapacity = len(self.__memberAll)
            if currentCapacity < self.__maxCapacity:
                self.__memberAll.append(member)
                return ((member.firstName + ' has been added to the enrolled list of ' + self.__className + '!'), self.__success)
            else:
                while True:
                    userInput = input('Unfortunately the class has been fully enrolled.\nAre you happy to be added to the waitlist? (y/n)')
                    if userInput.upper() == 'Y' or userInput.upper() == 'YES':
                        self.__memberWaitlist.append(member)
                        return ((member.firstName + ' has been added to the waitlist of ' + self.__className + '!'), self.__success)
                    elif userInput.upper() == 'N' or userInput.upper() == 'NO':
                        return ('Class enrolment cancelled.', self.__fail)
                    else:
                        print('Please re-enter.')
        else:
            return ('Member already in enrolled list or waitlist!', self.__fail)

    # Remove a member from the enrolled list
    def removeMember(self, member):
        if member in self.__memberAll:
            self.__memberAll.remove(member)
            return ((member.firstName + ' has been removed from the enrolled list.'), self.__success)
        else:
            return ((member.firstName + ' is not in the enrolled list'), self.__fail)

    # Print the members currently enrolled in the class  
    def displayEnrolled(self):
        print('All gym members currently enrolled in ' + self.__className)
        for member in self.__memberAll:
            print(member)
    
    # Assign a trainer to the class
    def assignTrainer(self, t):
        self.__trainer = t
        return (t.firstName + ' has been assigned as the trainer of ' + self.__className)
    
    # Return the number of members enrolled in the class
    def numberEnrolled(self):
        return (str(len(self.__memberAll)) + ' members has enrolled in the class!')
    
    # Return the number of slots available for enrolment
    def numberAvailable(self):
        available = self.__maxCapacity - len(self.__memberAll)
        return (str(available) + ' slots available for enrolment!')
    
    # Return the number of members on the waitlist
    def numberWait(self):
        return (str(len(self.__memberWaitlist)) + ' members are waiting in the class!')
    
    # Return the number of members who have attended the class
    def numberAttend(self):
        return (str(len(self.__memberCheckin)) + ' members has attended in the class!')
    
    # Set the fee per member for the class
    def setFee(self, fee):
        if not isinstance(fee, (int, float)):
            raise ValueError('Fee must be a number!')
        self.__fee = fee
        return ('Fee set.')

    # Calculate and return the total payment received
    def totalPayment(self):
        if self.__memberAll != [] and self.__fee != None:
            total = len(self.__memberAll) * self.__fee
            return ('The total payment received is ' + str(total) + ' NZD.')
        else:
            return 'Nobody enrolled the class or fee has not been set yet.'
    
    # Mark a member's attendance (same as checkin)
    def markAttendance(self, member):
        if member in self.__memberAll:
            self.__memberCheckin.append(member)
            return (member.firstName + "'s attendance has been marked.")
        else:
            return (f"Caution: you cannot mark {member.firstName}'s attendance because {member.firstName} is not in the enrolled list.")

    # Calculate and return the attendance percentage of the class    
    def attendanceClass(self):
            if self.__memberAll != []:
                return ('The attendance of the class is '+ str(round(((len(self.__memberCheckin) / len(self.__memberAll))* 100), 2)) + '%')
            else:
                return 'Nobody enrolled the class.'