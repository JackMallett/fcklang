
vars = {}

# f = open("demofile.txt", "r")
# f.readline()

def say(to_say, Lines: list[str], line_num: int):
    to_say = check_type(to_say, Lines, line_num)
    print(to_say)



functions = {
    'say' : say
}

DEBUG = False
def debug(arg: str):
    # DEBUG = True
    if DEBUG: print(arg)


def lineread(line: str):
    if line.startswith('goodnum') or line.startswith('badnum') or line.startswith('words'):
        declare(line)
    
    elif [line.startswith(x) for x in functions]:
        prefix = line[0:line.index('(')]

        functions[prefix]()




#line reading methods-----------------------

def declare(line: str):
    line = line.strip()
    if line.startswith('goodnum'):
        new_goodnum(line)
        
    elif line.startswith('badnum'):
        new_badnum(line)

    elif line.startswith('words'):
        new_words(line)

def eqs(line: str):
    if '==' in line:
        a, b = line.split('==')
        a, b = a.strip(), b.strip()

        if a in vars:
            a = vars[a]
        if b in vars:
            b = vars[b]

        return a == b

# ------------------------------------------





def new_goodnum(line : str):
    line = line.strip().replace('goodnum ','')
    name, value = line.split('=')

    name = name.strip()
    value = int(value.strip())


    vars.update({name: value})

def new_badnum(line : str):
    line = line.strip().replace('badnum ','')
    name, value = line.split('=')

    name = name.strip()
    value = float(value.strip())

    vars.update({name: value})

def new_words(line : str):
    line = line.strip().replace('words ','')
    name, value = line.split('=')

    name = name.strip()
    value = value.strip()[1:-1]     #remove quotes

    vars.update({name: value})









def howbig(line):
    if type(line) == str:
        return len(make_list(line))
    else:
        return len(line)


def split_line(line: str):      #function that splits in input line into a list of its terms and the operators between them

    count = 0
    in_quotes = False
    out = []
    tempstring = ''
    separators = ['+', '/', '-', '%', '*']

    def addtemp():
        if tempstring != '':
            out.append(tempstring)


    while(count < len(line)):
        
        c = line[count]
        if c == '"' or c == "'":
            addtemp()
            tempstring = ''
                                        #take the slice of the string from the current starting quote to the next quote mark
            quote = line[count + 1:]    #make a slice from the character after the opening quotation mark to the end of the string
            endquote = quote.index(c) + 1   #find the first occurance of a quotaion mark in the string (finds the next quotation mark which ends the string)

            tempstring = c + quote[:endquote]   #add this slice to the list
            addtemp()
            tempstring = ''
            count = (len(line) - len(quote)) + endquote     #convers the index of the quotation mark from the substring to its index in the original input line
            continue

        if tempstring == 'loop(':
            addtemp()
            temp = line[count: line.rindex(')')]
            temp = temp.split(',')
            for x in temp:
                out.append(x)
            tempstring = ''
            return out

        if c == ' ':
            addtemp()
            tempstring = ''
        elif line[count:count+2] in ['==', '**']:
            addtemp()
            out.append(line[count:count+2])
            count = count + 2
            tempstring = ''
        elif c in separators:
            addtemp()
            out.append(c)
            tempstring = ''
        else:
            tempstring = tempstring + c

        count += 1

    if tempstring != '':
        addtemp()
    return out


def make_list(line: str) -> list[str]:
    count = 1
    tempstring = ''
    out = []

    def addtemp():
        if tempstring != '':
            out.append(tempstring)

    while count < len(line):
        c = line[count]

        if c == '"' or c == "'":
            tempstring = ''

            #take the slice of the string from the current starting quote to the next quote mark
            quote = line[count + 1:]    #make a slice from the character after the opening quotation mark to the end of the string
            endquote = quote.index(c) + 1   #find the first occurance of a quotaion mark in the string (finds the next quotation mark which ends the string)

            tempstring = c + quote[:endquote]   #add this slice to the list
            addtemp()

            tempstring = ''
            count = (len(line) - len(quote)) + endquote     #convers the index of the quotation mark from the substring to its index in the original input line
            continue
        elif line[count: count + 2] == ', ':
            addtemp()
            tempstring = ''
            count += 1
        elif c == ',' or c == ']':
            addtemp()
            tempstring = ''
        else:
            tempstring =  tempstring + c
        count += 1
    return out


