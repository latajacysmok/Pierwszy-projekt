def checkMaxLength(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    m = -1

    if (l1 > l2):
        m = l1
    else:
        m = l2

    return m


def lengthOfInt(n):
    s = str(n)
    return len(s)


class Person:
    def __init__(self, firstName, secondName, age, proffesion, mail):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age
        self.proffesion = proffesion
        self.mail = mail
        self.l = ["First Name: ", "Second Name: ", "Age: ", "Proffesion: ", "Mailbox: "]

    def getFirstName(self):
        return self.firstName

    def getSecondName(self):
        return self.secondName

    def getAge(self):
        return self.age

    def __lt__(self, other):
        if self.firstName < other.firstName:
            return self.firstName < other.firstName
        elif self.firstName >= other.firstName:
            if self.secondName < other.secondName:
                return self.secondName < other.secondName

    def __str__(self):
        s = ""
        x = []
        for i in self.l:
            x.append(len(i))

        x.sort(reverse=True)
        print("to jest x {}:".format(self.secondName), x)
        m = x[0]
        print("max: ", m)

        return s


class Database:
    def __init__(self, name):
        self.name = name
        self.newM = 0
        self.persons = []

    def addPerson(self, person):
        self.persons.append(person)

    def __str__(self):
        print("Welcome in " + self.name + " database!")
        print(self.newM)
        for person in self.persons:
            print(person)

        print("***********ENJOY!!!!**********")

        return ""

    def sortPersons(self):
        self.persons.sort()


    def addPersonsFromFile(self, path):
        fileObject = open(path, 'r')

        with open(path) as myFile:
            count = sum(1 for line in myFile)

        with open(path) as myFile:
            lines = myFile.readlines()

        numOfPersonsInFile = int(count / 5)
        newPersons = []

        for i in range(numOfPersonsInFile):
            p = Person(lines[0 + i*5], lines[1 + i*5], int(lines[2+i*5]), lines[3+i*5], lines[4+i*5])
            self.addPerson(p)




p1 = Person("Ludomir", "Newelski", 54, "Lecturer", "ludek@math.com")
p2 = Person("Ziemowit", "Rzeszotnik", 40, "Lecturer", "zioma@math.com")
p3 = Person("Andrzej", "Krakowiak", 66, "Lecturer", "krak@gmail.com")
p4 = Person("Andrzej", "Bed", 10, "Student", "imprezauandrzeja@wp.pl")

db = Database("PhysX2.0")
db.addPerson(p1)
db.addPerson(p2)
db.addPerson(p3)
db.addPerson(p4)
print(db)

db.sortPersons()

db.addPersonsFromFile('/home/peter/persons.txt')

print(db)







