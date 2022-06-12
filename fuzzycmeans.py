import math as mt

new=[]
datalist=[]
datalistf=[]
TS=input("Enter the number of time slots")
TS=int(TS)

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
print(len(new))
for i in range(0,len(new)):
    datalistf.append(new[i])
# for i in range(len(datalistf)):
#     print(i)
#     print(datalistf[i]) 

# list_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

centroid_1 = 5
centroid_2 = 8
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
        numa = abs(anum1-anum2)
        denoa = abs(adeno1-adeno2)
        if(denoa==0):
            diva = 1
        else:
            diva = numa/denoa
        a = pow(diva,2)
        numb = abs(bnum1-bnum2)
        denob = abs(bdeno1-bdeno2)
        if(denob==0):
            divb = 1
        else:
            
            divb = numb/denob
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
        numa = abs(anum1-anum2)
        denoa = abs(adeno1-adeno2)
        if(denoa==0):
            diva = 1
        else:
            diva = numa/denoa
        a = pow(diva,2)
        numb = abs(bnum1-bnum2)
        denob = abs(bdeno1-bdeno2)
        if(denob==0):
            divb = 1
        else:
            
            divb = numb/denob
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
    
    for j in range(0,TS):
        mul1 = numerator1[i]*int(str(datalistf[i][j]))
        s_list1.append(mul1)
    sum_mul1 = sum(s_list1)
    s_list1.clear()
    denoc1 = sum_mul1/sum(numerator1)
    final_numerator1.append(denoc1)
print("The updated Centroid 1 is:")
print(final_numerator1)

for i in range(len(numerator2)):
    
    for j in range(0,TS):
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
        e1 = mt.sqrt(d1)
        res1 = res1 + e1
    d11.append(res1)

for i in range(0,len(datalistf)):
    res1 = 0 
    for j in range(0,TS):
        a1 = final_numerator2[j]
        b1 = float(str(datalistf[i][j]))
        c1 = a1-b1
        d1 = c1 ** 2
        e1 = mt.sqrt(d1)
        res1 = res1 + e1
    d22.append(res1)




cluster1 = []
cluster2 = []

for i in range(0,len(d11)):
    if(d11[i]<d22[i]):
        cluster1.append(i)
    elif(d11[i]>d22[i]):
            cluster2.append(i)

    else:
        if d11[i-1] in cluster1:
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
            numa = abs(anum1-anum2)
            denoa = abs(adeno1-adeno2)
            if(denoa==0):
                diva = 1
            else:
                diva = numa/denoa
            a = pow(diva,2)
            numb = abs(bnum1-bnum2)
            denob = abs(bdeno1-bdeno2)
            if(denob==0):
                divb = 1
            else:
                
                divb = numb/denob
            b = pow(divb,2)
            res = a+b 
            x_list.append(res)
        s = sum(x_list)
        x_list.clear()
        membership_value = 1/s
        final_listx1.append(membership_value)

    print("The membership value of all users with centroid_1 are:")
    print(final_listx1)
        

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
            numa = abs(anum1-anum2)
            denoa = abs(adeno1-adeno2)
            if(denoa==0):
                diva = 1
            else:
                diva = numa/denoa
            a = pow(diva,2)
            numb = abs(bnum1-bnum2)
            denob = abs(bdeno1-bdeno2)
            if(denob==0):
                divb = 1
            else:
                
                divb = numb/denob
            b = pow(divb,2)
            res = a+b 
            y_list.append(res)
        s = sum(y_list)
        y_list.clear()
        membership_value = 1/s
        final_listy1.append(membership_value)

    print("\nThe membership value of all users with centroid_2 are:")
    print(final_listy1)


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
        round1 = round(power1,3)
        numerator3.append(round1)


    for i in range(len(percentage_list4)):
        power2 = pow(percentage_list4[i], 2)
        round2 = round(power2,3)
        numerator4.append(round2)


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
            a11 = final_numerator3[j]
            b11 = int(str(datalistf[i][j]))
            c11 = a11-b11
            d11 = c11 ** 2
            e11 = mt.sqrt(d11)
            res1 = res1 + e11
        d33.append(res1)

    for i in range(0,len(datalistf)):
        res1 = 0 
        for j in range(0,TS):
            a11 = final_numerator4[j]
            b11 = int(str(datalistf[i][j]))
            c11 = a11-b11
            d11 = c11 ** 2
            e11 = mt.sqrt(d11)
            res1 = res1 + e11
        d44.append(res1)



    cluster3 = []
    cluster4 = []

    for i in range(0,len(d33)):
        if(d33[i]<d44[i]):
            cluster3.append(i)
        elif(d33[i]>d44[i]):
            cluster4.append(i)

        else:
            if d33[i-1] in cluster3:
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
# for i in range(len(numerator2)):
    
