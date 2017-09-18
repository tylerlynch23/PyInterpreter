from sys import exit

reserved = ["push", "pop", "add", "sub", "mul", "div", "rem", "neg", "swap", "and", "or", "not", "equal", "lessThan",
            "bind", "if", "let", "end", "quit", "fun"]
closure_dict = {}

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)

class Scope():
    def __init__(self):
        self.stack = Stack()
        self.dictionary = {}

class Closure():
    def __init__(self):
        self.scope = Scope()
        self.codeList = []
        self.paramList = []


def is_number(s):
    try:
        inNumberint = int(s)
        return True
    except ValueError:
        pass

    try:
        inNumberint = float(s)
        return True
    except(ValueError):
        pass




def negit(scope):
    if scope.stack.size() > 0:
        val = scope.stack.peek()
        if is_number(val):
            val = int(val)
            val = val * -1
            scope.stack.pop()
            scope.stack.push(str(val))
        elif isName(val):
            if is_number(str(scope.dictionary.get(val))):
                val2 = scope.dictionary[val]
                val3 = int(val2)
                val3 = val3 * -1
                scope.stack.pop()
                scope.stack.push(str(val3))
            else: scope.stack.push(":error:")
        else: scope.stack.push(":error:")
    else: scope.stack.push(":error:")
    return scope



def subit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if is_number(var1) and is_number(var2):
            var3 = int(var2) - int(var1)
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(str(var3))
        elif isName(str(var1)) or isName(str(var2)):
            if isName(str(var1)) and isName(str(var2)):
                if is_number(str(scope.dictionary.get(var2))) and is_number(str(scope.dictionary.get(var1))):
                    hmm1 = int(scope.dictionary[var2])
                    hmm2 = int(scope.dictionary[var1])
                    val4 = hmm1 - hmm2
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            elif isName(var1) and is_number(var2):
                if is_number(str(scope.dictionary.get(var1))):
                    hmm = int(scope.dictionary[var1])
                    val4 = int(var2) - hmm
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            elif is_number(var1) and isName(var2):
                if is_number(str(scope.dictionary.get(var2))):
                    hmm = int(scope.dictionary[var2])
                    val4 = hmm - int(var1)
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
        elif scope.stack.isEmpty():
            scope.stack.push(":error:")
        else: scope.stack.push(":error:")
    else: scope.stack.push(":error:")
    return scope

def addit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if is_number(var1) and is_number(var2):
            var3 = int(var1) + int(var2)
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(str(var3))
        elif isName(var1) or isName(var2):
            if isName(str(var1)) and isName(str(var2)):
                if is_number(str(scope.dictionary.get(var2))) and is_number(str(scope.dictionary.get(var1))):
                    hmm1 = int(scope.dictionary[var2])
                    hmm2 = int(scope.dictionary[var1])
                    val4 = hmm1 + hmm2
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            elif isName(var1) and is_number(var2):
                if is_number(str(scope.dictionary.get(var1))):
                    hmm = int(scope.dictionary[var1])
                    val4 = int(var2) + hmm
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            elif is_number(str(var1)) and isName(var2):
                temp = (scope.dictionary.get(var2))
                if is_number(str(temp)):
                    hmm = int(scope.dictionary[var2])
                    val4 = hmm + int(var1)
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        elif scope.stack.isEmpty():
            scope.stack.push(":error:")
        else: scope.stack.push(":error:")
    else: scope.stack.push(":error:")
    return scope

def mulit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if is_number(var1) and is_number(var2):
            var3 = int(var1) * int(var2)
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(str(var3))
        elif isName(var1) or isName(var2):
            if isName(var1) and isName(var2):
                if is_number(str(scope.dictionary.get(var2))) and is_number(str(scope.dictionary.get(var1))):
                    hmm1 = int(scope.dictionary[var2])
                    hmm2 = int(scope.dictionary[var1])
                    val4 = hmm1 * hmm2
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            elif isName(var1) and is_number(var2):
                if is_number(str(scope.dictionary.get(var1))):
                    hmm = int(scope.dictionary[var1])
                    val4 = int(var2) * hmm
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            elif is_number(var1) and isName(var2):
                if is_number(str(scope.dictionary.get(var2))):
                    hmm = int(scope.dictionary[var2])
                    val4 = hmm * int(var1)
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(val4)
                else:
                    scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        elif scope.stack.isEmpty():
            scope.stack.push(":error:")
        else: scope.stack.push(":error:")
    else: scope.stack.push(":error:")
    return scope

