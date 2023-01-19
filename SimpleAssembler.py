'''SIMPLE ASSEMBLER

Contributors :
    1. Divyansh Gaba
    2. Deepanshu Dabas
    3. Pulkit Nargotra

    GROUP 51 Section B'''
import math

register = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
}
registerDeclaration = {
    'R0': 0,
    'R1': 0,
    'R2': 0,
    'R3': 0,
    'R4': 0,
    'R5': 0,
    'R6': 0,
    'FLAGS': 0,
}
dict_repo = {
    "add": "10000",
    "sub": "10001",
    "mov": ["10010", "10011"],
    "ld": "10100",
    "st": "10101",
    "mul": "10110",
    "div": "10111",
    "rs": "11000",
    "ls": "11001",
    "xor": "11010",
    "or": "11011",
    "and": "11100",
    "not": "11101",
    "cmp": "11110",
    "jmp": "11111",
    "jlt": "01100",
    "jgt": "01101",
    "je": "01111",
    "hlt": "01010",
    "addf": "00000",
    "subf": "00001",
    "movf": "00010"
}
repo = {
    'typeA': {
        "add": "10000",
        "sub": "10001",
        "mul": "10110",
        "xor": "11010",
        "and": "11100",
        "or": "11011",
        "addf": "00000",
        "subf": "00001"
    },
    'typeB': {
        # "mov": "10010",
        "ls": "11001",
        "rs": "11000",
        "movf": "00010"
    },
    'typeC': {
        # "mov": "10011",
        "div": "10111",
        "not": "11101",
        "cmp": "11110",
    },
    'typeD': {
        "ld": "10100",
        "st": "10101",
    },
    'typeE': {
        "jmp": "11111",
        "jlt": "01100",
        "jgt": "01101",
        "je": "01111",
    },
    'typeF': {
        "hlt": "01010",
    }
}
variable = {}
variable_memory = {}


def checkOverflow(N):
    if float(N) > 31.5:
        return 1
    else:
        return 0


def checkUnderflow(N):
    if float(N) < 1:
        return 1
    else:
        return 0


def intigerToDecimal(N):
    s = ""
    N = int(N)
    while N > 0:
        L = N % 2
        N = N//2
        s += str(L)
    s = s[::-1]
    return s


def floatToBinary(N):
    s = ""
    N = float(N)
    con = 0
    L = float(N)
    l = []
    last = 0
    while N != float(0) and float(N) not in l:
        l.append(L)
        N = N*2
        N = str(N)
        temp = N[N.index('.')+1:]
        s += str(N[:N.index('.')])
        last = str(N[:N.index('.')])
        N = float(int(temp)*10**(-len(temp)))
        L = N

    # s=s[::-1]
    return s


def decimalToBinaryyy(n):
    index = n.index('.')
    a = n[:index]
    b = n[index+1:]
    an = intigerToDecimal(a)
    # print(an)
    b = "0."+b
    bn = floatToBinary(b)
    o = str(an)+"."+str(bn)
    p = ""
    exponent = o.index('.')-1
    I = int(math.log(int(a), 2))
    for i in range(1, len(o)):
        if o[i] == '.':
            continue
        else:
            p += o[i]

    y = p[::-1]
    for i in range(I):
        y += "0"
    y = y[::-1]
    for i in range(5-len(y)):
        y += "0"
    # o.pop(o.index('.'))
    if len(y) > 5:
        y = "11111"
    exp = intigerToDecimal(str(exponent))
    t = exp[::-1]
    for i in range(3-len(exp)):
        t += "0"
    t = t[::-1]
    if len(t) > 3:
        t = "111"

    return t+y


