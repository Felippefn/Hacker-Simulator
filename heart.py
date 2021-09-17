import random
import types
import time
import calendar
import sys
import string
from random import randrange
from datetime import datetime


class user_privacity:
    def __init__(self, _name, _secondName, _userCode, _moneyAcc, _location):
        self.name = _name
        self.secondName = _secondName
        self.userCode = _userCode
        self.moneyAcc = _moneyAcc
        self.location = _location


class user_socialmedia:
    def __init__(self, sname, ssecondName, sapp, slocation, scelphone):
        self.name = sname
        self.secondName = ssecondName
        self.apps = sapp
        self.location = slocation
        self.celphone = scelphone


now = datetime.now()
currentTime = now.strftime("%H:%M")
listFirstName = ['John', 'Clarice', 'David', 'Candice', 'Bryan', 'Charlie', 'Andrew', 'Mary', 'Mike', 'Becca', 'Barto',
                 'Callison', 'Cable', 'Daiva', 'Dominique', 'Juan', 'William', 'Billie', 'Ariana', 'Tallie', 'Drey', 'Adam', 'Natalia', 'Jacob', 'Pedro', 'Gabriela', 'Fernanda']
listSecondName = ['F.', 'A.', 'B.', 'Smith', 'Brown', 'Jones', 'Rodriguez',
                  'Martinez', 'Hernandez', 'Wilson', 'Lopez', 'Clifford', 'Dias', 'Ferrari', 'Costa']
listContries = ['Brazil', 'USA', 'China', 'Australia', 'Canada', 'France', 'India', 'United Kingdom', 'Japan',
                'South Korea', 'Portugal', 'Spain', 'Chile', 'South Africa', 'Sweden', 'Mexico', 'Egypt', 'Turkey', 'Italy', 'Argentina']
listApps = ['Instagram', 'Snapchat', 'Facebook', 'Tiktok', 'Youtube']
listCelphone = ['Iphone X', 'Iphone 11', 'Iphone 12', 'Iphone 6', 'Iphone 6s', 'Iphone 8', 'Iphone 8',
                'Note 10', 'Samsung S20', 'Samsung S21', 'Samsung A71', 'Samsung A32', 'XIAOMI MI 11', 'XIAOMI REDMI NOTE 9']


def base_str():
    return(string.ascii_letters+string.digits)


def key_gen():
    keyList = [random.choice(base_str()) for i in range(10)]
    return("".join(keyList))


def socialmFunction():
    socialmList = []
    for i in socialmList:
        socialmList.append(user_socialmedia(random.choice(listFirstName),
                                            random.choice(listSecondName), random.choice(listApps), random.choice(listContries), random.choice(listCelphone)))
        print("Tracking a random user...")
        print(socialmList[i].name + " " + socialmList[i].secondName + "\t\t|| " +
              + "\t\t|| " + socialmList[i].apps + "\t\t|| " + socialmList[i].location + socialmList[i].celphone)


def appleFunction():
    appList = []
    for i in range(10):
        internetVel = random.randint(5, 700)
        online_users = random.randint(1000000, 100000000)
        appList.append(user_privacity(random.choice(listFirstName),
                                      random.choice(listSecondName), random.choice(listApps), ipRandom(), random.choice(listContries)))
        print(appList[i].name + " " + appList[i].secondName + "\t\t|| " +
              str(appList[i].userCode) + "\t\t|| " + str(appList[i].moneyAcc) + "\t\t|| " + appList[i].location + " || " + str(internetVel) + "Mb/s")


def bankFunction():
    global Sum
    print("[i]STATUS: USING VIRTUAL MACHINE\n")
    print(actualMachine)
    Sum = 0
    userList = []
    for i in range(10):

        randomCode = random.randint(10, 10000)
        bankCode = key_gen()
        dinheiro = random.randint(10000, 10000000)
        Sum += dinheiro
        userList.append(user_privacity(random.choice(listFirstName),
                                       random.choice(listSecondName), bankCode, dinheiro, random.choice(listContries)))
        print(userList[i].name + " " + userList[i].secondName + "          \t\t||          " +
              str(userList[i].userCode) + "          \t\t||          " + str(userList[i].moneyAcc) + "          \t\t||          " + userList[i].location)
    actionUser = input(
        '\n[*]||found 10 accounts, do you want to transfer the money to your account? ')
    if actionUser == "yes":
        print("[!]your current money now is: ", Sum)
    else:
        print("[x]leaving bank system.")
        time.sleep(0.3)
        dotsEffect(dots)


