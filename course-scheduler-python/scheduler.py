import random

class Course:
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        #defining the given arguments
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.cid}({self.credits}): {self.cname}" #returning the format string as per the question

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(other, Course): #checking if the other id is an instance of the class Coure
                if self.cid == other.cid: #checking their equality
                    return True
        return False




class Catalog:
    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings = {} #defining a dictionary to store the course data in
        
    @property #defining the getter method
    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname
        self.credits = credits
        value = Course(cid,cname,credits) #assigning the arguments of the last class in a variable called value
        if cid not in self.courseOfferings: #checking for the id's absence in the course data
            self.courseOfferings[cid] = value #if not, then adding it to the data
            return "Course added successfully"
        else:
            return "Course already added"

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        self.cid = cid
        if cid in self.courseOfferings: #to remove, first checking if it's in the data or not
            del self.courseOfferings[cid] #deleting it from the data
            return "Course removed successfully"
        else:
            return "Course not found"


    def _loadCatalog(self, cmpsc_catalog_small):
        with open(cmpsc_catalog_small, 'r') as f: #opening the file in read mode
            course_info = f.read() #read() reads the file and returns a string containing all the data and with a \n between the every line and then storing it in the variable
        # YOUR CODE STARTS HERE
        lst = []
        sec_lst = []
        lst = course_info.split("\n") #storing it in a list with each line as a different element
        for i in lst:
            sec_lst.append(i.split(",")) #creating a nested list with the each list containing each line (data for one course in a list)
        length = len(sec_lst) #storing the number of courses (list's length) in a variable
        for i in range(0, length): #starting a loop where i iterates through all the lists
            #storing the data for each course in their respective variable names
            id = sec_lst[i][0]
            name = sec_lst[i][1]
            credits = sec_lst[i][2]
            course_data = Course(id, name, credits) #storing the variables as arguments using the class Course
            self.courseOfferings[id] = course_data #adding the data in the course data dict with its course id as the main key
            
        
        


class Semester:
    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        if len(self.courses.keys()) == 0: #checking if the dictionary which has the courses' data is empty
            return "No courses"
        courses = "; ".join(self.courses.keys()) #defining a new variable, courses, which as all the course ids with a '; ' between them
        return courses

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        #checking if the course is already in the data using its id, if not, then adding it to the same
        self.course = course
        if course.cid in self.courses:
            return f"Course already added"
        self.courses[course.cid] = course
            
            

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        #checking if the course is not in the data using its id, if it is, then removing it from the same
        self.course = course
        if course.cid not in self.courses:
            return f"No such course"
        del self.courses[course.cid]

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        result = 0 #setting a arbitrary value as zero
        for cname in self.courses.values():
            result += int(cname.credits) #this function will add the credits of each course in the data in the result variable and will return the total credits
        return result
    
    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        if self.totalCredits >= 12: #checking if the student is full time or not i.e. when he/she has total credits 12 or above
            return True
        return False
    
class Loan:
    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount 
        self.loan_id = self.__getloanID #storing the function __getloanID in a variable to be used with a self attribute ahead

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Balance: ${self.amount}"

    __repr__ = __str__
    
    @property    
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        rand_int = random.randint(10000, 99999) #gives us a random number between 10,000 and 99,999, which is our loan ID
        return rand_int


class Person:
    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Person({self.name}, ***-**-{self.ssn[-4:]})"

    __repr__ = __str__

    @property
    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return f"***-**-{self.ssn[-4:]}" #returns the last four digits of the SSN and replacing the first 5 digits with a *

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        #if other (another person) is an instance of the class Person and their SSNs are same, it will return True
        self.other = other
        if isinstance(other, Person):
            if self.ssn == other.ssn:
                return True
        return False

class Staff(Person):
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn
        self.supervisor = supervisor


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        initials = "" #empty string which will store the initials
        name_lst = self.name.split() #spliting the name in a list
        length = len(name_lst)
        for i in range(0, length):
            initial = name_lst[i][0] #storing the first letter in each word
            initials += initial.lower() #adding it to the empty string but first converting it to lowercase
        
        return f"905{initials}{self.ssn[-4:]}" #returning as per the format given in the question

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        #setting a new supervisor, if it is an instance of the class Staff then setting it equal to the old supervisor
        if isinstance(new_supervisor, Staff):
            self.supervisor = new_supervisor.supervisor
            return "Completed!"
        return None


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        #if student is not an instance of the class Student and nothing will be processed, else, a hold will be applied 
        if not isinstance(student, Student):
            return None
        
        student.hold = True
        return "Completed!"

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        #if student is not an instance of the class Student and nothing will be processed, else, the hold will be removed
        if not isinstance(student, Student):
            return None
        
        student.hold = False
        return "Completed!"

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        self.student = student 
        #if student is not an instance of the class Student and nothing will be processed, else, the student will be un-enrolled by setting their active status to false 
        if not isinstance(student, Student):
            return None
        
        student.active = False
        return "Completed!"
            

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        if isinstance(person, Student):
            self.name = person.name
            self.ssn = person.ssn
        return Student(person.name, person.ssn, "Freshman") #creating a new student in the system using the class Student and giving the required arguments, only if the person is an instance of the class




