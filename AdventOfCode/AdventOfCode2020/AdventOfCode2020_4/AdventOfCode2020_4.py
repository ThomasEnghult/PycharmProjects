import re

source = open("input.txt")
source = source.read()
source = source.split("\n\n", -1)

totalvalid = 0

for x in source:

    valid = 1
    '''print("---")
    print(x)'''
    checklist = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for keyword in checklist:
        if -1 == x.find(keyword):
            '''print("missing " + keyword)'''
            valid = 0
            break
    totalvalid += valid
'''print(totalvalid)'''

'''Part 2'''

def presentCheck(passport:str):
    checklist = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for keyword in checklist:
        if -1 == x.find(keyword):
            return 0
    return 1

def validCheck(passport:dict):

    birthyear = int(passport.get('byr'))
    if not 1920 <= birthyear <= 2002:
        print("wrong birth year: " + str(birthyear))
        return 0

    issueyear = int(passport.get('iyr'))
    if not 2010 <= issueyear <= 2020:
        print("wrong issue year: " + str(issueyear))
        return 0

    expirationyear = int(passport.get('eyr'))
    if not 2020 <= expirationyear <= 2030:
        print("wrong expiration year: " + str(expirationyear))
        return 0

    height = passport.get('hgt')
    if height[-2:] == 'cm':
        validheight = int(height[:-2])
        if not 150 <= validheight <= 193:
            print("wrong height in cm: " + str(height))
            return 0
    elif height[-2:] == "in":
        validheight = int(height[:-2])
        if not 59 <= validheight <= 76:
            print("wrong height in in: " + str(height))
            return 0
    else:
        print("invalid height no unit: " + str(height))
        return 0

    haircolor = passport.get('hcl')
    regex = "^#([a-f0-9]{6})$"
    test = re.compile(regex)
    if not re.search(test, haircolor):
        print("wrong haircolor: " + haircolor)
        return 0

    validcolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    eyecolor = passport.get('ecl')
    if not validcolors.count(eyecolor):
        print("wrong eyecolor: " + eyecolor)
        return 0

    passID = passport.get('pid')
    regex = "([0-9]{9})$"
    test = re.compile(regex)
    if not re.search(test, passID):
        print("wrong pass ID: " + passID)
        return 0
    elif not len(passID) == 9:
        print("too long pass ID: " + passID)
        return 0
    #print("------")
    #print(passport)
    #print("Your passport is valid!")
    return 1

presValid = 0
present = 0

for x in source:
    passport = x
    if presentCheck(passport):
        present += 1
        passport = passport.replace("\n"," ")
        passport = passport.split()
        passport = [key.split(":") for key in passport]
        passport = dict(passport)
        if validCheck(passport):
            presValid +=1

print("Total Valid and present passports:")
print(presValid)
print("Total present:")
print(present)




'''
if -1 == x.find("byr"):
    print("missing byr")
    continue
if -1 == x.find("iyr"):
    print("missing iyr")
    continue
if -1 == x.find("eyr"):
    print("missing eyr")
    continue
if -1 == x.find("hgt"):
    print("missing hgt")
    continue
if -1 == x.find("hcl"):
    print("missing hcl")
    continue
if -1 == x.find("ecl"):
    print("missing ecl")
    continue
if -1 == x.find("pid"):
    print("missing pid")
    continue
print("Valid")


valid += 1
'''