def sucessSecurity():

    toolbar_width = 60

    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    # return to start of line, after '['
    sys.stdout.write("\b" * (toolbar_width+1))

    for i in range(toolbar_width):
        time.sleep(0.07)  # do real work here
        # update the bar
        sys.stdout.write("•")
        sys.stdout.flush()

    sys.stdout.write("]\n")  # this ends the progress bar
    print("[D]|" + currentTime + "| 100% SUCCESS")
    time.sleep(0.5)
    print("acessing data.\n")


def breakingSecurity():
    z = 'disabling security'
    print('[^] ')
    dramEffect(z)
    print('\n\n')

    math1 = random.randint(0, 10)
    math2 = random.randint(0, 10)
    math3 = random.randint(1, 1000)
    math4 = random.randint(1, 1000)

    problem = "( " + str(math1) + " * " + str(math2) + \
        " ) / ( " + str(math1) + " + " + str(math2) + " )"

    calculate = math1*math2 / (math1 + math2)

    randon = random.randint(1, 20)

    attempts = 9

    print(problem)

    answerProblem1 = input('[A]: ')

    if float(answerProblem1) - 0.01 < calculate and float(answerProblem1) + 0.01 > calculate:
        print("\nSTEP 1 CONCLUDED. 1/2\n")
    else:
        print("[X]FAILED!!!\n")
        print("REBOOTING SECURITY")
        dramEffect(dots)
        breakingSecurity()

    print("There is a specific number between 1 and 20 that might used as PIN to unlock the system.")
    print("You have 9 attempts to try it, otherwise the system will restart.")

    while attempts < 10:
        number = int(input("Type your guess: "))
        attempts = attempts - 1
        str(print(attempts, "attempts left"))
        if number < randon:
            print("Too low. Try something higher!")
        if number > randon:
            print("Too high. Try something lower")
        if number == randon:
            break

    if number == randon:
        print("Well done! It took you only", attempts, "attempts")
        sucessSecurity()

    if number != randon:
        print("Sorry. All your attempts have been used up. The number was: ", randon)
        print("REBOOTING SECURITY")
        dramEffect(dots)
        breakingSecurity()


def ipRandom():
    first3 = random.randint(10, 999)
    second3 = random.randint(10, 999)
    # transform the variable into a str(numbers, in this case)
    third3 = random.randint(10, 999)
    ip = str(first3)+'.'+str(second3)+'.'+str(third3)
    return ip  # return the ip's value when called


def checkPing():
    print('\n[.]checking connection\n')
    time.sleep(0.5)
    ping = random.randint(5, 999)
    if ping < 100:
        time.sleep(0.5)
        print(ping, 'ms  || connection stable\n')
    elif ping < 400:
        time.sleep(0.5)
        print(ping, 'ms  || connection might be slow\n')
    else:
        time.sleep(0.5)
        print(ping, 'ms  || connection unstable\ntrying again\n')
        time.sleep(0.5)
        dotsEffect(dots)
        print('\n')
        checkPing()  # it calls the func again to find the value expected


def dotsEffect(af):  # GOT FROM STACKOVERFLOW
    for i in af.split():
        sys.stdout.write("{} ".format(i))
        sys.stdout.flush()
        seconds = ".6" + str(randrange(1, 5, 2))
        seconds = float(seconds)
        time.sleep(seconds)


def dramEffect(phrase):
    for i in phrase:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)


def loggs():
    askLogin = input('[\]Log In: ')
    time.sleep(1)
    if askLogin == 'masterChief':
        input('password: ')
    else:
        print('Invalid LogIn')
        time.sleep(1)
        quest = input('would you like to Sign Up? ')
        if quest.lower() == 'yes':
            global newLogIn
            global newPassword
            newLogIn = input('[\]Username: ')
            time.sleep(1)
            print('[*]username: avaliable')
            time.sleep(0.6)
            print('[*]username: saved as: ', newLogIn)
            time.sleep(0.6)
            newPassword = input('[*]Password: ')
            leng = (len(newPassword))
            print("[+] Lenght : ", leng)
            time.sleep(0.6)
            if leng < 8:
                print("[*]password: NOT STRONG")
                x = input('would you like to try again?')
                if x == 'yes':
                    global doublePassword
                    doublePassword = input('[*]new password: ')
                    doublePassword = newPassword
                else:
                    print('')
            elif leng >= 12:
                print("[*]password: VERY STRONG")
            else:
                print("[*]strebgth: STRONG")
            time.sleep(0.4)
            print("[*]saved succesful")
        else:
            loggs()  # Looping infinito da funcao// pode chamar ela no else que volta ao comeco


def chooseRandom(list):
    askSomethingRandom = random.randint(0, len(list))
    holder = list[askSomethingRandom]
    return holder


