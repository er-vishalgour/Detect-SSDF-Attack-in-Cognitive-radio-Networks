import sys
import os
from random import randint






detected=[]
non_detected=[]
Detection_ratio=0
False_Detection_ratio=0






print("KMEANS")


new=[]
datalist=[]
datalistf=[]

filepath = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\dataset1.txt'
with open(filepath) as fp:
    
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       datalist=line.strip()
       data = datalist.split(',')
       new.append(data)
       line = fp.readline()
       cnt += 1


print("Enter the range of the users where you want to apply the algorithm")
SR=input("Enter the starting range")
SR=int(SR)
ER=input("Enter the ending range")
ER=int(ER)
# SR=0
# ER=100
for i in range(SR,ER):
    datalistf.append(new[i])
for i in range(len(datalistf)):
    print(i)
    print(datalistf[i])       
# dictionary1=[]
# d={}
# fh='C:\\Users\\USER\\Desktop\\python\\finalyearproject\\partitionData.txt'
# with open(fh) as fd:
#     for line in fd:
#         items = line.split()
#         key, values = int(items[0]), items[1:]
#         my_dict.setdefault(key, []).extend(values)
#     print(items)   


TS=60
ABT=ER-1
div=ER-SR
# print(div)
malicious=[]
filepath1 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Maliciousdata1.txt'
with open(filepath1) as fw:
    for line in fw:
        malicious.append(line.strip())
    
malicious.sort()
# print(len(malicious))
for m in range(len(malicious)):
    malicious[m] = int(malicious[m])

# print(malicious)

Non_malicious=[]
filepath2 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Nonmaliciousdata.txt'
with open(filepath2) as fz:
    for line in fz:
        Non_malicious.append(line.strip())

Non_malicious.sort()
# print(len(Non_malicious))
for m in range(len(Non_malicious)):
    Non_malicious[m] = int(Non_malicious[m])

# print(Non_malicious)



x=randint(SR,ABT)
y=x
while(y==x):
    y=randint(SR,ABT)

ab=[]
ab.append(x)
ab.append(y)
print(ab)

check=all(item in malicious for item in ab)
while(check):
    ab.clear()
    x=randint(SR,ABT)
    y=x
    while(y==x):
        y=randint(SR,ABT)
    ab.append(x)
    ab.append(y)
    print(ab)
    check=all(item in malicious for item in ab)
    
    

# set1=set(malicious)
# set2=set(ab)
# if set1.intersection(set2):
#     ab.clear()
#     x=randint(0,99)
#     y=x
#     while(y==x):
#         y=randint(0,99)
#     ab.append(x)
#     ab.append(y)
#     print(ab)
# else:
#     print("good")


        


 
A=[]
B=[]
A=datalistf[x]
print(A)
B=datalistf[y]


d1=[]
d2=[]



for i in range(SR,ER):
    res=0
    
    for j in range(0,TS):
        a=int(str(datalistf[x][j]))
        b=int(str(datalistf[i][j]))
        res=res+abs(a-b)
        # abc=res*res
    d1.append(res)



for i in range(SR,ER):
    res=0
    abc=0
    for j in range(0,TS):
        a=int(str(datalistf[y][j]))
        b=int(str(datalistf[i][j]))
        res=res+abs(a-b)
        # abc=res*res
    d2.append(res)


# print(x)
# print(y)
print(d1)
print(d2)
# print(len(d1))
# print(len(d2))


cluster1=[]
cluster2=[]


for i in range(div):
    if(d1[i]<d2[i]):
        cluster1.append(i)
    else:
        cluster2.append(i)
print("The clusters are:")
print(cluster1)
print(cluster2)
print("\n")
print(len(cluster1))
print(len(cluster2))
count=1


