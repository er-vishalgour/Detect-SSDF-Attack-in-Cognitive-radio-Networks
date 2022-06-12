import math as mt

new=[]
datalist=[]
datalistf=[]


filepath = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\data.txt'
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
for i in range(len(datalistf)):
    print(i)
    print(datalistf[i]) 

# list_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

centroid_1 = 10
centroid_2 = 16
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
    
    for j in range(0,len(datalistf)):
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
    
    for j in range(0,len(datalistf)):
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
    round1 = round(power1,3)
    numerator1.append(round1)


for i in range(len(percentage_list2)):
    power2 = pow(percentage_list2[i], 2)
    round2 = round(power2,3)
    numerator2.append(round2)


final_numerator1 = []
final_numerator2 = []
s_list1 = []
s_list2 = []
for i in range(len(numerator1)):
    
    for j in range(len(datalistf)):
        mul1 = numerator1[i]*int(str(datalistf[i][j]))
        s_list1.append(mul1)
    sum_mul1 = sum(s_list1)
    s_list1.clear()
    denoc1 = sum_mul1/sum(numerator1)
    final_numerator1.append(denoc1)
print("The updated Centroid 1 is:")
print(final_numerator1)

for i in range(len(numerator2)):
    
    for j in range(len(datalistf)):
        mul2 = numerator2[i]*int(str(datalistf[i][j]))
        s_list2.append(mul2)
    sum_mul2 = sum(s_list2)
    s_list2.clear()
    denoc2 = sum_mul2/sum(numerator2)
    final_numerator2.append(denoc2)
print("The updated Centroid 2 is:")
print(final_numerator2)

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
print(cluster2)
count = 1

while True:
    x_list = []
    y_list = []
    final_listx = []
    final_listy = []
    for i in range(0,len(datalistf)):
        
        for j in range(0,len(datalistf)):
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
            denoa = (adeno1-adeno2)
            sq2 = mt.sqrt(denob)
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
        
        for j in range(0,len(datalistf)):
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
            denoa = (adeno1-adeno2)
            sq2 = mt.sqrt(denob)
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
        round1 = round(power1,3)
        numerator1.append(round1)


    for i in range(len(percentage_list2)):
        power2 = pow(percentage_list2[i], 2)
        round2 = round(power2,3)
        numerator2.append(round2)


    final_numerator3 = []
    final_numerator4 = []
    s_list1 = []
    s_list2 = []
    for i in range(len(numerator1)):
        
        for j in range(len(datalistf)):
            mul1 = numerator1[i]*int(str(datalistf[i][j]))
            s_list1.append(mul1)
        sum_mul1 = sum(s_list1)
        s_list1.clear()
        denoc1 = sum_mul1/sum(numerator1)
        final_numerator3.append(denoc1)
    print("The updated Centroid 1 is:")
    print(final_numerator3)

    for i in range(len(numerator2)):
        
        for j in range(len(datalistf)):
            mul2 = numerator2[i]*int(str(datalistf[i][j]))
            s_list2.append(mul2)
        sum_mul2 = sum(s_list2)
        s_list2.clear()
        denoc2 = sum_mul2/sum(numerator2)
        final_numerator4.append(denoc2)
    print("The updated Centroid 2 is:")
    print(final_numerator4)

    cluster3 = []
    cluster4 = []

    for i in range(0,len(final_listx)):
        if(final_listx[i]<final_listy[i]):
            cluster3.append(i)
        elif(final_listx[i]>final_listy[i]):
                cluster4.append(i)

        else:
            if final_listx[i-1] in cluster1:
                    cluster3.append(i)
            else:
                    cluster4.append(i)

    print("The clusters are:")
    print(cluster3)
    print(len(cluster3))
    print(cluster4)
    print(len(cluster4))

    if((cluster1==cluster3) & (cluster2==cluster4)):
        count = 0 
    else:
        count = count + 1

    if(count==0):
        print("Complete")
        break
    else:
        del cluster1
        del cluster2
        cluster1 = []
        cluster2 = []
        cluster1 = cluster3
        cluster2 = cluster4