def ipConnect(choose):
    dotsEffect(dots)
    time.sleep(1)
    everyIp = 'Bank of America -- 902.232.542\nApple ------------ 724.553.878\nNetflix ---------- 174.289.111'
    bankAm = '\n$$Bank Of America | Class: Bank | Location : United States, Florida | main ip: 902.232.542 | Status: available'
    apple = '\n$$Apple | Class: Eletronics company | Location : United States, California | main ip: 724.553.878 | Status: available'
    netflix = '\n$$Netflix | Class: Streaming | Location : United States, California | main ip: 174.289.111 | Status: available'

    question = input(choose)
    for i in question:
        if 'list' in question:
            dramEffect(everyIp)
            print('\n')
            time.sleep(1)
            ipConnect('\n[$]-input the ip: ')
        else:
            print('')

    if doSomething('exit', question):
        print('[#]|' + currentTime + '| \nreturning...\n')
        time.sleep(1)

    elif doSomething('902.232.542', question):
        print(bankAm)
        breakingSecurity()
        bankFunction()

    elif doSomething('724.553.878', question):
        print(apple)
        breakingSecurity()

    elif doSomething('174.289.111', question):
        print(netflix)
        breakingSecurity()
    else:
        print('')


def vpnAcess():
    global _user
    cc = 'connecting to a random computer as host:\n'
    dramEffect(cc)
    dotsEffect(dots)
    _user = '\n[U]' + ipRandom() + ' || ' + str(random.randint(5, 999)) + 'ms' + ' || ' + chooseRandom(
        listContries) + ' || ' + chooseRandom(listFirstName) + ' ' + chooseRandom(listSecondName) + ' || ' + key_gen()
    print(_user + "\n")
    actualMachine = _user


def doSomething(key, ed):
    if key in ed:
        return True
    else:
        return False
    return key in ed


def askInfo(choice):
    enterInput = ""
    enterInput.lower()
    enterInput = input(choice)
    if doSomething('info', enterInput):
        info()

    elif doSomething('ping', enterInput):
        checkPing()

    elif doSomething('vpn', enterInput):
        vpnAcess()

    elif doSomething('ip', enterInput):
        ipConnect(
            '\n[!]- type "exit" to go back and "list" to see all the available ips\n[?]: ')
    elif doSomething('money', enterInput):
        _real = Sum * 5.20
        _euro = Sum / 1.18
        _pound = Sum / 1.38
        _yen = Sum / 0.0091
        print("You have: ", Sum, " $- DOLLARS")
        print("Converting the value: ")
        print(_real, "R$- REAIS")
        print("----------------------------")
        print(_euro, "€- EUROS")
        print("----------------------------")
        print(_pound, "£- POUNDS")
        print("----------------------------")
        print(_yen, "¥- YENS")

    elif doSomething('social media', enterInput):
        print('')

    else:
        print('[#].ERROR' + '.' + str(random.randint(111, 999)) + ' ')
        askInfo('[#]|' + currentTime + '|try again: ')
    askInfo('[*]|' + currentTime + '| : ')


def info():
    information = '=====================================================\n||"ip" -> show list of ip to invade or attack\n||"vpn" -> acess a new computer\n||"money" -> to acess your money account / money value\n||"social media" -> hack differents social media accounts\n||"ping" -> check your ping\n=====================================================\n'
    for z in information:
        sys.stdout.write(z)
        sys.stdout.flush()
        time.sleep(0.0003)


dots = '. . .'

# #randomNum = str(random.randint(100000000000000,
# #                               100000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
# #for i in randomNum:
# #    sys.stdout.write(randomNum)
# #    sys.stdout.flush()
# #    time.sleep(0.005)
# print('\n\n')
# #dotsEffect(dots)
# print('\n\n\n')
# #time.sleep(2)
# print('======================================')

# sis = '===||    INITIALIZING SYSTEM     ||===\n'
# dramEffect(sis)

# print('======================================\n\n\n')
# time.sleep(2)
# dotsEffect(dots)
# time.sleep(1)
# print('\n\n\n')
# #loggs()
# user_random = random.randint(1, 1000)
# user_code = sys.getsizeof(newLogIn) * user_random
# time.sleep(1)
# dotsEffect(dots)
# print('\n\n')
# print('[C]usercode: HaSsCd' + str(user_code))
# time.sleep(1.5)
# checkPing()
# time.sleep(2)
actualMachine = '[U]' + ipRandom() + ' || ' + str(random.randint(5, 999)) + 'ms' + ' || ' + \
    chooseRandom(listContries) + ' || ' + \
    chooseRandom(listFirstName) + ' ' + chooseRandom(listSecondName)
print('[-]your actual host: ' + actualMachine)
askInfo('[!]|' + currentTime + '.| type "info": ')
