import math

# import sys
# inputs = sys.stdin.read().splitlines() # read all first
# outputs = []                           # buffer output first
# ln = 0                                 # assumption:
# while True:                            # input has >1 lines
#     N = int(inputs[ln])                # with 1 integer each
#     if N == 0: break
#     outputs.append(str(N))            
#     ln += 1
# sys.stdout.write('\n'.join(outputs))   


def secret(N, messages):
    returnArr = []
    for i in range(0, len(messages)):
        message = messages[i]
        enc = ''
        L = len(message)
        M = int(math.ceil(math.sqrt(L)))
        astericMessage = message + '*'*M 
        count = M-1
         
        
    
print(secret(1, ['iloveyouJack']))

# i = (0,0) -> (3,0)
# l = (1,0) -> (3,1)
# o = (2,0) -> (3,2)
# v = (3,0) -> (3,3)

# e = (0,1) -> (2,0)
# y = (1,1) -> (2,1)
# 