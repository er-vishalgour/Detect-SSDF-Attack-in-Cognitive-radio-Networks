import math as mt
from random import randint
import time

new=[]
datalist=[]
datalistf=[]
detected=[]
non_detected=[]
Detection_ratio=0
False_Detection_ratio=0


filepath = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\dataset2.txt'
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
print(len(new))
for i in range(0,len(new)):
    datalistf.append(new[i])
# for i in range(len(datalistf)):
#     print(i)
#     print(datalistf[i]) 



SR=0
ER=20
TS=20
ABT=ER-1


malicious=[]
filepath1 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Maliciousdata1.txt'
with open(filepath1) as fw:
    for line in fw:
        malicious.append(line.strip())
    
malicious.sort()
for m in range(len(malicious)):
    malicious[m] = int(malicious[m])




Non_malicious=[]
filepath2 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Nonmaliciousdata.txt'
with open(filepath2) as fz:
    for line in fz:
        Non_malicious.append(line.strip())

Non_malicious.sort()
for m in range(len(Non_malicious)):
    Non_malicious[m] = int(Non_malicious[m])



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

centroid_1 = x
centroid_2 = y
print("{},{}".format(centroid_1,centroid_2))
m = 2
c = 2
n = m-1
p = 2/n


A = datalistf[centroid_1]
B = datalistf[centroid_2]
print("\n")
print("centroid_1")
print(A)
print("\n")
print("centroid_2")
print(B)
print("\n")
x_list = []
y_list = []
final_listx = []
final_listy = []
for i in range(0,len(datalistf)):
    
    for j in range(0,TS):
        anum1 = int(str(datalistf[i][j]))
        anum2 = int(str(datalistf[centroid_1][j]))
        adeno1 = int(str(datalistf[i][j]))
        adeno2 =int(str(datalistf[centroid_1][j]))
        bnum1 = int(str(datalistf[i][j]))
        bnum2 = int(str(datalistf[centroid_1][j]))
        bdeno1 = int(str(datalistf[i][j]))
        bdeno2 = int(str(datalistf[centroid_2][j]))
        numa = (anum1-anum2)**2
        sq1 = mt.sqrt(numa)
        denoa = (adeno1-adeno2)**2
        sq2 = mt.sqrt(denoa)
        if(denoa==0):
            diva = 1
        else:
            diva = sq1/sq2
        a = pow(diva,2)
        numb = (bnum1-bnum2)**2
        sq3 = mt.sqrt(numb)
        denob = (bdeno1-bdeno2)**2
        sq4 = mt.sqrt(denob)
        if(denob==0):
            divb = 1
        else:
            
            divb = sq3/sq4
        b = pow(divb,2)
        res = a+b 
        x_list.append(res)
    s = sum(x_list)
    x_list.clear()
    membership_value = 1/s
    
    final_listx.append(membership_value)

print("The membership value of all users with centroid_1 are:")
print(final_listx)
    

for i in range(0,len(datalistf)):
    
    for j in range(0,TS):
        anum1 = int(str(datalistf[i][j]))
        anum2 = int(str(datalistf[centroid_2][j]))
        adeno1 = int(str(datalistf[i][j]))
        adeno2 =int(str(datalistf[centroid_1][j]))
        bnum1 = int(str(datalistf[i][j]))
        bnum2 = int(str(datalistf[centroid_2][j]))
        bdeno1 = int(str(datalistf[i][j]))
        bdeno2 = int(str(datalistf[centroid_2][j]))
        numa = (anum1-anum2)**2
        sq1 = mt.sqrt(numa)
        denoa = (adeno1-adeno2)**2
        sq2 = mt.sqrt(denoa)
        if(denoa==0):
            diva = 1
        else:
            diva = sq1/sq2
        a = pow(diva,2)
        numb = (bnum1-bnum2)**2
        sq3 = mt.sqrt(numb)
        denob = (bdeno1-bdeno2)**2
        sq4 = mt.sqrt(denob)
        if(denob==0):
            divb = 1
        else:
            
            divb = sq3/sq4
        b = pow(divb,2)
        res = a+b 
        y_list.append(res)
    s = sum(y_list)
    y_list.clear()
    membership_value = 1/s

    final_listy.append(membership_value)

