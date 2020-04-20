# a=("name","Ahmad","age",23,"phone",[9989886455,9100943495],"account no",
# 50100159564066,"address","14-20-556/2")
# print(a)
# print(a[2])
# print(dir(tuple))
# print(a.count("name"))
# print(a[1])
# print(a[5][1])   nested indexing
# a[5][1]=77888554455 updating the list inside the tuple
# print(a)
# a=(9999999999,66666666,4444444444,5555555,464646464)
# b[]
# for b in a:
#     if len(b)==10:
#         print(b)
#     else:
#         print(a)
# a=("name","Ahmad","age",23,"phone",[9989886455,9100943495],"account no")
# print(a[5][1]) nested indexing
# print(a[0:4])
# print(a[-1:-5:-1]) reverse indexing
# print(a.index("phone"))
# print(a.count("age"))
# b=(32,5,6,2)
# print(a+b)  concatination
# c=a+b          concatination
# print(c)
# c=b*2   concatenation
# print(c)
# print(b*2)  concatenation

a=("name","Ahmad","age",23,"phone",[9989886455,9100943495],"account no")
# if the elment inside the tuple is a mutuable datatype. 
# It is possible to make changes to that particular datatype value... 
# a[5].append(300300100)   
# print(a)
# a[0]="ramesh"     tuple is immutable 
# print(a)
# print(list(a))   we can convert the given tuple into string
# b=a
# print(b)
b=[]
for j in a:
    a.append(b)
    print(b)