def truecaller(phn):
    dbc={}
    f = open('C', 'r')
    db=f.read()
    f.close()
    for i in db:
        k=""
        v=""
        while(i!=":"):
            k=k+i
        while(i!=","):
            v=v+i
        dbc[k]=v
    print "this number belongs to",dbc[phn]
phn=input("enter number")
phn=str(phn)
truecaller(phn)



