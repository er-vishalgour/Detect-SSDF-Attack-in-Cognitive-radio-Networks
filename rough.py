# import math as mt
# final_listx1 = [0.11,0.91,1.23,4.65,0.009,0.22]
# final_listx  = [0.23,0.45,0.67,0.89,0.21,0.26]

# final_listy1 = [1,2,3,4,5,6]
# final_listy = [7,8,9,10,11,12]

# end1 = []
# end2 = []
# for  i in range(len(final_listx1)):
#     dif1 = final_listx1[i] - final_listx[i]
#     dif1_abs = abs(dif1)
#     end1.append(dif1_abs)

# for  i in range(len(final_listy1)):
#     dif1 = final_listy1[i] - final_listy[i]
#     dif1_abs = abs(dif1)
#     end2.append(dif1_abs)

# sum_end1 = sum(end1)
# print(sum_end1)
# sum_end2 = sum(end2)
# print(sum_end2)


# datalistf=[[1,6],[2,5],[3,8],[4,4],[5,7],[6,9]]
# c1 = [0.8,0.9,0.7,0.3,0.5,0.2]
# c2 = [0.2,0.1,0.3,0.7,0.5,0.8]
# c11=[]
# c22=[]

# def step1(c1,c2,datalistf):
 

#     for i in range(len(datalistf)):
#         res=0
#         for j in range(len(c1)):
#             s=c1[j]
#             a=int(datalistf[s][i])
#             res1 = a*s
#             res = res + res1
#         c11.append(res)
#     d33=[]
#     d44=[]

#     for i in range(0,len(datalistf)):
#         res1 = 0 
#         for j in range(0,2):
#             a1 = final_numerator3[j]
#             b1 = int(str(datalistf[i][j]))
#             c1 = a1-b1
#             d1 = c1 ** 2

#             res1 = res1 + d1
#         res2 = mt.sqrt(res1)
#         res3 = round(res2,2)
#         d33.append(res3)

#     for i in range(0,len(datalistf)):
#         res1 = 0 
#         for j in range(0,2):
#             a1 = final_numerator4[j]
#             b1 = int(str(datalistf[i][j]))
#             c1 = a1-b1
#             d1 = c1 ** 2
            
#             res1 = res1 + d1
#         res2 = mt.sqrt(res1)
#         res3 = round(res2,2)    
#         d44.append(res3)
#     print("distance1:{}".format(d33))
#     print("distance2:{}".format(d44))


# if __name__ == '__main__':
    
    
#     datalistf=[[1,6],[2,5],[3,8],[4,4],[5,7],[6,9]]
#     c1 = [0.8,0.9,0.7,0.3,0.5,0.2]
#     c2 = [0.2,0.1,0.3,0.7,0.5,0.8]
#     c11=[]
#     c22=[]
    
#     step1(c1,c2,datalistf)
#     print(c11)
    
datalistf = [[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]]
final_listx = [0.0122,0,0.0200,0.1000,0.2647,0.5000,0.7353,0.9000,0.9800,1.0000]


percentage_list1 = []
percentage_list2 = []
for i in range(len(final_listx)):
    percentage1 = final_listx[i]*100
    percentage_list1.append(percentage1)


print(percentage_list1)

numerator1 = []
numerator2 = []
for i in range(len(percentage_list1)):
    power1 = pow(percentage_list1[i], 2)
    
    numerator1.append(power1)



final_numerator1 = []
final_numerator2 = []
s_list1 = []
s_list2 = []
d_list1 = []
d_list2 = []
print(sum(numerator1))
for i in range(len(numerator1)):
    
    for j in range(0,1):
        mul1 = numerator1[i]*datalistf[i][j]
        s_list1.append(mul1)
    sum_mul1 = sum(s_list1)
    print(sum_mul1)
    s_list1.clear()
    
    denoc1 = sum_mul1/sum(numerator1)
    final_numerator1.append(denoc1)
print("The updated Centroid 1 is:")
print(final_numerator1)