l = int(input("Last Number: "))
# n × ( n + 1 ) × ( 2 n + 1 ) 

def SumSquare(l):
    v = (l * ( l + 1 ) * ( (2 * l) + 1 )) / 6
    return v

print(SumSquare(l))