'''
def suboverFlown(N):
    if float(N)<1:
        return 1
    else:
        return 0
def add_f(reg1,reg2,reg3):
    if overFlown(reg1+reg2) == 0:
        reg3=decimalToBinaryyy(str(reg1+reg2))
    else:
        reg3="111111"
        
def sub_f(reg1,reg2,reg3):
    if suboverFlown(reg1-reg2)==0:
        reg3=decimalToBinaryyy(str(reg1-reg2))
    else:
        reg3="00000000"
def mov_f (reg1,imm):
    if overFlown(float(imm))==0 and subiverFlown == 0:
        reg1=imm
    else:
        if overFlown==1:
            reg1="11111111"
        else:
            reg1 = "00000000"
def intigerToDecimal(N):
    s = ""
    N = int(N)
    while N > 0:
        L = N % 2
        N = N//2
        s += str(L)
    s = s[::-1]
    return s
def floatToBinary(N):
    s=""
    N=float(N)
    con=0
    L=float(N)
    l=[]
    last=0
    while N!=float(0) and float(N) not in l:
        l.append(L)
        N=N*2
        N=str(N) 
        temp=N[N.index('.')+1:]
        s+=str(N[:N.index('.')])
        last=str(N[:N.index('.')])
        N=float(int(temp)*10**(-len(temp)))
        L=N
        
    #s=s[::-1]
    return s

def decimalToBinaryyy(n):
    index=n.index('.')
    a=n[:index]
    b=n[index+1:]
    an=intigerToDecimal(a)
    #print(an)
    b="0."+b
    bn=floatToBinary(b)
    o=str(an)+"."+str(bn)
    p=""
    exponent=o.index('.')-1+3
    for i in range(1,len(o)):
        if o[i]=='.':
            continue
        else:
            p+=o[i]
    y=p[::-1]
    for i in range(5-len(p)):
        y+="0"
    y=y[::-1]
    #o.pop(o.index('.'))
    if len(y)>5:
        y="11111"
    
    exp=intigerToDecimal(str(exponent))
    t=exp[::-1]
    for i in range(3-len(exp)):
        t+="0"
    t=t[::-1]
    if len(t) >3:
        t="111"
    
    return t+y

o=decimalToBinaryyy(n)
print(o)
'''


def flottobinary(value):
    s = ""
    a = int(value)
    b = a
    while(a > 0):
        s += str(a % 2)
        a //= 2
    s = s[::-1]
    count = 0
    for i in s:
        if i == '1':
            count += 1
            break
        count += 1
    s = s[count:]
    e = len(s)
    e = str(bin(e))
    e = e[2:]
    e = e.zfill(3)
    value = value-b
    i = 0
    while(value != 1 and i < 4):
        value *= 2
        if value < 1:
            s = s+'0'
        if value == 1:
            s += '1'
            break
        if value >= 1:
            s += '1'
            value -= 1
        i += 1
    if(value != 1):
        # setoverflowtrue
        pass
    for i in range(5-len(s)):
        s += '0'
    e = e+s
    return e[:8]


def checkLessThan(a, b):
    if a > b:
        return 0
    else:
        return 1


def checkEqual(a, b):
    if a == b:
        return 1
    else:
        return 0


def checkGreaterThan(a, b):
    if a > b:
        return 1
    else:
        return 0


def decimaltobinary(N):
    s = ""
    N = int(N)
    while N > 0:
        L = N % 2
        N = N//2
        s += str(L)
    s = s[::-1]
    return s.zfill(8)


# 220310151411
con = 0
errors = []
flags = {
    "clt": "0",
    "cgt": "0",
    "ceq": "0",
    "overflow": "0"
}


def error(i, statement):
    global errors
    errors.append("Error at line {}: Error: {} ".format(i, statement))


def pritErrors():
    for i in range(len(error)):
        print(errors[i])


'''def isOverflown(a, b, c, i):
    astr = str(bin(a))
    bstr = str(bin(b))
    cstr = str(bin(c))
    if(astr[0] == bstr[0] and cstr[0] != astr[0]):
        error(i+1, "Overflow")'''


def checkEightBit(a):
    if(a > 255):
        return False
    else:
        return True


labels = {}
isError = 0
Nerror = 0
x = 0
vari = 0


