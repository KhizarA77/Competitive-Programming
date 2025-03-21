dictionary = dict()


def performOperations(_input):
    
    global dictionary
    input = _input.split(' ')
    operation = input[0]

    if operation == 'def':

        varname = input[1]
        value = int(input[2])
        dictionary[varname] = value
    
    elif operation == 'clear':
        dictionary = dict()



    elif operation == 'calc':
        vars = []
        ops = []

        for i in range(1, len(input)):
            if i % 2 != 0:
                vars.append(input[i])
            else:
                if input == '=':
                    break
                ops.append(input[i])
        j = 0
        if vars[0] not in dictionary:
            print(f"{_input[5:]} unknown")
            return
        
        result = dictionary[vars[0]]

        for i in range(1, len(vars)):
            v2 = 0

            if vars[i] not in dictionary:
                print(f"{_input[5:]} unknown")
                return

            if j >= len(ops):
                break

            if ops[j] == '=':
                break

            v2 = dictionary[vars[i]]

            if ops[j] == '+':
                result = result + v2
                j += 1
            
            elif ops[j] == '-':
                result = result - v2
                j+=1
            


        res = 'unknown'
        
        for key, value in dictionary.items():
                if value == result:
                    res = key
                    break
        
        output_string = f"{_input[5:]} {res}"

        print(output_string)



    

while True:
    try:
        _input = input()
        performOperations(_input)
    except EOFError:
        break