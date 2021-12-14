class gates:
    def notgate(A):
        return not A
    def orgate(A, B):
        if A or B:
            return True
        else:
            return False
    def andgate(A, B):
        if A and B:
            return True
        else:
            return False
    def xorgate(A, B):
        if A or B:
            if not(A and B) and not((not A) and (not B)):
                return True
            else:
                return False
        else:
            return False
    def nandgate(A, B):
        if A and B:
            return False
        else:
            return True
    def norgate(A,B):
        if A or B:
            return False
        else:
            return True


def operations(op, A, B):
    switch={
       'not': gates.notgate(A),
       'or': gates.orgate(A, B),
       'and': gates.andgate(A, B),
       'xor': gates.xorgate(A, B),
       'nand': gates.nandgate(A, B),
       'nor': gates.norgate(A, B)
    }
    return switch.get(op)

def converttoboolean(a):
    try:
        a = int(a)
        if a == 1:
            a = True
        else:
            a = False
    except ValueError:
        if a == "true":
            a = True
        elif a == "false":
            a = False
    return a


gateselected = input("Which logic gate do you wish to use?: ").lower()
A = input("Specify A:").lower()
B = input("Specify B:").lower()
A = converttoboolean(A)
B = converttoboolean(B)

result = operations(gateselected, A, B)
if result == True:
    print(1)
else:
    print(0)
