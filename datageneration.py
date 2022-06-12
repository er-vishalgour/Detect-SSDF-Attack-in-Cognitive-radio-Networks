from random import randint
# from tabulate import tabulate
# import pandas as pd
from random import shuffle
import os
import random


class data():

    def __init__(self):
        self.dictData=dict()
    
    def getdata(self):
        return self.dictData



    
def main():

    if os.path.exists("dataset1.txt"):
        os.remove("dataset1.txt")
    if os.path.exists("dataset2.txt"):
        os.remove("dataset2.txt")
    if os.path.exists("Nonmaliciousdata.txt"):
        os.remove("Nonmaliciousdata.txt")
    if os.path.exists("partitionData.txt"):
        os.remove("partitionData.txt")
    if os.path.exists("Maliciousdata1.txt"):
        os.remove("Maliciousdata1.txt")
    if os.path.exists("DetectionRatio.txt"):
        os.remove("DetectionRatio.txt")
    if os.path.exists("FalseDetectionRatio.txt"):
        os.remove("FalseDetectionRatio.txt")
    if os.path.exists("sensingreport.txt"):
        os.remove("sensingreport.txt")
    if os.path.exists("PrimaryUser.txt"):
        os.remove("PrimaryUser.txt")
    if os.path.exists("DetectionRatio_fuzzy.txt"):
        os.remove("DetectionRatio_fuzzy.txt")
    if os.path.exists("FalseDetectionRatio_fuzzy.txt"):    
        os.remove("FalseDetectionRatio_fuzzy.txt")



    PU = []
    P_pu=0.5
    #P_pu is probability of presence of primary user
    alpha=0.6


    mal = []
    mal2 = []
    P_fa=0.10
    P_md=0.10
    SU = []
    SU2 = []
    final = []
    final2 = []
    indx=[]
    nonMalIndx=[]
    Sreport=[]

    SEC=input("How many users you want:")
    SEC=int(SEC)
    print(SEC)
    TS=input("How many time slots you want")
    TS=int(TS)
    print(TS)
    ad=[SEC]
    ABC=SEC-1
    print(ABC)
    
    for i in range(0,SEC):
        x=randint(1,100)
        if(x<=P_pu*100):
            PU.append(1)
        else:
            PU.append(0)
    for i in PU:
        f = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\PrimaryUser.txt","a")
        f.write(str(i))
        f.write("\n")         

    print("The presence or absence of primary user is as follows:")
    print(PU)
    
    


    
    
    def secondary_user():
        for i in range(0,SEC):
            column = []
            for j in range(0,TS):
                x=randint(1,100)
                # print(x)
                if(PU[i]==0):
                    
                    if(x<=P_fa*100):
                        
                        column.append(1)
                    else:
                        column.append(0)
                elif(PU[i]==1):
                    
                    if(x<=P_md*100):
                        column.append(0)
                    else:
                        column.append(1)
                
            SU.append(column)

        for i in range(SEC):
            print(i)
            print(SU[i])   
    
    def secondaryUser2():
        
        
        for i in PU:
            column = []
            for j in range(0,TS):
                x=randint(1,100)
                # print(x)
                if(i==0):
                    
                    if(x<=P_fa*100):
                        
                        column.append(1)
                    else:
                        column.append(0)
                elif(i==1):
                    
                    if(x<=P_md*100):
                        column.append(0)
                    else:
                        column.append(1)
                
            SU2.append(column)
        



    LOM=input("How many malicious users you want:")
    LOM=int(LOM)
    # LON=input("How many non malicious users you want:")
    # LON=int(LON)
    LON=SEC-LOM
    print(LON)
    print("Enter the range in between which you want to introduce the malicious")
    SR=input("Enter the starting range")
    SR=int(SR)
    ER=input("Enter the ending range")
    ER=int(ER)
    indx=random.sample(range(SR,ER),LOM)
    


    def always_yes():

        for i in range(len(indx)):
            column = []
            for j in range(0,TS):
                column.append(1)
            mal2.append(column)
        for i in indx:
            column = []
            for j in range(0,TS):
                column.append(1)
            mal.append(column)

    def always_no():
    
        for i in range(0,LOM):
            column = []
            for j in range(0,TS):
                column.append(0)
            mal2.append(column)   
        for i in range(0,LOM):
            column = []
            for j in range(0,TS):
                column.append(0)
            mal.append(column)  

    def always_false():

        for i in indx:
            column= []
            for j in range(0,TS):
                
                if(SU2[i][j]==0):
                    column.append(1)
                else:
                    column.append(0)
            mal2.append(column) 
        for i in indx:
            column= []
            for j in range(0,TS):
                
                if(SU[i][j]==0):
                    column.append(1)
                else:
                    column.append(0)
            mal.append(column)                
                
    def random_yes():

        for i in indx:
            column=[]
            for j in range(TS):
                x=random.randint(0,100)
                if(x<=alpha*100):
                    column.append(1)
                else:
                    column.append(0)
                
            mal2.append(column) 
                
            mal.append(column)           

    def random_no():

        for i in indx:
            column=[]
            for j in range(TS):
                x=random.randint(0,100)
                if(x<=alpha*100):
                    column.append(0)
                else:
                    column.append(1)
                
            mal2.append(column) 

            mal.append(column)

    def random_false():

        for i in indx:
            column=[]
            for j in range(TS):
                x=random.randint(0,100)
                if(SU2[i][j]==0):
                    if(x<=alpha*100):
                        column.append(1)
                    else:
                        column.append(0)
                else:
                    if(x<=alpha*100):
                         column.append(0)
                    else:
                        column.append(1)
            mal2.append(column)

        for i in indx:
            column=[]
            for j in range(TS):
                x=random.randint(0,100)
                if(SU[i][j]==0):
                    if(x<=alpha*100):
                        column.append(1)
                    else:
                        column.append(0)
                else:
                    if(x<=alpha*100):
                         column.append(0)
                    else:
                        column.append(1)
            mal.append(column)



    print("\n")
    print("1 for Always Yes attack ")
    print("2 for Always No attack  ")
    print("3 for Always False attack  ")
    print("4 for Random Yes attack  ")
    print("5 for Random No attack ")
    print("6 for Random False attack \n")
    attack = input("Enter which attack you want:")
    attack = int(attack)
    print(attack)
    print(type(attack))
    if(attack == 1):
        always_yes()
        secondary_user()
        secondaryUser2()
    elif(attack == 2):
        always_no()
        secondary_user()
        secondaryUser2()
    elif(attack == 3):
        secondary_user()
        secondaryUser2()
        always_false()
    elif(attack == 4):
        secondary_user()
        secondaryUser2()
        random_yes()
    elif(attack == 5):
        secondary_user()
        secondaryUser2()
        random_no()

    else:
        secondary_user()
        secondaryUser2()
        random_false()

    
    



    for t in range(SEC):
        final.append(None)


    
    dictObj = data()
    dictData = dictObj.dictData
    
    

    

    for k in range(len(indx)):
        inx = indx[k]
        final[inx]=mal[k]



    # for item in SU:
    #     empty=None
    #     for x in range(len(final)):
    #         if(final[x]!=None):
    #             continue
    #         empty=x
    #         break
    #     final[empty]=item

   

    for x in range(len(final)):
        if(final[x]!=None):
            continue
        empty=x
        final[empty]=SU[empty]
    

    print("I am Final")

    
    


    for b in range(len(final)):
        found=False
        for p in indx:
            if(b == p):
                found=False
                break
            else:
                found=True
                continue
        
        if(found):
            nonMalIndx.append(b)

    dictData['1']=indx
    dictData['0']=nonMalIndx



    print("The indexes of malicious values in the final list are :")
    print(dictData['1'])
    print("The indexes of non-malicious values in the final list are :")  
    print(dictData['0']) 
    print("Length malicious {}".format(len(dictData['1'])))
    print("Length non-malicious {}".format(len(dictData['0'])))
    print(dictData)

        

    # p=randint(0,19)
    # check=[]
    # num=0
    # while(num<p):
    #     r=randint(0,19)
    #     for i in check:
    #         if

        


    print("The secondary user  is as follows")
    for i in range(SEC):
        print(i)
        print(final[i])
    
    
    
    for t in range(SEC):
        final2.append(None)
    for k in range(len(indx)):
        inx2 = indx[k]
        final2[inx2]=mal2[k]
    for x in range(len(final2)):
        if(final2[x]!=None):
            continue
        empty2=x
        final2[empty2]=SU2[empty2]
    for i in final2:
        f111 = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\sensingreport.txt","a")
        f111.write(str(i))
        f111.write("\n")


    def Hamming_Distance(a,b):
        count=0
        for i in range(0,TS):
            if(a[i]!=b[i]):
                count=count+1
        return count
        print(count)
    print("Hamming distances")
    lst=[]
    for k in range(SEC):
        lst.append(k)
    # print(lst)
    distance=[]
    for i in range(0,SEC):
        # j=i
        distance2=[]
        distance3=[]
        #print(lst[i])
        for j in range(0,SEC):
            # print("final:{}".format(i))
            # print(final[i])
            # print("final:{}".format(j))
            # print(final[j])
            ham=Hamming_Distance(final[i],final[j])
            ham2=Hamming_Distance(final2[i],final2[j])

            distance2.append(ham)
            distance3.append(ham2)
            #print(ham)

            f = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\dataset1.txt","a")
            f.write(str(distance2[j]))
            if(j!=SEC-1):
                f.write(",")


            f1 = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\dataset2.txt","a")
            f1.write(str(distance3[j]))
            if(j!=SEC-1):
                f1.write(",")
            


            
        f.write("\n")
        f1.write("\n")

        distance.append(distance2)
        # df =pd.DataFrame(ham)
        # print(df)   
        
        # print("next")
    print('  {}'.format(lst))
    for i in range(0,SEC):
        print('{} {}' .format(lst[i], distance[i]))
    
    file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\partitionData.txt","a")
    for i in indx:
        file.write("1 ")
        file.write(str(i))
        file.write("\n")
    for j in nonMalIndx:
        file.write("0  ")
        file.write(str(j))
        file.write("\n")

    file.close()

    
    file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Maliciousdata1.txt","a")
    for i in range(len(indx)):
        c = indx[i]
        file.write(str(c))
        file.write("\n")
    file.close()

    file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Nonmaliciousdata.txt","a")
    for i in range(len(nonMalIndx)):
        c = nonMalIndx[i]
        file.write(str(c))
        file.write("\n")
    file.close()


    