def divit(scope):
    if scope.stack.size() > 1:
        varY = scope.stack.peek()
        #checks if varY is a number
        if is_number(varY):
            if int(varY) == 0:
                scope.stack.push(":error:")
                return scope
            scope.stack.pop()
            varX = scope.stack.peek()
            scope.stack.push(varY)
            if is_number(varX):
                var3 = int(varX) // int(varY)
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(str(var3))
            if isName(str(varX)):
                if is_number(str(scope.dictionary.get(varX))):
                    hmm = int(scope.dictionary[varX])
                    hmm2 = hmm//int(varY)
                    if not hmm == 0:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(hmm2)
                    else:
                        scope.stack.push(":error:")
                else:
                    scope.stack.push(":error:")
        #checks if varY is a name
        elif isName(varY):
            if is_number(str(scope.dictionary.get(varY))):
                scope.stack.pop()
                varX = scope.stack.peek()
                scope.stack.push(varY)
                hmm = int(scope.dictionary[varY])
                if hmm == 0:
                    scope.stack.push(":error:")
                    return scope
                elif is_number(varX):
                    var3 = int(varX) // hmm
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(str(var3))
                elif isName(varX):
                    if is_number(str(scope.dictionary.get(varX))):
                        hmm3 = int(scope.dictionary[varX])
                        if not hmm == 0:
                                hmm2 = hmm3 // hmm
                                scope.stack.pop()
                                scope.stack.pop()
                                scope.stack.push(hmm2)
                        else:
                            scope.stack.push(":error:")
                    else:
                        scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        else:
            scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope






def remit(scope):
    if scope.stack.size() > 1:
        varY = scope.stack.peek()
        # checks if varY is a number
        if is_number(varY):
            if int(varY) == 0:
                scope.stack.push(":error:")
                return scope
            scope.stack.pop()
            varX = scope.stack.peek()
            scope.stack.push(varY)
            if is_number(varX):
                var3 = int(varX) % int(varY)
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(str(var3))
            if isName(varX):
                if is_number(str(scope.dictionary.get(varX))):
                    hmm = int(scope.dictionary[varX])
                    hmm2 = hmm % int(varY)
                    if not hmm == 0:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(hmm2)
                    else:
                        scope.stack.push(":error:")
                else:
                    scope.stack.push(":error:")
        # checks if varY is a name
        elif isName(varY):
            if is_number(str(scope.dictionary.get(varY))):
                scope.stack.pop()
                varX = scope.stack.peek()
                scope.stack.push(varY)
                hmm = int(scope.dictionary[varY])
                if hmm == 0:
                    scope.stack.push(":error:")
                    return scope
                elif is_number(varX):
                    var3 = int(varX) % hmm
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(str(var3))
                elif isName(varX):
                    if is_number(str(scope.dictionary.get(varX))):
                        hmm3 = int(scope.dictionary[varX])
                        if not hmm == 0:
                            hmm2 = hmm3 % hmm
                            scope.stack.pop()
                            scope.stack.pop()
                            scope.stack.push(hmm2)
                        else:
                            scope.stack.push(":error:")
                    else:
                        scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        else:
            scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope


def andit(scope):
    if (scope.stack.size() > 1):
        var1 = scope.stack.peek()
        if(var1 != ":true:" and var1 != ":false:"):
            if not isName(var1):
                scope.stack.push(":error:")
                return scope
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if(var2 != ":true:" and var2 != ":false:"):
            if not isName(var2):
                scope.stack.push(":error:")
                return scope
        if(var1 == ":true:" and var2 == ":true:"):
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(":true:")
        elif(var1 == ":false:" or var2 == ":false:"):
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(":false:")
        elif isName(var1) and isName(var2):
            var1name = scope.dictionary[var1]
            var2name = scope.dictionary[var2]
            if var1name == ":true:" or var1name == ":false:":
                if var2name == ":true:" or var2name == ":false:":
                    if var1name == ":false:" or var2name == ":false:":
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                else:
                    scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        elif isName(var1) and (var2 == ":true:" or var2 == ":false:"):
            var1name = scope.dictionary[var1]
            if var1name == ":true:" or var1name == ":false:":
                if var1name == ":true:" and var2 == ":true:":
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":true:")
                else:
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":false:")
            else:
                scope.stack.push(":error:")
        elif isName(var2) and (var1 == ":true:" or var1 == ":false:"):
            var2name = scope.dictionary[var2]
            if var2name == ":true:" or var2name == ":false:":
                if var2name == ":true:" and var1 == ":true:":
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":true:")
                else:
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":false:")
            else:
                scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope

