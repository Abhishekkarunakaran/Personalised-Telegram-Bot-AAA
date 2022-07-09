# import re


def filt(test):

    
    print(" ")
    print( " Notification :  " + test)
    res = test.split()

    #print(" Filtered string is : " + str(res))
    # n = len(res)
    #print(" ")

    prog = ["B.Tech", "B.Arch", "B.Des", "M.Tech", "MCA", "M.Arch", "MBA"]
    sem = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]

    for x in res:
        for y in prog:
            if x==y:
                # program = x
                print(" Program  = " + x)
                prgm=x

    for x in res:
        for z in sem:
            if x==z:
                # semester = x
                print(" Sem      = "+ x)
                sems=x

    print(" ")
  #return prgm,sems
    # print(" - - - - - - - - - - - - - - - -  ")  
        