from fuck import execute



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
    count = 0
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





def check_type(x: str, vars: dict[str]):
    x = x.strip()

    if x[0] == '[' and x[-1] == ']':
        x_type = 'list'
        x = make_list(x)
        for i, v in enumerate(x):
            x[i] = check_type(v)[1]

        return x_type, x

    #String------------------------------------------
    elif (x[0] == "'" and x[-1] == "'") or (x[0] == '"' and x[-1] == '"'):
        x_type = 'string'
        return x_type, x



    #Numbers-----------------------------------------
    #int
    elif x.isdigit() or (x[0] == '-' and x[1:-1].isdigit()):
        x_type = 'int'
        return x_type, int(x)

    #float
    elif '.' in x and (x[:x.index('.')].isdigit() or (x[0] == '-' and x[1:x.index('.')].isdigit()) and x[x.index('.') + 1:].isdigit()):
        x_type = 'float'
        return x_type, float(x)

    #variable
    elif x == 'True' or x == 'False':
        x_type = bool
        return x_type, x

    elif ' ' not in x and x in vars.keys():
        x_type = 'var'
        return x_type, vars[x]

    else:
        x_type = 'expression'
        x = execute(x)
    #FUNCTIONS
    # elif '(' in x:
    #     prefix = x[0:x.index('(')]

    #     functions[prefix]()

    


# def howbig(input):
    
# z = "['hello my name jack', 35, 'i like pizza, coffee, and golf', 132525, True]"

# print(check_type(z))