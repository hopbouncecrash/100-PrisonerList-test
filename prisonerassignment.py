#import random module
import random
#generating list of numbers 1-100
prisonerlist=list(range(1,101))
#generating box list
boxlist=list(range(1,101))
#sample number of tries
print("input number of tries:")
samplesize=input()
samplesize=int(samplesize)
initialnumber=0
finalresult=[]
#follow the boxes using the loop rule
while initialnumber<samplesize:
#shuffle box list
    shuffleboxlist=random.sample(boxlist,len(boxlist))
    #assign box list to dictionary
    assignmentdict=dict(zip(shuffleboxlist,prisonerlist))
    storeresult=[]
    maxtries=50
    for prisoner in prisonerlist:
        temptries=0
        prisonertry=prisoner
        tempresult=False
        while temptries<maxtries:
            prisonertry=assignmentdict[prisonertry]
            temptries=temptries+1
            if prisonertry==prisoner:
                storeresult.append(True)
                tempresult=True
                temptries=temptries+50
        if tempresult==False:
            storeresult.append(False)
    if False in storeresult:
        finalresult.append(0)
    else:
        finalresult.append(1)

    initialnumber=initialnumber+1
#print(finalresult)
print('number of tries:'+str(len(finalresult)))
average_success=sum(finalresult)/len(finalresult)
print('success rate='+str(average_success))