class Student(Person):
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn
        self.classCode = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount() #storing a student account for the student in their self account

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Student({self.name}, {self.id}, {self.classCode})"

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        self.s_acc = StudentAccount(self) 
        return self.s_acc #creating and returning a student account for the student


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        #creating a unique student ID based on their initials and last 4 digits of their SSN
        initials = ""
        name_lst = self.name.split()
        length = len(name_lst)
        for i in range(0, length):
            initial = name_lst[i][0]
            initials += initial.lower()
        
        return f"{initials}{self.ssn[-4:]}"

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        #register a new semester for the student based on their current class year (classCode), only if there is no hold on them and their status is active
        if self.hold == True or self.active == False:
            return "Unsuccessful operation"
        
        length = len(self.semesters)+1
        if 2 > length >= 0:
            self.classCode = "Freshman"
            self.semesters[length] = Semester() #used the class Semester to store it as a class object and not a normal string
        elif 4 > length >= 2:
            self.classCode = "Sophomore"
            next_sem = max(self.semesters.keys()) + 1
            self.semesters[next_sem] = Semester()
        elif 6 > len(self.semesters) >= 4:
            self.classCode = "Junior"
            next_sem = max(self.semesters.keys()) + 1
            self.semesters[next_sem] = Semester()
        elif len(self.semesters) >= 6:
            self.classCode = "Senior"
            next_sem = max(self.semesters.keys()) + 1
            self.semesters[next_sem] = Semester()
            

        return None

    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        #enrolling a student in a course, also updating their account balance, only if there is no hold on them and their status is active
        if self.hold == True or self.active == False:
            return "Unsuccessful operation"
        if cid not in catalog.courseOfferings.keys(): #the dictionary used in the class Catalog to store the course data
            return "Course not found"

        max_sem = max(self.semesters.keys())
        if cid in self.semesters[max_sem].courses:
            return "Course already enrolled"
        if cid in catalog.courseOfferings.keys():
            course_class = catalog.courseOfferings[cid] 
            self.semesters[max_sem].addCourse(course_class) #using the function addCourse made under the class Semester to add the course to the dictionary
            credits = course_class.credits
            self.account.balance += int(credits) * self.account.CREDIT_PRICE #changing the balance
            return "Course added successfully"
        
    
    
    
    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        #droping a course for the student and also updating their account balance, only if there is no hold on them and their status is active
        if self.hold == True or self.active == False:
            return "Unsuccessful operation"
        
        max_sem = max(self.semesters.keys())
        if cid in self.semesters[max_sem].courses:
            course_class = self.semesters[max_sem].courses[cid] #storing the course id of the latest course of the student
            credits = int(course_class.credits)
            
            del self.semesters[max_sem].courses[cid] #removing the required course from the dictionary
            self.account.balance -= 0.5 * credits * self.account.CREDIT_PRICE #changing the balance
            return "Course dropped successfully"
            
        return "Course not found"
        

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        #requesting a loan for a student and updating their account balance with adding a new loan, only if there is no hold on them and their status is active
        self.amount = amount
        if self.hold == True or self.active == False:
            return "Unsuccessful operation"
        max_sem = max(self.semesters.keys())
        if self.semesters[max_sem].isFullTime == False: #using the isFullTime function defined in the class Semester to check if the student is not part-time
            return "Not full time"
         
        loan = Loan(amount) #using the class Loan to store its amount in loan as an argument of the class
        loan_id = loan.loan_id
        self.account.loans[loan_id] = loan
        self.account.makePayment(amount) #using the function makePayment from the class Loan to update the account balance when taking the loan


class StudentAccount:  
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}
    CREDIT_PRICE = 1000 #defining a class atribute containing the credit price


    def __str__(self):
        # YOUR CODE STARTS HERE
        id = self.student.id
        student = self.student.name
        return f"Name: {student}\nID: {id}\nBalance: ${self.balance}"
    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        #processing a payment where the balance is reducing by a specified amount
        self.amount = amount
        self.balance -= self.amount
        return self.balance


    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        #processing a charge where the amount is being added to the balance
        self.amount = amount
        self.balance += self.amount
        return self.balance