def storeFunctions():
    global isError
    global con
    global errors
    global Nerror
    global x
    global vari
    if isError == 0:
        for i in range(0, len(inputList)):
            if(len(inputList[i]) == 0):
                continue
            else:
                if(inputList[i][0] == 'var'):
                    if len(inputList[i]) != 2:
                        error(i+1, "Invalid statement")
                        isError = 1
                        Nerror += 1
                        break
                    if con == 1:
                        error(i+1, "Varibles not delared earlier")
                        isError = 1
                        Nerror += 1
                        break
                    if(inputList[i][1] in variable.keys()):
                        error(i+1, "variable already declared")
                        isError = 1
                        Nerror += 1
                        break

                    else:
                        variable[str(inputList[i][1])] = 0
                        variable_memory[str(inputList[i][1])] = i
                        # print(variable_memory[str(inputList[i][1])])
                        vari += 1
                if(inputList[i][0] == 'ld'):
                    if(len(inputList[i]) != 3):
                        isError = 1
                        Nerror += 1
                        con = 1
                        error(i+1, "Invalid")
                        break
                    if(inputList[i][1] not in register.keys()):
                        error(i+1, "Invalid")
                        isError = 1
                        Nerror += 1
                        con = 1
                        break

                    else:
                        try:
                            registerDeclaration[str(
                                inputList[i][1])] = variable[str(inputList[i][2])]
                        except:
                            error(i+1, "Variable not declared")
                            isError = 1
                            Nerror += 1
                            con = 1
                            break

                if(inputList[i][0] == 'st'):
                    if(len(inputList[i]) != 3):
                        isError = 1
                        Nerror += 1
                        con = 1
                        error(i+1, "Invalid")
                        break
                    if(inputList[i][1] not in register.keys()):
                        error(i+1, "Invalid")
                        isError = 1
                        Nerror += 1
                        con = 1
                        break
                    else:
                        try:
                            variable[str(inputList[i][2])] = registerDeclaration[str(
                                inputList[i][1])]
                        except:
                            isError = 1
                            Nerror += 1
                            con = 1
                            error(i+1, "Variable not declared")
                            break