print("\nThe membership value of all users with centroid_2 are:")
print(final_listy)


percentage_list1 = []
percentage_list2 = []
for i in range(len(final_listx)):
    percentage1 = final_listx[i]*100
    percentage_list1.append(percentage1)

for i in range(len(final_listy)):
    percentage2 = final_listy[i]*100
    percentage_list2.append(percentage2)


numerator1 = []
numerator2 = []
for i in range(len(percentage_list1)):
    power1 = pow(percentage_list1[i], 2)
    
    numerator1.append(power1)


for i in range(len(percentage_list2)):
    power2 = pow(percentage_list2[i], 2)
    
    numerator2.append(power2)


final_numerator1 = []
final_numerator2 = []
s_list1 = []
s_list2 = []
for i in range(len(numerator1)):
    
    for j in range(TS):
        mul1 = numerator1[i]*int(str(datalistf[i][j]))
        s_list1.append(mul1)
    sum_mul1 = sum(s_list1)
    s_list1.clear()
    denoc1 = sum_mul1/sum(numerator1)
    final_numerator1.append(denoc1)
print("The updated Centroid 1 is:")
print(final_numerator1)

for i in range(len(numerator2)):
    
    for j in range(TS):
        mul2 = numerator2[i]*int(str(datalistf[i][j]))
        s_list2.append(mul2)
    sum_mul2 = sum(s_list2)
    s_list2.clear()
    denoc2 = sum_mul2/sum(numerator2)
    final_numerator2.append(denoc2)
print("The updated Centroid 2 is:")
print(final_numerator2)


d11 = []
d22 = []

for i in range(0,len(datalistf)):
    res1 = 0 
    for j in range(0,TS):
        a1 = final_numerator1[j]
        b1 = int(str(datalistf[i][j]))
        c1 = a1-b1
        d1 = c1 ** 2
        res1 = res1 + d1
    res2 = mt.sqrt(res1)
    
    d11.append(res2)

for i in range(0,len(datalistf)):
    res1 = 0 
    for j in range(0,TS):
        a1 = final_numerator2[j]
        b1 = int(str(datalistf[i][j]))
        c1 = a1-b1
        d1 = c1 ** 2

        res1 = res1 + d1
    res2 = mt.sqrt(res1)
    
    d22.append(res2)




cluster1 = []
cluster2 = []

for i in range(0,len(final_listx)):
    if(final_listx[i]<final_listy[i]):
        cluster1.append(i)
    elif(final_listx[i]>final_listy[i]):
        cluster2.append(i)

    else:
        if final_listx[i-1] in cluster1:
                cluster1.append(i)
        else:
                cluster2.append(i)




print("The clusters are:")
print(cluster1)
print(len(cluster1))
print(cluster2)
print(len(cluster2))
count = 1