def check_type(x: str, Lines: list[str], line_num: int, return_type: bool = False, variables: dict[str] = vars):
    if type(x) is not str:
        return (str(type(x)), x) if return_type else x


    x = x.strip()

    if x[0] == '[' and x[-1] == ']':
        x_type = 'list'
        x = make_list(x)
        for i, v in enumerate(x):
            x[i] = check_type(v, Lines, line_num)

        return (x_type, x) if return_type else x

    #String------------------------------------------
    elif (x[0] == "'" and x[-1] == "'") or (x[0] == '"' and x[-1] == '"'):
        x = x.strip(x[0])
        x_type = 'string'
        return (x_type, x) if return_type else x

    elif ' ' not in x and x in variables.keys():
        x_type = 'var'
        return (x_type, variables[x]) if return_type else variables[x]

    #Numbers-----------------------------------------
    #int
    elif x.isdigit() or (x[0] == '-' and x[1:-1].isdigit()):
        x_type = 'int'
        return (x_type, int(x)) if return_type else int(x)

    #float
    elif '.' in x and (x[:x.index('.')].isdigit() or (x[0] == '-' and x[1:x.index('.')].isdigit()) and x[x.index('.') + 1:].isdigit()):
        x_type = 'float'
        return (x_type, float(x)) if return_type else float(x)
    
    #variable
    elif x == 'True' or x == 'False':
        x_type = 'bool'
        x = True if x == 'True' else False
        return (x_type, x) if return_type else x

    

    else:
        x = split_line(x)
        x_type = 'expression'
        x = execute(x, Lines, line_num)
        return (x_type, x) if return_type else x


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def process_line(line: str, Lines: list[str], line_num: int):
    #declarative
    debug(f'processing line: {line}')
    if line == '\n' or line == '' or line.strip()[0] == '#':
        return
    line = line.strip()
    for i, v in enumerate(line):
        if v == '(':
            break
        if v == '=' and line[i + 1] != '=':
            #decl
            var_type, var_val = check_type(line[i + 1:], Lines, line_num, True)
            var_name = line[:i].strip()
            vars.update({var_name: var_val})
            

    if line.strip()[0:4] == 'say(':
        e = line.rindex(')')      #index of furthest right close-parenthesis
        to_print = line[4:e]

        say(to_print, Lines, line_num)

    else:
        execute(split_line(line), Lines, line_num)

def execute(args: list[str], Lines: list[str], line_num: int):
    debug(f'executing: {args}')
    out = args.copy()
    to_del = []
    functions = [
        'howbig(',
        'say('
        'loop('
    ]
    maths = {
        '+': lambda a, b: a+b, 
        '/': lambda a, b: a/b, 
        '-': lambda a, b: a-b, 
        '%': lambda a, b: a%b, 
        '*': lambda a, b: a*b, 

        '<': lambda a, b: a<b,
        '>': lambda a, b: a>b,
        '<=': lambda a, b: a<=b,
        '>=': lambda a, b: a>=b,

        '**': lambda a, b: a**b, 
        '//': lambda a, b: a//b    
    }


    debug(f'args: {args}')

    for i, v in enumerate(args):
        

        if v =='howbig(':
            arg = check_type(args[i+1], Lines, line_num)
            to_del.append(i)
            to_del.append(i+1)
            out[i + 2] = howbig(arg)

        if v == 'loop(':
            #['loop(', 'arg1',     'arg2',       'arg3',  '){']
            #         counter    condition   incrementer
            counter = args[i + 1]
            condition = args[i + 2]
            incrementer = args[i + 3]
            process_line(counter, Lines, line_num)
            loop_start_pos = line_num
            while execute(split_line(condition), Lines, line_num) is False or execute(split_line(condition), Lines, line_num) == 'False':
                line_num = loop_start_pos
                while True:
                    line_num += 1
                    if Lines[line_num] == '}':
                        break
                    else:
                        process_line(Lines[line_num], Lines, line_num)

                process_line(incrementer, Lines, line_num)

                        



    #condenses arguments
    #ex:     ['howbig(', my_list', ')', '==', '5'] --->  ['5', '==', '5']

    to_del.sort(reverse=True)
    for x in to_del:
        del(out[x])
    to_del = []
    args = out.copy()