def errorHandling(inputList, i, n):
    global con
    global isError
    global Nerror
    global vai
    if(inputList[i][0] not in dict_repo.keys() and inputList[i][0] != 'var'):
        error(i+1, "Invalid command")
        isError = 1
        Nerror += 1
    else:
        if inputList[i][0] == 'mov':
            o = str(inputList[i][2])
            if(len(inputList[i]) != 3):
                error(i+1, "invalid Syntax")
                isError = 1
                Nerror += 1
                con = 1
            if(o[0] != '$' and inputList[i][2] not in register.keys()):
                error(i+1, "No $ sign and invalid register")
                isError = 1
                Nerror += 1
                con = 1
            if o[0] == '$':
                if(checkEightBit(int(o[1:])) == False and u == 0):
                    error(i+1, "Not an 8 bit number")
                    isError = 1
                    Nerror += 1
                    con = 1

            '''if(checkEightBit(int(o[1:])) == False and u == 0):
                error(i+1, "Not an 8 bit number")
                isError = 1
                Nerror += 1
                con = 1'''

        if(inputList[i][0] in repo['typeA'].keys()):
            u = 0
            if(len(inputList[i]) != 4):
                isError = 1
                con = 1
                u = 1
                Nerror += 1
                error(i+1, "Invalid syntax")
            if(u == 0 and (inputList[i][1] not in register.keys() or inputList[i][2] not in register.keys() or inputList[i][3] not in register.keys())):
                error(i+1, "Invalid registers")
                isError = 1
                Nerror += 1
                con = 1
            if(u == 0 and (inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag' or inputList[i][3] == 'Flag')):
                error(i+1, "Incorrect use of Flag")
                isError = 1
                Nerror += 1
                con = 1
            '''if(isOverflown(inputList[i][1], inputList[i][2], inputList[i][3], i)):
                error(i+1, "overflow detected")
                isError = 1
                Nerror += 1
                con = 1'''
        if(inputList[i][0] in repo['typeB'].keys()):
            u = 0
            o = str(inputList[i][2])

            if(inputList[i][0] != "movf" and str(o[1:]).isnumeric() == False):
                isError = 1
                Nerror += 1
                u = 1
                con = 1
                error(i+1, "exected a decimal number")
            if(inputList[i][1] not in register.keys()):
                isError = 1
                Nerror += 1
                u = 1
                con = 1
            if (inputList[i][1] == "movf"):
                if ('.' not in inputList[i][2]):
                    isError = 1
                    Nerror += 1
                    u = 1
                    con = 1
                    error(i+1, "exected a floating number")
            if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                if(inputList[i][0] != 'mov'):
                    error(i+1, "Incorrect use of Flag")
                    isError = 1
                    Nerror += 1
                    con = 1
            if(o[0] != '$'):
                error(i+1, "No $ sign ")
                isError = 1
                Nerror += 1
                con = 1
                u = 1
            if(inputList[i][0] != "movf" and checkEightBit(int(o[1:])) == False and u == 0):
                error(i+1, "Not an 8 bit number")
                isError = 1
                Nerror += 1
                con = 1

        if(inputList[i][0] in repo['typeC'].keys()):
            if inputList[i][0] == 'mov':
                u = 0
                if(len(inputList[i]) != 3):
                    error(i+1, "Invalid syntax")
                    isError = 1
                    con = 1
                    Nerror += 1
                if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                    error(i+1, "Incorrect use of Flag")
                    isError = 1
                    Nerror += 1
                    con = 1
                if(inputList[i][1] not in register.keys()):
                    error(i+1, "Invalid Register")
                    isError = 1
                    con = 1
                    Nerror += 1
                if(o[0] != '$'):
                    error(i+1, "No $ sign ")
                    isError = 1
                    Nerror += 1
                    con = 1
                    u = 1
                    error(i+1, "Invalid register")
                if(u == 0 and checkEightBit(int(o[1:])) == False):
                    error(i+1, "Not an 8 bit number")
                    isError = 1
                    Nerror += 1
                    con = 1
            else:
                if(len(inputList[i]) != 3):
                    error(i+1, "Invalid syntax")
                    isError = 1
                    con = 1
                    Nerror += 1
                if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                    error(i+1, "Incorrect use of Flag")
                    isError = 1
                    Nerror += 1
                    con = 1
                if(inputList[i][1] not in register.keys()):
                    error(i+1, "Invalid Register")
                    isError = 1
                    con = 1
                    Nerror += 1
            '''if(isOverflown(inputList[i][1], inputList[i][2], i)):
                error(i+1, "overflow detected")
                isError = 1
                Nerror += 1
                con = 1'''
        if(inputList[i][0] in repo['typeD'].keys()):
            if(len(inputList[i]) != 3):
                isError = 1
                con = 1
                Nerror += 1
                error(i+1, "Invalid syntax")
            if(inputList[i][1] == 'Flag' or inputList[i][2] == 'Flag'):
                error(i+1, "Incorrect use of Flag")
                isError = 1
                Nerror += 1
                con = 1

            '''if(checkMemory(inputList[i][2]) == False):
                isError = 1
                error(i+1, "Invalid")
                Nerror += 1'''
        if(inputList[i][0] in repo['typeE'].keys()):

            if(len(inputList[i]) != 2):
                isError = 1
                con = 1
                Nerror += 1
                error(i+1, "Invalid syntax")
            if(inputList[i][1] == 'Flag'):
                error(i+1, "Incorrect use of Flag")
                isError = 1
                Nerror += 1
                con = 1
            if(inputList[i][1] not in variable and inputList[i][1] not in labels):
                isError = 1
                Nerror += 1
                con = 1
                error(i+1, "Invalid Memory Address")
            '''if(checkMemory(inputList[i][2]) == False):
                isError = 1
                Nerror += 1
                error(i+1, "Invalid")'''
        if(inputList[i][0] in repo['typeF'].keys()):
            if(len(inputList[i]) != 1):
                isError = 1
                Nerror += 1
                con = 1
                error(i+1, "Invalid syntax")
            if(i != n-1):
                error(i+1, "hlt not as last")
                Nerror += 1
                isError = 1
                con = 1


n = 0


def printBinary(l, n, o, l4):
    global vari
    global vai
    if (l[0] == "add"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[2])+registerDeclaration.get(l[1])
        if checkEightBit(registerDeclaration.get(l[3])) == False:
            flags.get["Overflow"] = "1"
            print("Error at line "+str(o)+": Error: Overflow")
            return 1
    if l[0] == "addf":
        w = str(float(registerDeclaration.get(
            l[1]))+float(registerDeclaration.get(l[2])))
        if (checkOverflow(w) == 0):
            registerDeclaration[l[3]] = float(registerDeclaration.get(
                l[1]))+float(registerDeclaration.get(l[2]))
        else:
            print("Error at line "+str(o)+": Error: Overflow")

            flags["Overflow"] = "1"
            return 1
    if l[0] == "subf":
        w = str(float(registerDeclaration.get(
            l[1]))-float(registerDeclaration.get(l[2])))
        if (checkUnderflow(w) == 0):
            registerDeclaration[l[3]] = float(registerDeclaration.get(
                l[1]))-float(registerDeclaration.get(l[2]))
        else:
            print("Error at line "+str(o)+": Error: Underflow")
            flags["Overflow"] = "1"
            return 1
    if (l[0] == "sub"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1])-registerDeclaration.get(l[2])
        if checkEightBit(registerDeclaration.get(l[3])) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            flags.get["Overflow"] = "1"
            return 1
    if l[0] == "movf":
        j = str(l[2][1:])
        if checkOverflow(str(j)) == 0:
            registerDeclaration[l[1]] = str(j)
        else:
            print("Error at line "+str(o)+": Error: Overflow")
            flags["Overflow"] = "1"
            return 1
    if (l[0] == "mul"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1])*registerDeclaration.get(l[2])
        if checkEightBit(registerDeclaration.get(l[3])) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            flags.get["Overflow"] = "1"
            return 1
    try:
        if l[0] == "div":
            registerDeclaration["R0"] = int(
                registerDeclaration[l[1]]//registerDeclaration[l[2]])
            registerDeclaration["R1"] = int(
                registerDeclaration[l[1]] % registerDeclaration[l[2]])
            if checkEightBit(registerDeclaration.get("R0")) == False:
                print("Error at line "+str(o)+": Error: Overflow")
                flags.get["Overflow"] = "1"
                return 1
            if checkEightBit(registerDeclaration.get("R1")) == False:
                print("Error at line "+str(o)+": Error: Overflow")
                flags.get["Overflow"] = "1"
                return 1
    except ZeroDivisionError:
        print("Error at line "+str(o)+": Error: ZeroDivisionError")
        return 1
    if (l[0] == "xor"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1]) ^ registerDeclaration.get(l[2])
        if checkEightBit(registerDeclaration.get(l[3])) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            flags.get["Overflow"] = "1"
            return 1
    if (l[0] == "or"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1]) | registerDeclaration.get(l[2])
        if checkEightBit(registerDeclaration.get(l[3])) == False:
            #print("Error at line "+str(o)+": Error: Overflow")
            flags.get["Overflow"] = "1"
            return 1
    if (l[0] == "and"):
        registerDeclaration[l[3]] = registerDeclaration.get(
            l[1]) & registerDeclaration.get(l[2])
        if checkEightBit(registerDeclaration.get(l[3])) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            flags.get["Overflow"] = "1"
            return 1
    if (l[0] == "not"):
        registerDeclaration[l[2]] = ~registerDeclaration.get(l[1])
        if checkEightBit(registerDeclaration.get(l[2])) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            flags.get["Overflow"] = "1"
            return 1
    if (l[0] in repo['typeA'].keys()):
        l4.append(dict_repo.get(l[0])+"00"+register.get(l[1]) +
                  register.get(l[2])+register.get(l[3]))
    if (l[0] == "not" or l[0] == "cmp" or l[0] == "div"):
        l4.append(dict_repo.get(l[0])+"00000" +
                  register.get(l[1])+register.get(l[2]))
    if (l[0] == "movf"):
        o = str(l[2][1:])
        l4.append(dict_repo.get(l[0]) +
                  register.get(l[1]) + flottobinary(float(o)))
    if (l[0] == "ld" or l[0] == "st"):
        l4.append(dict_repo.get(l[0])+register.get(l[1]) +
                  decimaltobinary(n-blank-vai+variable_memory[str(l[2])]))  # -3
    if (l[0] == "je" or l[0] == "jgt" or l[0] == "jlt" or l[0] == "jmp"):
        if l[1] in labels.keys():
            l4.append(dict_repo.get(l[0])+"000"+labels.get(l[1]))
        elif l[1] in variable.keys():
            l4.append(dict_repo.get(l[0])+"000"+variable.get(l[1]))
    if (l[0] == "rs" or l[0] == "ls"):
        l4.append(dict_repo.get(l[0])+register.get(l[1])+decimaltobinary(l[2]))
    if (l[0] == "mov" and l[2] not in register):
        s = str(l[2])
        s = s[1:]
        registerDeclaration[l[1]] = int(s)
        if checkEightBit(int(s)) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            return 1
        l4.append(dict_repo.get(l[0])[0] +
                  register.get(l[1]) + decimaltobinary(s))
    elif(l[0] == "mov" and l[2] in register):
        registerDeclaration[l[2]] = registerDeclaration.get(l[1])
        if checkEightBit(registerDeclaration.get(l[2])) == False:
            print("Error at line "+str(o)+": Error: Overflow")
            return 1
        l4.append(dict_repo.get(l[0])[1]+"00000" +
                  register.get(l[1])+register.get(l[2]))

    if (l[0] == "hlt"):
        l4.append(dict_repo.get(l[0])+"00000000000")
    return 0