def orit(scope):
    if (scope.stack.size() > 1):
        var1 = scope.stack.peek()
        if(var1 != ":true:" and var1 != ":false:"):
            if not isName(var1):
                scope.stack.push(":error:")
                return scope
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if(var2 != ":true:" and var2 != ":false:"):
            if not isName(var2):
                scope.stack.push(":error:")
                return scope
        if(var1 == ":true:" or var2 == ":true:"):
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(":true:")
        elif(var1 == ":false:" and var2 == ":false:"):
            scope.stack.pop()
            scope.stack.pop()
            scope.stack.push(":false:")
        elif isName(var1) and isName(var2):
            var1name = scope.dictionary[var1]
            var2name = scope.dictionary[var2]
            if var1name == ":true:" or var1name == ":false:":
                if var2name == ":true:" or var2name == ":false:":
                    if var1name == ":true:" or var2name == ":true:":
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        elif isName(var1) and (var2 == ":true:" or var2 == ":false:"):
            var1name = scope.dictionary[var1]
            if var1name == ":true:" or var1name == ":false:":
                if var1name == ":true:" or var2 == ":true:":
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":true:")
                else:
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":false:")
            else:
                scope.stack.push(":error:")
        elif isName(var2) and (var1 == ":true:" or var1 == ":false:"):
            var2name = scope.dictionary[var2]
            if var2name == ":true:" or var2name == ":false:":
                if var2name == ":true:" or var1 == ":true:":
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":true:")
                else:
                    scope.stack.pop()
                    scope.stack.pop()
                    scope.stack.push(":false:")
            else:
                scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope

def notit(scope):
    if (scope.stack.size() > 0):
        var1 = scope.stack.peek()
        if(var1 != ":true:" and var1 != ":false:") and not(isName(var1)):
            scope.stack.push(":error:")
            return scope
        if(var1 == ":true:" or var1 == ":false:"):
            if(var1 == ":true:"):
                scope.stack.pop()
                scope.stack.push(":false:")
            elif(var1 == ":false:"):
                scope.stack.pop()
                scope.stack.push(":true:")
        else:
            var = scope.dictionary[var1]
            if var == ":true:":
                scope.stack.pop()
                scope.stack.push(":false:")
            elif var == ":false:":
                scope.stack.pop()
                scope.stack.push(":true:")
            else:
                scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope

def equalit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if is_number(str(var1)) and is_number(str(var2)):
            if(int(var1) == int(var2)):
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(":true:")
            else:
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(":false:")
        elif isName(var1) or isName(var2):
            if isName(var1) and isName(var2):
                if is_number(str(scope.dictionary.get(var2))) and is_number(str(scope.dictionary.get(var1))):
                    hmm1 = int(scope.dictionary[var2])
                    hmm2 = int(scope.dictionary[var1])
                    if hmm1 == hmm2:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            elif isName(var1) and is_number(var2):
                if is_number(str(scope.dictionary.get(var1))):
                    hmm = int(scope.dictionary[var1])
                    if int(var2) == hmm:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            elif is_number(var1) and isName(var2):
                if is_number(str(scope.dictionary.get(var2))):
                    hmm = int(scope.dictionary[var2])
                    if hmm == int(var1):
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        elif scope.stack.isEmpty():
            scope.stack.push(":error:")
        else: scope.stack.push(":error:")
    else: scope.stack.push(":error:")
    return scope

def lessThanit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if is_number(str(var1)) and is_number(str(var2)):
            if(int(var2) < int(var1)):
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(":true:")
            else:
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(":false:")
        elif isName(var1) or isName(var2):
            if isName(var1) and isName(var2):
                tempvar2 = is_number(scope.dictionary[var2])
                tempvar1 = is_number(scope.dictionary[var1])
                if tempvar2 != None and tempvar1 != None:
                    hmm1 = int(scope.dictionary[var2])
                    hmm2 = int(scope.dictionary[var1])
                    if hmm1 < hmm2:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            elif isName(var1) and is_number(var2):
                if is_number(str(scope.dictionary.get(var1))):
                    hmm = int(scope.dictionary[var1])
                    if int(var2) < hmm:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            elif is_number(var1) and isName(var2):
                if is_number(str(scope.dictionary.get(var2))):
                    hmm = int(scope.dictionary[var2])
                    if hmm < int(var1):
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":true:")
                    else:
                        scope.stack.pop()
                        scope.stack.pop()
                        scope.stack.push(":false:")
                else:
                    scope.stack.push(":error:")
            else:
                scope.stack.push(":error:")
        elif scope.stack.isEmpty():
            scope.stack.push(":error:")
        else: scope.stack.push(":error:")
    else: scope.stack.push(":error:")
    return scope