#     for j in range(len(datalistf)):
#         mul2 = numerator2[i]*int(str(datalistf[i][j]))
#         s_list2.append(mul2)
#     sum_mul2 = sum_mul2+mul2
#     final_numerator2.append(sum_mul2)
# print(final_numerator2)



# deno_res1 = sum(numerator1)
# deno_res2 = sum(numerator2)

# numero_res1 = sum(final_numerator1)
# numero_res2 = sum(final_numerator2)


# new_centroid1 = numero_res1/deno_res1
# new_centroid2 = numero_res2/deno_res2



# print("The new centroids are:")
# print(new_centroid1)
# print(new_centroid2)
# for i in range(len(list_1)):
#     t1 = abs(list_1[i]-centroid_1)
#     t2 = abs(list_1[i]-centroid_2)
#     if(t1 == 0):
#         a = 1
#     else:
#         a = t1/t1

#     a2 = pow(a, p)
#     if(t2 == 0):
#         b = 1

#     else:
#         b = t1/t2

#     b2 = pow(b, p)

#     plus = a2 + b2

#     res = 1/plus

#     x_list.append(res)
# print("The items after membership matrix with centroid1 is :{}\n".format(x_list))
# for i in range(len(list_1)):
#     t1 = abs(list_1[i]-centroid_1)
#     t2 = abs(list_1[i]-centroid_2)
#     if(t1 == 0):
#         a = 1
#     else:
#         a = t2/t1

#     a2 = pow(a, p)
#     if(t2 == 0):
#         b = 1

#     else:
#         b = t2/t2

#     b2 = pow(b, p)

#     plus = a2 + b2

#     res = 1/plus

#     y_list.append(res)

# print("The items after membership matrix with centroid2 is :{}\n".format(y_list))
# percentage_list1 = []
# percentage_list2 = []
# for i in range(len(x_list)):
#     percentage1 = x_list[i]*100
#     percentage_list1.append(percentage1)

# for i in range(len(y_list)):
#     percentage2 = y_list[i]*100
#     percentage_list2.append(percentage2)


# numerator1 = []
# numerator2 = []
# for i in range(len(percentage_list1)):
#     power1 = pow(percentage_list1[i], 2)
#     numerator1.append(power1)


# for i in range(len(percentage_list2)):
#     power2 = pow(percentage_list2[i], 2)
#     numerator2.append(power2)


# final_numerator1 = []
# final_numerator2 = []

# for i in range(len(numerator1)):
#     mul1 = numerator1[i]*list_1[i]
#     final_numerator1.append(mul1)


# for i in range(len(numerator2)):
#     mul2 = numerator2[i]*list_1[i]
#     final_numerator2.append(mul2)

# deno_res1 = sum(numerator1)
# deno_res2 = sum(numerator2)

# numero_res1 = sum(final_numerator1)
# numero_res2 = sum(final_numerator2)


# new_centroid1 = numero_res1/deno_res1
# new_centroid2 = numero_res2/deno_res2



# print("The new centroids are:")
# print(new_centroid1)
# print(new_centroid2)


# d1 = []
# d2 = []

# for i in range(len(list_1)):
#     multi1 = abs(new_centroid1-list_1[i])
#     d1.append(multi1)