while True:
    x_list1 = []
    y_list1 = []
    final_listx1 = []
    final_listy1 = []
    for i in range(0,len(datalistf)):
        
        for j in range(0,TS):
            anum1 = int(str(datalistf[i][j]))
            anum2 = float(str(final_numerator1[j]))
            adeno1 = int(str(datalistf[i][j]))
            adeno2 = float(str(final_numerator1[j]))
            bnum1 = int(str(datalistf[i][j]))
            bnum2 = float(str(final_numerator1[j]))
            bdeno1 = int(str(datalistf[i][j]))
            bdeno2 = float(str(final_numerator2[j]))
            numa = (anum1-anum2)**2
            sq1 = mt.sqrt(numa)
            denoa = (adeno1-adeno2)**2
            sq2 = mt.sqrt(denoa)
            if(denoa==0):
                diva = 1
            else:
                diva = sq1/sq2
            a = pow(diva,2)
            numb = (bnum1-bnum2)**2
            sq3 = mt.sqrt(numb)
            denob = (bdeno1-bdeno2)**2
            sq4 = mt.sqrt(denob)
            if(denob==0):
                divb = 1
            else:
                
                divb = sq3/sq4
            b = pow(divb,2)
            res = a+b 
            x_list1.append(res)
        s = sum(x_list1)
        x_list1.clear()
        membership_value = 1/s
        
        final_listx1.append(membership_value)

    print("The membership value of all users with centroid_1 are:")
    print(final_listx1)
    print(len(final_listx1))
        

    for i in range(0,len(datalistf)):
        
        for j in range(0,TS):
            anum1 = int(str(datalistf[i][j]))
            anum2 = float(str(final_numerator2[j]))
            adeno1 = int(str(datalistf[i][j]))
            adeno2 =float(str(final_numerator1[j]))
            bnum1 = int(str(datalistf[i][j]))
            bnum2 = float(str(final_numerator2[j]))
            bdeno1 = int(str(datalistf[i][j]))
            bdeno2 = float(str(final_numerator2[j]))
            numa = (anum1-anum2)**2
            sq1 = mt.sqrt(numa)
            denoa = (adeno1-adeno2)**2
            sq2 = mt.sqrt(denoa)
            if(denoa==0):
                diva = 1
            else:
                diva = sq1/sq2
            a = pow(diva,2)
            numb = (bnum1-bnum2)**2
            sq3 = mt.sqrt(numb)
            denob = (bdeno1-bdeno2)**2
            sq4 = mt.sqrt(denob)
            if(denob==0):
                divb = 1
            else:
                
                divb = sq3/sq4
            b = pow(divb,2)
            res = a+b 
            y_list1.append(res)
        s = sum(y_list1)
        y_list1.clear()
        membership_value = 1/s
        
        final_listy1.append(membership_value)

    print("\nThe membership value of all users with centroid_2 are:")
    print(final_listy1)
    print(len(final_listy1))


    percentage_list3 = []
    percentage_list4 = []
    for i in range(len(final_listx1)):
        percentage1 = final_listx1[i]*100
        percentage_list3.append(percentage1)

    for i in range(len(final_listy1)):
        percentage2 = final_listy1[i]*100
        percentage_list4.append(percentage2)

    
    numerator3 = []
    numerator4 = []
    for i in range(len(percentage_list3)):
        power1 = pow(percentage_list3[i], 2)

        numerator3.append(power1)


    for i in range(len(percentage_list4)):
        power2 = pow(percentage_list4[i], 2)
        
        numerator4.append(power2)


    final_numerator3 = []
    final_numerator4 = []
    s_list3 = []
    s_list4 = []
    for i in range(len(numerator3)):
        
        for j in range(TS):
            mul1 = numerator3[i]*int(str(datalistf[i][j]))
            s_list3.append(mul1)
        sum_mul1 = sum(s_list3)
        s_list3.clear()
        denoc1 = sum_mul1/sum(numerator3)
        final_numerator3.append(denoc1)
    print("The updated Centroid 1 is:")
    print(final_numerator3)

    for i in range(len(numerator4)):
        
        for j in range(TS):
            mul2 = numerator4[i]*int(str(datalistf[i][j]))
            s_list4.append(mul2)
        sum_mul2 = sum(s_list4)
        s_list4.clear()
        denoc2 = sum_mul2/sum(numerator4)
        final_numerator4.append(denoc2)
    print("The updated Centroid 2 is:")
    print(final_numerator4)

    d33=[]
    d44=[]

    for i in range(0,len(datalistf)):
        res1 = 0 
        for j in range(0,TS):
            a1 = final_numerator3[j]
            b1 = int(str(datalistf[i][j]))
            c1 = a1-b1
            d1 = c1 ** 2

            res1 = res1 + d1
        res2 = mt.sqrt(res1)
        
        d33.append(res2)

    for i in range(0,len(datalistf)):
        res1 = 0 
        for j in range(0,TS):
            a1 = final_numerator4[j]
            b1 = int(str(datalistf[i][j]))
            c1 = a1-b1
            d1 = c1 ** 2
            
            res1 = res1 + d1
        res2 = mt.sqrt(res1)
         
        d44.append(res2)
  


    cluster3 = []
    cluster4 = []

    for i in range(0,len(final_listx1)):
        if(final_listx1[i]<final_listy1[i]):
            cluster3.append(i)
        elif(final_listx1[i]>final_listy1[i]):
            cluster4.append(i)

        else:
            if final_listx1[i-1] in cluster3:
                    cluster3.append(i)
            else:
                    cluster4.append(i)

    
    

    end1 = []
    end2 = []
    for  i in range(len(final_listx1)):
        dif1 = final_listx1[i] - final_listx[i]
        dif1_abs = abs(dif1)
        end1.append(dif1_abs)

    for  i in range(len(final_listy1)):
        dif1 = final_listy1[i] - final_listy[i]
        dif1_abs = abs(dif1)
        end2.append(dif1_abs)

    print(cluster3)
    print(cluster4)

    # if((final_listx1==final_listx) & (final_listy1==final_listy)):
    #     count = 0 
    # else:
    #     count = count + 1

    # if(count==0):
    #     print("Complete")
    #     break
    # else:
    #     del final_listx
    #     del final_listy
    #     final_listx = []
    #     final_listy = []
    #     final_listx = final_listx1
    #     final_listy = final_listy1


    
    sum_end1 = sum(end1)
    print(sum_end1)
    sum_end2 = sum(end2)
    print(sum_end2)

    a=len(malicious)
    if((sum_end1<0.5) & (sum_end2<0.5)):
        count = 0 
    else:
        count = count + 1

    if(count==0):
        print("Complete")
        time.sleep(1)
        print(x)
        print(y)
        break
    else:
        del final_listx
        del final_listy
        final_listx = []
        final_listy = []
        final_listx = final_listx1
        final_listy = final_listy1