def swapit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.pop()
        scope.stack.push(var1)
        scope.stack.push(var2)
    else: scope.stack.push(":error:")
    return scope


def isName(word):
    if not word[0].isalpha():
        return False
    else:
        return True

def isElse(word , scope):
    if is_number(word):
        return True
    elif word == ":true:" or word == ":false:":
        return True
    elif word[0] == '"':
        return True
    elif word == ":unit:":
        return True
    elif not scope.dictionary.get(word) == None:
        return True
    else:
        return False


def bindit(scope):
    if scope.stack.size() > 1:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.push(var1)
        if isName(var2) and isElse(var1, scope):
            if not (scope.dictionary.get(var1) == None):
                scope.dictionary[var2] = scope.dictionary[var1]
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(":unit:")
            else:
                scope.dictionary[var2] = var1
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(":unit:")
        else:
            scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope

def ifit(scope):
    if scope.stack.size() > 2:
        var1 = scope.stack.peek()
        scope.stack.pop()
        var2 = scope.stack.peek()
        scope.stack.pop()
        var3 = scope.stack.peek()
        scope.stack.push(var2)
        scope.stack.push(var1)
        if (var3 == ":true:" or var3 == ":false:") or (scope.dictionary[var3] == ":true:" or scope.dictionary[var3] == ":false:"):
            if var3 == ":true:" or scope.dictionary.get(var3) == ":true:":
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(var1)
            elif var3 == ":false:" or scope.dictionary.get(var3) == ":false:":
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.pop()
                scope.stack.push(var2)
        else:
            scope.stack.push(":error:")
    else:
        scope.stack.push(":error:")
    return scope

def letit(globalStack):
    s = Scope()
    topScope = globalStack.peek()
    s.dictionary = topScope.dictionary.copy()
    globalStack.push(s)
    return globalStack

def endit(globalStack):
    topScope = globalStack.pop()
    if topScope.stack.size() > 0:
        top_val = topScope.stack.peek()
        topScope = globalStack.peek()
        topScope.stack.push(top_val)
    return globalStack

def funDec(globalStack, line):
    scope = Scope()
    splitLine = line.split()
    funName = splitLine[0]
    funArgs = splitLine[1:]
    for temp in reserved:
        if temp == funName:
            scope.stack.push(":error:")
            return globalStack
        for temp2 in funArgs:
            if temp2 == temp or  temp2 == funName:
                scope.stack.push(":error:")
                return globalStack
    closure = Closure()
    topScope = globalStack.pop()
    if topScope.dictionary.get(funName) == None:
        topScope.dictionary[funName] = closure
        closure.scope.dictionary = topScope.dictionary
    else:
        topScope.push(":error:")
        globalStack.push(topScope)
        return globalStack
    for temp in funArgs:
        closure.paramList.append(temp)
    tempdict = topScope.dictionary.copy
    tempScope = Scope()
    tempScope.dictionary = tempdict
    globalStack.push(topScope)
    globalStack.push(tempScope)

    closure_dict[funName] = closure
    global currentString
    currentString = funName


    return globalStack

def returnIt(globalStack):
    templist = []
    topScope = globalStack.pop()
    while not topScope.stack.isEmpty():
        val = topScope.stack.pop()
        templist.append(val)
    temp2 = closure_dict[currentString]
    temp2.codeList = templist




    return globalStack




def interpreter(input,output):
    #read input file line by line
    #for every line in input file, perform action in stack
    #after input file is depleted, write the contents of stack onto output file
    scope = Scope()
    scopeStack = Stack()
    localStack = Stack()
    scope.stack = localStack
    #scope.dictionary = localDict
    scopeStack.push(scope)
    closure = Closure()
    closureStack = Stack()


    f = open(input, "r")
    o = open(output, "w")
    #myStack = Stack()
    flag = True;
    global currentString
    for line in f:

        scope = scopeStack.peek()

        if flag == True:

#        pushit = scope.stack.push(line[5:].strip())

