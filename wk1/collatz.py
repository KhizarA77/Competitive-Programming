def collatz(num_1, num_2):
    num1 = num_1
    num2 = num_2
    # Two dictionaries for num of steps taken to reach each value
    S_a = dict()
    S_b = dict()

    
    S_a[num1] = 0
    S_b[num2] = 0
    steps_A = 1
    while True: # num 1
        if num1 != 1 and num1 % 2 == 0:
            num1 = num1/2
        elif num1 != 1 and num1 % 2 != 0:
            num1 = 3*num1 + 1 
        # num1 = int(num1)
        S_a[num1] = steps_A
        steps_A += 1
        if num1 == 1:
            break
    
    steps_B = 0
    while True:

        if num2 in S_a:
            print(f"{num_1} needs {S_a[num2]} steps, {num_2} needs {steps_B} steps, they meet at {int(num2)}")
            break

        if num2 != 1 and num2 % 2 == 0:
            num2 = num2/2
        elif num2 != 1 and num2 % 2 != 0:
            num2 = (3*num2) + 1
        # num2 = int(num2)



        S_b[num2] = steps_B
        steps_B += 1
        if num2 == 1:
            break
    



while True:
    _input = input()
    num1 = int(_input.split(' ')[0])
    num2 = int(_input.split(' ')[1])
    if num1 == 0 and num2 == 0:
        break
    collatz(num1, num2)
