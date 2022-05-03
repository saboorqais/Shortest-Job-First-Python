##Importing Class to Check occurency
from collections import Counter
def sjf(jobs: list, index: int):
  ##Initalizing data varibales to be stored
    finalData=[]
    #Total Time for eacah job
    total=0
    j=jobs
    #Referecning new List 
    a=list(j)
    d=[]
    #List to keep track of the values Been Visited
    for each in range(len(jobs)):
       d.append(0) 
    #looping over all the values one by one
    for each in jobs:
        minpos = a.index(min(a))
        #Finding the digit value of minimum position
        digit=a[minpos]
        total=total+digit
        data={}
        ##occurency Check
        if(Counter(jobs)[digit]>1):
          #Finding the positon of occurency
            indexes = [i for i in range(len(jobs)) if jobs[i] == digit]
            x=0
            ##Cross checking the value been Visited For FIFO
            for each in indexes:
                if d[each]==0 :
                    data['position']=each
                    data['time']=total
                    ##marking visit
                    d[each]=1
                    finalData.append(data)
                    break
              
        else:
          ##Block For single Occurence Values
            data['position']=jobs.index(digit)
            data['time']=total
            ##marking visit
            d[jobs.index(digit)] =1
            finalData.append(data)
        ##popping out the visited value from new referenced list
        a.pop(minpos)
    #searching the position
    for each in finalData:
        if each['position']==index:
          #returning the time based on input positon
            return each['time']