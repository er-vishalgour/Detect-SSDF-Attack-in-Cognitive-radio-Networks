from random import randint
# from tabulate import tabulate
# import pandas as pd
from random import shuffle
import os
import random






    
def main():

    


    PU = []
    P_pu=0.5
    #P_pu is probability of presence of binary user
    alpha=0.6


    mal = []
    P_fa=0.10
    P_md=0.10
    SU = []
    SU2 = []
    final = []
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
                else:
                    if(x<=P_md*100):
                        column.append(0)
                    else:
                        column.append(1)
                
            SU.append(column)

        for i in range(SEC):
            print(i)
            print(SU[i])   
   

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
            mal.append(column)    

    def always_false():

        for i in indx:
            column= []
            for j in range(0,TS):
                if(SU[i][j]==0):
                    column.append(1)
                else:
                    column.append(0)
            mal.append(column)                
            print(i)
            print(mal)    
    def random_yes():

        for i in indx:
            column=[]
            for j in range(TS):
                x=random.randint(0,100)
                if(x<=alpha*100):
                    column.append(1)
                else:
                    column.append(0)
                
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
                
            mal.append(column) 

    def random_false():

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
    elif(attack == 2):
        always_no()
        secondary_user()
    elif(attack == 3):
        secondary_user()
        always_false()
    elif(attack == 4):
        secondary_user()
        random_yes()
    elif(attack == 5):
        secondary_user()
        random_no()
    else:
        secondary_user()
        random_false()
    
    
    



    for t in range(SEC):
        final.append(None)


    
    
    
    

    

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

    for i in final:
        f = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\sensingreport.txt","a")
        f.write(str(i))
        f.write("\n")
    


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



    def Hamming_Distance(a,b):
        count=0
        for i in range(0,TS):
            if(a[i]!=b[i]):
                count=count+1
        return count
    print("Hamming distances")
    lst=[]
    for k in range(SEC):
        lst.append(k)
    # print(lst)
    distance=[]
    for i in range(0,SEC):
        # j=i
        distance2=[]
        #print(lst[i])
        for j in range(0,TS):
            ham=Hamming_Distance(final[i],final[j])
            distance2.append(ham)
            #print(ham)

            f = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\dataset1.txt","a")
            f.write(str(distance2[j]))
            if(j!=99):
                f.write(",")
            

            
        f.write("\n")


        distance.append(distance2)
        # df =pd.DataFrame(ham)
        # print(df)   
        
        # print("next")
    print('  {}'.format(lst))
    for i in range(0,SEC):
        print('{} {}' .format(lst[i], distance[i]))
if __name__ == "__main__":main()