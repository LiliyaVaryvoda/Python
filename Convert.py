mydict={"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35}

def convert_n_to_m(x, n, m):
    z = ""
    v = 0
    mylist=[]
    if type(x) == str or type(x) == int:
        if x<0:
            return False
        elif type(x)==str:
            for element in x:
                if element in mydict.keys() and n<11:
                    return False
                elif int(element)>=n:
                    return False
        elif type(x)==int:
            for element in str(x):
                if int(element)>=n:
                    return False
        elif m==1:
            y=len(str(x))
            for element in str(x):
                y=y-1
                v+=(int(element)*(n**y))
            return str(0)*v
        elif n<10:
            y=len(str(x))
            for element in str(x):
                y=y-1
                v+=(int(element)*(n**y))
            while v >= 1:
                z += str(v % m)
                v = v // m
                return z[::-1]
        elif n==10:
            while x>0:
                z+=str(x%m)
                x=x//m
                return z[::-1]
        else:
            if n > 10:
                y = len(str(x))
                for element in str(x).upper():
                    if element in mydict.keys():
                        element1=mydict.get(element)
                        mylist.append(element1)
                    else:
                        mylist.append(element)
                for value in mylist:
                    y = y - 1
                    v += (int(value)*(n * y))
                while v>=1:
                    z1=v%m
                    if z1>9:
                        z2= mydict.keys()[mydict.values().index(z1)]
                        z+=z2
                    else:
                        z+=str(z1)
                    v=v//m
                    return z[::-1]
    else:
        return False