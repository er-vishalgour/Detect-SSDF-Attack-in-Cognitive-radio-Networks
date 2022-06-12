import io
Primaryuser=[]
filepath1 = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\PrimaryUser.txt'
with open(filepath1) as fw:
    for line in fw:
        Primaryuser.append(line.strip())

print(len(Primaryuser))
for m in range(len(Primaryuser)):
    Primaryuser[m] = int(Primaryuser[m])

print(Primaryuser)

# datalist=[]
# datalistf=[]
# bi=['0','1']
# filepath = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\sensingreport.txt'
# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        data=[]
#        print("Line {}: {}".format(cnt, line.strip()))
#        datalist=line.strip()
#        for s in datalist:
#            if s in bi:
#                s = int(s)
#                data.append(s)
#            else:
#                 continue
#            datalistf.append(data)
#        line = fp.readline()
#        cnt += 1

bi=['0','1']

final=[]
f = open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\sensingreport.txt","r")
l = f.readline()
while True:
    data=[]
    for ch in l:
        if ch in bi:
            s = int(ch)
            data.append(s)
    final.append(data)
    l = f.readline()
    if not l:
        break

TS=100
# print(final)
print(len(final))

counter=[]
for i in final:
    c=0
    for e in i:
        if(e == 1):
            c+=1
    counter.append(c)
PR=[]
SR=int(input("Enter the starting range"))
ER=int(input("Enter the ending range"))
print("Primary User : Number of 1's")

for i in range(SR,ER):
    print("{}: {}       :        {}".format(i+1,Primaryuser[i],counter[i]))


Fusion_centre=[]
for i in range(SR,ER):
    PR.append(Primaryuser[i])

# print(PR)
SU=len(PR)
# print(SU)


for i in range(SR,ER):
    Busy_count=0
    for j in range(0,TS):
        if(final[i][j]==1):
            Busy_count += 1
    if(Busy_count >= TS/2 ):
        Fusion_centre.append(1)
    else:
        Fusion_centre.append(0)






print(Primaryuser)
print(Fusion_centre)
print(len(Fusion_centre))    
num_fpr=0
num_tpr=0
for i in range(len(PR)):
    if( (PR[i] == 0) & (Fusion_centre[i] == 1)  ):
        num_fpr += 1
            
     
    elif( (PR[i]==1) & (Fusion_centre[i]==1) ):
        num_tpr += 1
    else:
        continue       
print(num_fpr)
print(num_tpr)

deno_fpr=0
deno_tpr=0
for i in range(len(PR)):
    if(PR[i]==0):
        deno_fpr += 1
    elif(PR[i]==1):
        deno_tpr += 1

print(deno_fpr)
print(deno_tpr)
True_Positive_Rate=num_tpr/deno_tpr
False_Positive_Rate=num_fpr/deno_fpr
print("True positive rate is {}".format(True_Positive_Rate))
print("False positive rate is {}".format(False_Positive_Rate))