while True:



    centroid1=[]
    centroid2=[]



    for i in range(0,TS):
        res=0
        for j in range(0,len(cluster1)):
            s=int(str(cluster1[j]))
            a=int(str(datalistf[s][i]))
            res=res+a
        res=res/len(cluster1)
        centroid1.append(res)



    for i in range(0,TS):
        res=0
        for j in range(0,len(cluster2)):
            s=int(str(cluster2[j]))
            a=int(str(datalistf[s][i]))
            res=res+a
        res=res/len(cluster2)
        centroid2.append(res)


    print(centroid1)
    print(centroid2)
    print("Final Manhatten Distance")




    d3=[]
    d4=[]



    for i in range(SR,ER):
        res=0
        for j in range(0,TS):
            a=float(str(centroid1[j]))
            b=int(str(datalistf[i][j]))
            res=res+abs(a-b)
        d3.append(res)



    for i in range(SR,ER):
        res=0
        for j in range(0,TS):
            a=float(str(centroid2[j]))
            b=int(str(datalistf[i][j]))
            res=res+abs(a-b)
        d4.append(res) 


    print(d3)
    print(d4)


    cluster3=[]
    cluster4=[]


    for i in range(div):
        if(d3[i]<d4[i]):
            cluster3.append(i)

        elif(d3[i]>d4[i]):
            cluster4.append(i)
        else:
            if d3[i-1] in cluster3:
                cluster3.append(i)
            else:
                cluster4.append(i)

    print(cluster3)
    print(cluster4)

    if(((cluster1)==(cluster3)) &((cluster2)==(cluster4))):
        count=0
    else:
        count=count+1
    
    if(count==0):
        print("Complete")
        break
    else:
        del cluster1
        del cluster2
        cluster1=[]
        cluster2=[]
        cluster1=cluster3
        cluster2=cluster4
# print(type(cluster1))
# print(type(malicious))



war=any(elem in cluster1 for elem in malicious)
if(war):
    print("The malicious cluster is:\n {} ".format(cluster1))
    print("The non malicious cluster is:\n {}".format(cluster2))
    for itm in cluster1:
        for itm1 in malicious:
            if(itm==itm1):
                detected.append(itm)
    for item in cluster1:
        for item1 in Non_malicious:
            if(item==item1):
                non_detected.append(item)
    Detection_ratio=int((len(detected)/len(cluster1))*100)
    Detection_ratio=float(Detection_ratio)
    print("The Detection ratio is {} % ".format(Detection_ratio))



    False_Detection_ratio=int((len(non_detected)/len(Non_malicious))*100)
    False_Detection_ratio=float(False_Detection_ratio)
    print("The False Detection ratio is {} % \n".format(False_Detection_ratio))            
    
    print("The number of malicious users detected:\n {}".format(detected))
    print(len(detected))
    print("The number of non malicious users detected as malicious:\n {}".format(non_detected))
    print(len(non_detected))


else:
    print("The malicious cluster is:\n {}".format(cluster2))
    print("The non malicious cluster is:\n {}".format(cluster1))
    for itm in cluster2:
        for itm1 in malicious:
            if(itm==itm1):
                detected.append(itm)
    
    for item in cluster2:
        for item1 in Non_malicious:
            if(item==item1):
                non_detected.append(item)
    
    Detection_ratio=int((len(detected)/len(cluster2))*100)
    Detection_ratio=float(Detection_ratio)
    print("The Detection ratio is {} % ".format(Detection_ratio))



    False_Detection_ratio=int((len(non_detected)/len(Non_malicious))*100)
    False_Detection_ratio=float(False_Detection_ratio)
    print("The False Detection ratio is {} % \n".format(False_Detection_ratio))
    
    print("The number of malicious users detected:\n {}".format(detected))
    print(len(detected))
    print("The number of non malicious users detected as malicious:\n {}".format(non_detected))
    print(len(non_detected))


print("The length of cluster1 is: ")
print(len(cluster1))
print("The length of cluster2 is: ")
print(len(cluster2))     









file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\DetectionRatio.txt","a")
file.write(str(Detection_ratio))
file.write("\n")
file.close()

file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\FalseDetectionRatio.txt","a")
file.write(str(False_Detection_ratio))
file.write("\n")
file.close()
   


# for i in range(10):
#     exec(open("kmeanscluster.py").read())




        



    








