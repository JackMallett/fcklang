

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




def exec(args: list[str]):
    functions = [
        'howbig(',
        'say('
    ]

    for f in functions:
        for i, v in enumerate(args):
            if v == f:
                
                # inner_args = args[i:]
                # end = inner_args.index(')')
                # inner_args = inner_args[i: end]

                arg = args[i+1]




    return 0

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