inputList = []
totalCommmands = 0
'''while(n > 0):
    try:
        temp = [i for i in input().split()]
        if(':' in temp[0]):
            inputList.append(temp[1:])
            y = temp[0].rstrip(':')
            labels[str(y)] = decimaltobinary(n-t)
        else:
            inputList.append(temp)

        totalCommmands += 1
        n = n-1
    except:
        break'''

vai = 0
blank = 0
while True:
    try:
        temp = [i for i in input().split()]
        if temp != [] and temp[0] == 'var':
            vai += 1
        if temp == []:
            inputList.append([])
            blank += 1
        elif(':' in temp[0]):
            inputList.append(temp[1:])
            y = temp[0].rstrip(':')
            labels[str(y)] = decimaltobinary(n-vai-blank)
            variable[str(y)] = decimaltobinary(n-vai-blank)
        else:
            inputList.append(temp)
        totalCommmands += 1
        n += 1
    except:
        break
t = n

storeFunctions()
for i in range(totalCommmands):
    if(len(inputList[i]) == 0):
        continue
    errorHandling(inputList, i, totalCommmands)

if(inputList[n-1] != []):
    if inputList[n-1][0] != 'hlt':
        error(i+1, "no halt")
        isError = 1
else:
    if inputList[n-2][0] != 'hlt':
        error(i+1, "no halt")
        isError = 1

if(isError == 0):
    k = 1
    div = 0
    l4 = []
    for i in inputList:
        if(i == []):
            k += 1
            continue
        div = printBinary(i, t, k, l4)
        if div == 1:
            break
        k += 1
    if div == 1:
        pass
    else:
        for i in l4:
            print(i)
else:
    for i in errors:
        print(i)
