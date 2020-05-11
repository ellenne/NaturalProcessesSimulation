## The aim of this process is to forecast the outcome of an cellular automata given an input path

def applyRules (segment):
    '''
    This method taken in input a segment made of 3 neighour and calculate the outcome
    '''
    rules = {
        "111": 0,  #1
        "110": 1,  #2
        "101": 1,  #3
        "100": 0,  #4
        "011": 1,  #5 
        "010": 1,  #6
        "001": 1,  #7 
        "000": 0  #8
    }

    ret = rules.get(segment, lambda: "invalid")

    return ret


#index   0  1  2  3  4  5  6  7  8  9 10  11
input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

cur = input

print(f"Input      : [{cur[0]}{cur[1]}{cur[2]}{cur[3]}{cur[4]}{cur[5]}{cur[6]}{cur[7]}{cur[8]}{cur[9]}{cur[10]}{cur[11]}]")

for i in range (8):

    ret = [0] * 12    

    for j in range(len(ret)):
        #build string
        left = str(cur[j-1])
        central = str(cur[j])
        if j+1 == len(cur):
            right = str(cur[0])
        else:
            right = str(cur[j+1])
        myStr = left + central + right
        #call function
        ret[j] = applyRules(myStr)
    
    print(f"Iteration {i}: [{ret[0]}{ret[1]}{ret[2]}{ret[3]}{ret[4]}{ret[5]}{ret[6]}{ret[7]}{ret[8]}{ret[9]}{ret[10]}{ret[11]}]")

    cur = ret
        