ct = 0

war=any(elem in cluster3 for elem in malicious)
for i in range(0,len(cluster3)):
    for j in range(0,len(malicious)):
        if(cluster3[i] == malicious[j]):
            ct += 1

half_malicious = len(malicious)/2
if(ct >= half_malicious):
    print("The malicious cluster is:\n {} ".format(cluster3))
    print("The non malicious cluster is:\n {}".format(cluster4))
    for itm in cluster3:
        for itm1 in malicious:
            if(itm==itm1):
                detected.append(itm)
    for item in cluster3:
        for item1 in Non_malicious:
            if(item==item1):
                non_detected.append(item)
    Detection_ratio=float((len(detected)/len(malicious)))
    Detection_ratio=float(Detection_ratio)
    print("The Detection ratio is {} % ".format(Detection_ratio))



    False_Detection_ratio=float((len(non_detected)/len(Non_malicious)))
    False_Detection_ratio=float(False_Detection_ratio)
    print("The False Detection ratio is {} % \n".format(False_Detection_ratio))            
    
    print("The number of malicious users detected:\n {}".format(detected))
    print(len(detected))
    print("The number of non malicious users detected as malicious:\n {}".format(non_detected))
    print(len(non_detected))


else:
    print("The malicious cluster is:\n {}".format(cluster4))
    print("The non malicious cluster is:\n {}".format(cluster3))
    for itm in cluster4:
        for itm1 in malicious:
            if(itm==itm1):
                detected.append(itm)
    
    for item in cluster4:
        for item1 in Non_malicious:
            if(item==item1):
                non_detected.append(item)
    
    Detection_ratio=float((len(detected)/len(malicious)))
    Detection_ratio=float(Detection_ratio)
    print("The Detection ratio is {} % ".format(Detection_ratio))



    False_Detection_ratio=float((len(non_detected)/len(Non_malicious)))
    False_Detection_ratio=float(False_Detection_ratio)
    print("The False Detection ratio is {} % \n".format(False_Detection_ratio))
    
    print("The number of malicious users detected:\n {}".format(detected))
    print(len(detected))
    print("The number of non malicious users detected as malicious:\n {}".format(non_detected))
    print(len(non_detected))


print("The length of cluster3 is: ")
print(len(cluster3))
print("The length of cluster4 is: ")
print(len(cluster4))     



file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\DetectionRatio_fuzzy.txt","a")
file.write(str(Detection_ratio))
file.write("\n")
file.close()

file = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\FalseDetectionRatio_fuzzy.txt","a")
file.write(str(False_Detection_ratio))
file.write("\n")
file.close()