# MATH OPERATIONS
# -------------------------------------------------------------------------------
    while not set(maths).isdisjoint(args):      #loops while any of the mathematical operators in keys of the 'maths' dict are in the args
        for x in maths:
            for i, v in enumerate(args):
                if v == x:
                    arg1 = check_type(args[i - 1], Lines, line_num)      #takes the list items before and after the mathematical operator   (ex 15 and 32 in : ['15', '+', '32'] )
                    arg2 = check_type(args[i + 1], Lines, line_num)

                    result = maths[v](arg1, arg2)       #computes the result of the two args using the appropriate lambda function stored in the 'maths; array
                   
                    args[i + 1] = result        #stores the result in the args array in place of the second argument  (since we're in a while loop we can change the main list without issues)
                    del(args[i])                #deletes the first argument and the mathematical operator (the middle arg) replacing the terms with their results
                    del(args[i-1])              #ex: ['15', '+', '32']   --> [47]
                    
                    out = args.copy()           #copies the args to the out list (used for the remaining methods that use iterators instead of while loops)




# --------------------------------------------------------------------------------

# -------------------------------------------------------------------------------

    # for x in maths:
    #     for i, v in enumerate(args):
    #         if v == x:
    #             arg1 = check_type(args[i - 1], Lines, line_num)
    #             arg2 = check_type(args[i + 1], Lines, line_num)

    #             result = maths[v](arg1, arg2)
    #             out[i + 1] = result
    #             to_del.append(i-1)
    #             to_del.append(i)

    # to_del.sort(reverse=True)
    # for x in to_del:
    #     del(out[x])
    # to_del = []
    # args = out.copy()

# --------------------------------------------------------------------------------


    while '==' in args or '!=' in args:
        print(f'args while: {args}')
        for i, v in enumerate(args):
            if v == '==' or v == '!=':
                true = True if v == '==' else False
                arg1 = check_type(args[i - 1], Lines, line_num)
                arg2 = check_type(args[i + 1], Lines, line_num)
                if arg1 == arg2:                
                    args[i + 1] = true          #stores the result in the args array in place of the second argument  (since we're in a while loop we can change the main list without issues)
                else: 
                    args[i + 1] = not true

                       
                del(args[i])                #deletes the first argument and the mathematical operator (the middle arg) replacing the terms with their results
                del(args[i-1])              #ex: ['15', '+', '32']   --> [47]
                
                out = args.copy()           #copies the args to the out list (used for the remaining methods that use iterators instead of while loops)
                print(f'args fater: {args}')

    if len(out) == 1:
        out = out[0]
    debug({f'out: {out}'})
    return out




if __name__ == '__main__':
    while True:
        x = input()
        if x[0:6] == 'fuck' and x[-4:] == '.txt':
            f = open(x[6:], 'r')
            Lines = [line.strip() for line in f.readlines()]
            lc = 0
            while lc < len(Lines):
                line = Lines[lc]
                process_line(line, Lines, lc)
                lc += 1
        elif x.lower() == 'fuckthis':
            print('fuck you too :)')
            break
        else:
            print('Please execute a file using: \nfuck example.txt\n or quit by saying "fuckthis')