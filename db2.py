import smtplib

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
    def __init__(self, firstName, secondName, age, proffesion, mailbox):
        self.firstName = firstName
        self.secondName = secondName
        self.age = age
        self.proffesion = proffesion
        self.mailbox = mailbox
        self.l = ["First Name: ", "Second Name: ", "Age: ", "Proffesion: ", "Mailbox: "]
        self.myL = [self.firstName, self.secondName, self.age, self.proffesion, self.mailbox]
        self.m = -1

    def getFirstName(self):
        return self.firstName

    def getM(self):
        return self.m

    def getSecondName(self):
        return self.secondName

    def getAge(self):
        return self.age

    def getProffesion(self):
        return self.proffesion

    def getMailbox(self):
        return self.mailbox

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
            # print("długość self.l[{}]: ".format(i), len(i))
            x.append(len(i))
        j = 0
        while j != len(self.myL):
            # print("długość myL[{}]: ".format(j), len(str(self.myL[j])))
            x[j] += len(str(self.myL[j]))
            # print(x[j])
            j += 1
        x.sort(reverse=True)
        # print("x: ", x)
        # print("to jest x {}:".format(self.secondName), x)
        self.m = x[0] + 2
        # print("m: ", m)
        # print("max: ", m)
        s = self.m * "-" + "\n"
        l = 0
        for k in self.myL:
            # print("to jest myL: ", k)
            s = s + "|" + self.l[l] + str(k) + (((self.m - 2) - (len(str(k)) + len(str(self.l[l])))) * " " + "|") + "\n"
            l += 1
            # s = s + "|" + self.l[0] + self.firstName + (((m - 2) - (len(self.firstName) + len(self.l[0]))) * " " + "|") + "\n" + "|" + self.l[1] +  self.secondName + (((m - 2) - len(self.secondName)) * " " + "|") + "\n" + \
            # "|" + self.l[2] + str(self.age) + (((m - 2) - len(str(self.age))) * " " + "|") + "\n" + "|" + self.l[3] + self.proffesion + (((m - 2) - len(self.proffesion)) * " " + "|")  + "\n" + "|" + self.l[4] + self.mailbox + (((m - 2) - len(self.mailbox)) * " " + "|") + "\n"
        s = s + self.m * "-" + "\n"
        return s
        # def getM(self):
        # return self.m


class Database:
    def __init__(self, name):
        self.name = name
        self.persons = []
        p = Person("A","B",10, "D","s")
        self.m = p.getM()

    def addPerson(self, person):
        self.persons.append(person)

    def __str__(self):
        print("Welcome in " + self.name + " database!")
        # print(self.m)
        for person in self.persons:
            # print("person: ", person,"dupa")
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
            # print(i)
            # print((lines[0 + i*6][:-1], lines[1 + i*6], lines[2+i*6], lines[3+i*6], lines[4+i*6]))
            p = Person(lines[0 + i * 6][:-1], lines[1 + i * 6][:-1], lines[2 + i * 6][:-1], lines[3 + i * 6][:-1],
                       lines[4 + i * 6][:-1])
            self.addPerson(p)

    def getPersons(self):
        return self.persons

    def getMails(self):
        l = self.getPersons()
        x = []

        for i in range(len(l)):
            x.append(l[i].getMailbox())

        return x



class MailBox:

    def __init__(self, db):
        self.sender = 'maksymles@gmail.com'
        self.receipers = ['deamondev@gmail.com']
        print(self.receipers)

    def sendMails(self):

        msg = """From: From Person <maksymles@gmail.com
        This is test.
        """

    gmail_user = 'xxx@gmail.com'
    gmail_password = 'xxx'

    sent_from = 'xxx@gmail.com'
    to = ['yyy@gmail.com', 'zzz@gmail.com']
    subject = 'OMG Super Important Message'
    body = 'Pierwszy, wy\n\n - Maksym'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')






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


print(db)

mB = MailBox(db)