if __name__ == "__main__":main()

print("1:K-means")
print("2:Fuzzy C-means")
Algo = input("Which algorithm you want to execute:")
Algo = int(Algo)
if(Algo == 1):

    for i in range(0,5):


        print("Execution number:{}".format(i))
        exec(open("kmeanscluster.py").read())
        # print(kp.Detection_ratio)
        # print(kp.False_Detection_ratio)
        
    Detection_ratio=[]
    filepath56 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\DetectionRatio.txt'
    with open(filepath56) as fw:
        for line in fw:
            Detection_ratio.append(line.strip())
        
    print(len(Detection_ratio))
    for m in range(len(Detection_ratio)):
        Detection_ratio[m] = float(Detection_ratio[m])

    print(Detection_ratio)  

    False_Detection_ratio=[]
    filepath57 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\FalseDetectionRatio.txt'
    with open(filepath57) as fd:
        for line in fd:
            False_Detection_ratio.append(line.strip())
        
    print(len(False_Detection_ratio))
    for m in range(len(False_Detection_ratio)):
        False_Detection_ratio[m] = float(False_Detection_ratio[m])

    print(False_Detection_ratio)


    total=0
    total1=0

    for i in range(0,len(Detection_ratio)):
        total=total+Detection_ratio[i]


    avgDR=0

    avgDR=total/len(Detection_ratio)

    print("\n\n\n")
    print("The average detection ratio is:{} % \n ".format(avgDR))


    for i in range(0,len(False_Detection_ratio)):
        total1=total1+False_Detection_ratio[i]



    avgFDR=0

    avgFDR=total1/len(False_Detection_ratio)
    print("The average false detection ratio is:{} % \n ".format(avgFDR))

    