# for i in range(len(list_1)):
#     multi2 = abs(new_centroid2-list_1[i])
#     d2.append(multi2)
# print("The distance of new centroid c1 to item:\n{}".format(d1))
# print("The distance of new centroid c2 to item:\n{}".format(d2))


# cluster1 = []
# cluster2 = []


# for i in range(len(list_1)):
#     if(d1[i] < d2[i]):
#         cluster1.append(list_1[i])
#     else:
#         cluster2.append(list_1[i])


# print(cluster1)
# print(cluster2)

# count = 1

# while True:

#     x_list = []
#     y_list = []

#     for i in range(len(list_1)):
#         t1 = abs(list_1[i]-new_centroid1)
#         t2 = abs(list_1[i]-new_centroid2)
#         if(t1 == 0):
#             a = 1
#         else:
#             a = t1/t1

#         a2 = pow(a, p)
#         if(t2 == 0):
#             b = 1

#         else:
#             b = t1/t2

#         b2 = pow(b, p)

#         plus = a2 + b2

#         res = 1/plus

#         x_list.append(res)
#     print("The items after membership matrix with updated centroid1 is :\n{}".format(x_list))

#     for i in range(len(list_1)):
#         t1 = abs(list_1[i]-new_centroid1)
#         t2 = abs(list_1[i]-new_centroid2)
#         if(t1 == 0):
#             a = 1
#         else:
#             a = t2/t1

#         a2 = pow(a, p)
#         if(t2 == 0):
#             b = 1

#         else:
#             b = t2/t2

#         b2 = pow(b, p)

#         plus = a2 + b2

#         res = 1/plus

#         y_list.append(res)
#     print("The items after membership matrix with updated centroid2 is :\n{}".format(y_list))

#     percentage_list1 = []
#     percentage_list2 = []
#     for i in range(len(x_list)):
#         percentage1 = x_list[i]*100
#         percentage_list1.append(percentage1)

#     for i in range(len(y_list)):
#         percentage2 = y_list[i]*100
#         percentage_list2.append(percentage2)

#     numerator1 = []
#     numerator2 = []
#     for i in range(len(percentage_list1)):
#         power1 = pow(percentage_list1[i], 2)
#         numerator1.append(power1)

#     for i in range(len(percentage_list2)):
#         power2 = pow(percentage_list2[i], 2)
#         numerator2.append(power2)

#     final_numerator1 = []
#     final_numerator2 = []

#     for i in range(len(numerator1)):
#         mul1 = numerator1[i]*list_1[i]
#         final_numerator1.append(mul1)

#     for i in range(len(numerator2)):
#         mul2 = numerator2[i]*list_1[i]
#         final_numerator2.append(mul2)

#     deno_res1 = sum(numerator1)
#     deno_res2 = sum(numerator2)

#     numero_res1 = sum(final_numerator1)
#     numero_res2 = sum(final_numerator2)

#     new_centroid3 = numero_res1/deno_res1
#     new_centroid4 = numero_res2/deno_res2

#     print("The new centroids are:")
#     print(new_centroid3)
#     print(new_centroid4)
#     d1 = []
#     d2 = []

#     for i in range(len(list_1)):
#         multi1 = new_centroid3-list_1[i]
#         d1.append(multi1)

#     for i in range(len(list_1)):
#         multi2 = new_centroid4-list_1[i]
#         d2.append(multi2)
#     print(d1)
#     print(d2)

#     cluster1 = []
#     cluster2 = []
#     for i in range(len(list_1)):
#         if(d1[i] < d2[i]):
#             cluster1.append(list_1[i])
#         else:
#             cluster2.append(list_1[i])

#     print(cluster1)
#     print(cluster2)
#     if((new_centroid1 == new_centroid3) & (new_centroid2 == new_centroid4)):
#         count = 0
#     else:
#         count = 1

#     if(count == 0):
#         print("Process complete")
#         break
#     else:
#         new_centroid1 = new_centroid3
#         new_centroid2 = new_centroid4
