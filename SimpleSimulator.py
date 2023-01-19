import matplotlib.pyplot as plt
import numpy as np
cycle = 0
programcounter = 0
numberofinstructions = 0
memory = []
programlist = []
cyclelist = []

for i in range(256):
    memory.append('0000000000000000')
register_dict = {'000': '0000000000000000', '101': '0000000000000000', '001': '0000000000000000', '011': '0000000000000000',
                 '010': '0000000000000000', '100': '0000000000000000', '111': {'V': '0', 'L': '0', 'G': '0', 'E': '0'}, '110': '0000000000000000'}


def binarytofloat(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r1 = value[0:3]
    r1 = r1[::-1]
    r2 = value[3:8]
    power = 0
    result = 0
    overflow = 0
    for i in r1:
        result += int(i)*2**power
        power += 1
    if (result >= 5):
        overflow = 1
    else:
        point = 0
        r1 = r2[0:result]
        r2 = r2[result:]
        r1 = '1'+r1
        r1 = r1[::-1]
        power = 0
        result = 0
        for i in r1:
            result += int(i)*2**power
            power += 1
        power = 1
        for i in r2:
            point += int(i)/2**power
            power += 1
        result += point
        return result, overflow


def flottobinary(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    overflow = 0
    s = ""
    a = int(value)
    b = a
    if(value > 31.5):
        overflow = 1
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
        overflow = 1
    for i in range(5-len(s)):
        s += '0'
    e = e+s
    return e[0:8], overflow


def reset():
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    register_dict['111']['V'] = register_dict['111']['L'] = register_dict['111']['G'] = register_dict['111']['E'] = '0'


def hlt(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    reset()
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (numberofinstructions+1, 1)


def add_f(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    r1 = register_dict.get(r1)
    r2 = register_dict.get(r2)
    r1 = r1[8:16]
    r2 = r2[8:16]
    r1, overflow = binarytofloat(r1)
    r2, overflow = binarytofloat(r2)
    result, overflow = flottobinary(r1+r2)
    register_dict[r3] = result.zfill(16)
    programcounter_in_binary = bin(programcounter)[2:]
    if(overflow):
        register_dict['111']['V'] = '1'
        register_dict[r3] = '0000000011111111'
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def sub_f(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    r1 = register_dict.get(r1)
    r2 = register_dict.get(r2)
    r1 = r1[8:16]
    r2 = r2[8:16]
    r1, overflow = binarytofloat(r1)
    r2, overflow = binarytofloat(r2)
    result = r1-r2
    if(result < 0):
        overflow = 1
        register_dict[r3] = '0000000000000000'
        register_dict['111']['V'] = '1'
    else:
        result, overflow = flottobinary(result)
        register_dict[r3] = result.zfill(16)
    if(overflow):
        register_dict['111']['V'] = '1'
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def mov_f(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r1 = value[5:8]
    Imm = value[8:]
    register_dict[r1] = Imm.zfill(16)  # immediate stored in Imm
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def subtraction(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    diff = int(register_dict[r1], 2) - int(register_dict[r2], 2)
    if diff < 0:
        register_dict[r3] = '0000000000000000'
        register_dict['111']['V'] = '1'
    elif diff > pow(2, 16) - 1:
        register_dict[r3] = bin(diff)[-16:]
        register_dict['111']['V'] = '1'
    else:
        rvalue = bin(diff)[2:]
        register_dict[r3] = rvalue.zfill(16)
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def addition(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    output = int(register_dict[r1], 2)
    output += int(register_dict[r2], 2)
    if output <= pow(2, 16) - 1:
        rvalue = bin(output)[2:]
        register_dict[r3] = rvalue.zfill(16)
    else:
        register_dict[r3] = bin(output)[-16:]
        register_dict['111']['V'] = '1'
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def multiply(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    Mul = int(register_dict[r1], 2)
    Mul *= int(register_dict[r2], 2)
    if Mul <= pow(2, 16) - 1:
        rvalue = bin(Mul)[2:]
        register_dict[r3] = rvalue.zfill(16)
    else:
        register_dict['111']['V'] = '1'  # overflow bit set if overflow occurs
        register_dict[r3] = bin(Mul)[-16:]
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def divide(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    reset()
    r4 = value[13:16]
    r3 = value[10:13]
    r0 = int(int(register_dict[r3], 2)/int(register_dict[r4], 2))
    r0 = bin(r0)[2:]
    register_dict['000'] = r0.zfill(16)
    res1 = int(register_dict[r3], 2)
    res2 = int(register_dict['000'], 2)*int(register_dict[r4], 2)
    r1 = bin(res1-res2)[2:]
    register_dict['001'] = r1.zfill(16)
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def leftshift(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    reset()
    global programlist
    global cyclelist
    r1 = value[5:8]
    temp_shifter = value[8:]
    shifter = int(temp_shifter, 2)
    res1 = register_dict[r1]
    res2 = '0'*shifter
    register_dict[r1] = res1[shifter:16] + res2
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def exclusiveor(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    rvalue = ''
    i = 0
    while(i < len(register_dict[r1])):
        if((register_dict[r1][i]) != register_dict[r2][i]):
            rvalue += '1'
        else:
            rvalue += '0'
        i += 1
    programcounter_in_binary = bin(programcounter)[2:]
    register_dict[r3] = rvalue
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def andfunc(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    rvalue = ''
    for i in range(len(register_dict[r2])):
        if((register_dict[r1][i]) != 1 or register_dict[r2][i] != 1):
            rvalue += '0'
            i += 1
        else:
            rvalue += '1'
            i += 1
    programcounter_in_binary = bin(programcounter)[2:]
    register_dict[r3] = rvalue
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def moveimmediate(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    reset()
    r1 = value[5:8]
    Imm = value[8:]
    register_dict[r1] = Imm.zfill(16)  # immediate stored in Imm
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def orfunc(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r3 = value[13:]
    r2 = value[10:13]
    r1 = value[7:10]
    reset()
    rvalue = ''
    for i in range(len(register_dict[r2])):
        if((register_dict[r1][i]) != 1 and register_dict[r2][i] != 1):
            rvalue += '0'
            i += 1
        else:
            rvalue += '1'
            i += 1
    programcounter_in_binary = bin(programcounter)[2:]
    register_dict[r3] = rvalue
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def rightshift(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    reset()
    T = value[5:5+3]
    r1 = T
    shifterb = value[8:]
    shifter = int(shifterb, 2)
    temp_reg = '0'*shifter
    temp_reg2 = register_dict[r1][0:16-shifter]
    register_dict[r1] = temp_reg + temp_reg2
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def movetoregister(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r2 = value[13:16]
    r1 = value[10:13]
    if r2 == '111':
        register_dict[r2] = '000000000000' + register_dict['111']['V'] + \
            register_dict['111']['L'] + \
            register_dict['111']['G'] + register_dict['111']['E']
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    else:
        reset()
        register_dict[r2] = register_dict[r1]
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def compare(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r2 = value[13:16]
    t11 = int(register_dict[r2], 2)
    r1 = value[10:13]
    t1 = int(register_dict[r1], 2)
    reset()
    if(t11 == t1):
        register_dict['111']['E'] = '1'
    elif t11 > t1:
        register_dict['111']['L'] = '1'
    else:
        register_dict['111']['G'] = '1'
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def invert(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    r2 = value[13:16]
    r1 = value[10:13]
    reset()
    rvalue = ''
    lgr = len(register_dict[r2])
    for i in range(lgr):
        if(not register_dict[r2][i]):
            rvalue += '1'
        else:
            rvalue += '0'
    register_dict[r2] = rvalue.zfill(16)
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0)


def store(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    reset()
    a1 = int(value[8:], 2)
    memory[a1] = register_dict[value[5:8]]
    programcounter_in_binary = bin(programcounter)[2:]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0, a1)


def load(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    reset()
    programcounter_in_binary = bin(programcounter)[2:]
    register_dict[value[5:8]] = memory[int(value[8:], 2)]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (1, 0, int(value[8:], 2))


def UnconditionalJump(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    programcounter_in_binary = bin(programcounter)[2:]
    reset()
    address = value[8:16]
    print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
          register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
    return (int(address, 2), 1)


def JumpIfGreaterThan(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    if register_dict['111']['G'] != '1':
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
        return (1, 0)
    else:
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
        return (int(value[8:16], 2), 1)


def JumpIfEqual(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    if register_dict['111']['E'] != '1':
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
        return (1, 0)
    else:
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
        return (int(value[8:16], 2), 1)


def JumpIfLessThan(value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    if register_dict['111']['L'] != '1':
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
        return (1, 0)
    else:
        reset()
        programcounter_in_binary = bin(programcounter)[2:]
        print(programcounter_in_binary.zfill(8), register_dict['000'], register_dict['001'], register_dict['010'], register_dict['011'], register_dict['100'], register_dict['101'],
              register_dict['110'], '000000000000' + register_dict['111']['V'] + register_dict['111']['L'] + register_dict['111']['G'] + register_dict['111']['E'])
        return (int(value[8:16], 2), 1)


def functioncall(opcode, value):
    global cycle
    global programcounter
    global numberofinstructions
    global memory
    global programlist
    global cyclelist
    programlist.append(programcounter)
    if opcode == '10000':
        temp = addition(value)
        cycle += 1
        return temp
    if opcode == '10001':
        temp = subtraction(value)
        cycle += 1
        return temp
    if opcode == '10010':
        temp = moveimmediate(value)
        cycle += 1
        return temp
    if opcode == '10011':
        temp = movetoregister(value)
        cycle += 1
        return temp
    if opcode == '10100':
        temp = load(value)
        programlist.append(temp[2])
        cyclelist.append(cycle)
        cycle += 1
        return temp
    if opcode == '10101':
        temp = store(value)
        programlist.append(temp[2])
        cyclelist.append(cycle)
        cycle += 1
        return temp
    if opcode == '10110':
        temp = multiply(value)
        cycle += 1
        return temp
    if opcode == '10111':
        temp = divide(value)
        cycle += 1
        return temp
    if opcode == '11000':
        temp = rightshift(value)
        cycle += 1
        return temp
    if opcode == '11001':
        temp = leftshift(value)
        cycle += 1
        return temp
    if opcode == '11010':
        temp = exclusiveor(value)
        cycle += 1
        return temp
    if opcode == '11011':
        temp = orfunc(value)
        cycle += 1
        return temp
    if opcode == '11100':
        temp = andfunc(value)
        cycle += 1
        return temp
    if opcode == '11101':
        temp = invert(value)
        cycle += 1
        return temp
    if opcode == '11110':
        temp = compare(value)
        cycle += 1
        return temp
    if opcode == '11111':
        temp = UnconditionalJump(value)
        cycle += 1
        return temp
    if opcode == '01100':
        temp = JumpIfLessThan(value)
        cycle += 1
        return temp
    if opcode == '01101':
        temp = JumpIfGreaterThan(value)
        cycle += 1
        return temp
    if opcode == '01111':
        temp = JumpIfEqual(value)
        cycle += 1
        return temp
    if opcode == '01010':
        temp = hlt(value)
        cycle += 1
        return temp
    if opcode == '00000':
        temp = add_f(value)
        cycle += 1
        return temp
    if opcode == '00001':
        temp = sub_f(value)
        cycle += 1
        return temp
    if opcode == '00010':
        temp = mov_f(value)
        cycle += 1
        return temp


while True:
    try:
        temporary = input()
        temporary = temporary.strip()
        memory[numberofinstructions] = temporary
        numberofinstructions += 1
    except:
        break
while(programcounter < numberofinstructions):
    value = memory[programcounter]
    opcode = value[0:5]
    cyclelist.append(cycle)
    func = functioncall(opcode, value)
    if func[1] == 1:
        programcounter = func[0]
    else:
        programcounter += 1
for i in memory:
    s = str(i)
    print(s)
xpoints = np.array(cyclelist)
ypoints = np.array(programlist)
plt.scatter(xpoints, ypoints)
plt.ylabel('Memory address->')
plt.xlabel('Cycle Number->')
plt.title('Cycle Number Vs Memory address Graph')
plt.show()
plt.savefig("C:/Users/Deepanshu Dabas/Desktop/graph1.png")