else:
    for i in range(0,5):
    

        print("Execution number:{}".format(i))
        exec(open("copyfuzzy2.py").read())
        # print(kp.Detection_ratio)
        # print(kp.False_Detection_ratio)
        
    Detection_ratio=[]
    filepath56 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\DetectionRatio_fuzzy.txt'
    with open(filepath56) as fw:
        for line in fw:
            Detection_ratio.append(line.strip())
        
    print(len(Detection_ratio))
    for m in range(len(Detection_ratio)):
        Detection_ratio[m] = float(Detection_ratio[m])
    print(Detection_ratio)  

    False_Detection_ratio=[]
    filepath57 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\FalseDetectionRatio_fuzzy.txt'
    with open(filepath57) as fd:
        for line in fd:
            False_Detection_ratio.append(line.strip())
        
    print(len(False_Detection_ratio))
    for m in range(len(False_Detection_ratio)):
        False_Detection_ratio[m] = float(False_Detection_ratio[m])

    print(False_Detection_ratio)


    total=0
    total1=0

    for i in range(0,len(Detection_ratio)):
        total=total+Detection_ratio[i]


    avgDR=0

    avgDR=total/len(Detection_ratio)

    print("\n\n\n")
    print("The average detection ratio is:{} % \n ".format(avgDR))


    for i in range(0,len(False_Detection_ratio)):
        total1=total1+False_Detection_ratio[i]



    avgFDR=0

    avgFDR=total1/len(False_Detection_ratio)
    print("The average false detection ratio is:{} % \n ".format(avgFDR))

    




    


 
