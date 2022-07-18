import re

a = "Commencement of B.Des S3, B.Tech S5, MCA S3, M.Arch S3 "
b = "Commencement of B.Des S3(S)/S9(S)/S2 B.Tech S5, MCA S3, M.Arch S3 "
c = "Commencement of B.Des/B.Tech MCA S3, M.Arch S3 "

def filt(test):

    
    print(" ")

    print( " Notification :  " + test)
    test1 = test.replace(',', '').replace('/', ' ').replace('(', ' ')
    res = test1.split()
    # print(res)
    # res = test.split(", ")
    # print(" Filtered string is : " + str(res))
    # n = len(res)
    #print(" ")

    prog = ["B.Tech", "B.Arch", "B.Des", "M.Tech", "MCA", "M.Arch", "M.Plan"]
    sem = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
    l=[]
    program=""
    semm=""
                
    for x in res:
        for y in prog:
            if x==y:
                program = x
                dy={}
                dy["program"]=program
                print(" Program  = " + x)  

        for z in sem:
            if x==z:
                semm = z
                print(" Sem      = " + z)
                dy={}
                dy["program"]=program
                dy["semester"]=semm
                l+=[dy]
                # print(dy)

    print(l)
    print(" ")
    return l
    # print(" - - - - - - - - - - - - - - - -  ")  

# filt(a)
# filt(b)
# filt(c)

        