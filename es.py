# filepath = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\untitled.txt'
# with open(filepath) as fp:
#     content=fp.readlines()
#     content[line].split(',')
# print(content)



filepath = 'C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\untitled.txt'
data = [line.strip() for line in open("C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\untitled.txt",'r')]
for i in data:
    print(i)



# import csv
# file='C:\\Users\\USER\\Desktop\\Final Year Group Project\\finalyearproject\\Untitled-2.csv'
# with open(file) as csvfile:
#     reader=csv.reader(file , delimiter=',')
#     for line in reader:
#         print(','.join(line))