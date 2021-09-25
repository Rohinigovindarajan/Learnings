def nthSevenish(n):
    power = 0
    add = 0
    sevenish=[1]*n
    i=1
    while(i<n):
        if add == power:
            add = 0
            sevenish[i] = sevenish[power]*7
            power = i
        else:
            sevenish[i]=sevenish[power]+sevenish[add]
            add+=1
        i+=1
    return sevenish[-1] 
n=int(input("Enter n : "))
if n <= 0:
    print("Enter valid input")
else:
    print(nthSevenish(n))