#        line.strip()
        # checks if line is a string with quotes
            if "push" in line[0:4]:
                if(line[5] == '"'):
                    word = line[5:].strip()
                    #word = word.replace('"',"").strip()
                    scope.stack.push(word)
            # checks if int
                if(line[5] == '-'):
                    if(line[6:].strip() == '0'):
                        scope.stack.push('0')
                    elif(line[6:].strip().isdigit()):
                        scope.stack.push(line[5:])
                    else: scope.stack.push(":error:")
                elif(is_number(line[5:].strip())):
                    if(line[5:].strip().isdigit()):
                        scope.stack.push(line[5:])
                    else:
                        scope.stack.push(":error:")
                elif(line[5] == ':'):
                    scope.stack.push(":error:")
            # checks for "name"
                elif(not is_number(line[5:].strip()) and not line[5] == '"'):
                    scope.stack.push(line[5:].strip())
        #POP function
            if "pop" in line[0:3]:
                if( scope.stack.isEmpty()):
                    scope.stack.push(":error:")
                else: scope.stack.pop()
        #true / false function
            elif ":true:" in line[0:6]:
                scope.stack.push(":true:")
            elif ":false:" in line[0:7]:
                scope.stack.push(":false:")
        #error literal
            elif ":error:" in line[0:7]:
                scope.stack.push(":error:")

            elif "add" in line[0:3]:
                scope = addit(scope)

            elif "sub" in line[0:3]:
                scope = subit(scope)

            elif "mul" in line[0:3]:
                scope = mulit(scope)

            elif "div" in line[0:3]:
                scope = divit(scope)

            elif "rem" in line[0:3]:
                scope = remit(scope)

            elif "neg" in line[0:3]:
                scope = negit(scope)

            elif "swap" in line[0:4]:
                scope = swapit(scope)

            elif "and" in line[0:3]:
                scope = andit(scope)

            elif "or" in line[0:2]:
                scope = orit(scope)

            elif "not" in line[0:3]:
                scope = notit(scope)

            elif "equal" in line[0:5]:
                scope = equalit(scope)

            elif "lessThan" in line[0:8]:
                scope = lessThanit(scope)

            elif "bind" in line[0:4]:
                scope = bindit(scope)

            elif "if" in line[0:2]:
                scope = ifit(scope)

            elif "let" in line[0:3]:
                scopeStack = letit(scopeStack)

            elif "end" in line[0:3]:
                scopeStack = endit(scopeStack)

            elif "fun" in line[0:3]:
                scopeStack = funDec(scopeStack, line[4:])

                #scopeStack = funDec(scopeStack, line[4:])

                flag = False;

            elif "quit" in line[0:4]:
                while scopeStack.size() > 0:
                    if scopeStack.size() == 1:
                        topScope = scopeStack.peek()

                        while not topScope.stack.isEmpty():
                            item = topScope.stack.pop()
                            item = str(item)
                            item = item.strip('\n')
                            if is_number(item):
                                o.write(item + '\n')
                            elif item[0] == '"':
                                item = item.replace('"', "")
                                o.write(item + '\n')
                            else:
                                o.write(item + '\n')
                    scopeStack.pop()
        else:

            if "return" in line[0:6]:
                scopeStack = returnIt(scopeStack)
                flag = True;
            else:

                split_line = line.split()
                for temp in split_line[1:]:
                    if not isName(temp):
                        scope.stack.push(":error:")
                        scopeStack.pop()
                scope.stack.push(split_line[0])


            #    print("-----------stack------------")
    while scopeStack.size() > 0:
        if scopeStack.size() == 1:
            topScope = scopeStack.peek()
            while not topScope.stack.isEmpty():
                topVar = topScope.stack.peek()
                if is_number(topVar):
                    o.write(str(topVar))
                    print(topVar)
                    topScope.stack.pop()
                elif topVar[0] == '"':
                    topVar = topVar.replace('"',"").strip()
                    topScope.stack.pop()
                    topScope.stack.push(topVar)
                    o.write(topScope.stack.peek().strip() + "\n")
                    print( topScope.stack.peek())
                    topScope.stack.pop()
                else:
                    o.write( topScope.stack.peek().strip() + "\n")
                    print( scope.stack.peek())
                    topScope.stack.pop()
#                topScope.stack.pop()
        scopeStack.pop()

    '''
    print("------ Stack ------")
    while not scope.stack.isEmpty():
        tempString = scope.stack.peek()
        if is_number(tempString):
            o.write(str(tempString))
            print(tempString)
            scope.stack.pop()
        elif tempString[0] == '"':
            tempString = tempString.replace('"',"").strip()
            scope.stack.pop()
            scope.stack.push(tempString)
            o.write( scope.stack.peek().strip() + "\n")
            print( scope.stack.peek())
            scope.stack.pop()
        else:
            o.write( scope.stack.peek().strip() + "\n")
            print( scope.stack.peek())
            scope.stack.pop()
    '''
    #for p in scope.stack.items:
    #    o.write( scope.stack.peek())
    #    scope.stack.pop()
    f.close()
#interpreter('input.txt', 'output.txt')
#scope = Stack()
# scope.stack.push("4")
# scope.stack.pop()
