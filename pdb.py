# s="vinod KUMAR tHupakuLa GarnimiiTTa kvpalli Chittoor Andra"
# s1=s.split()
# print(s1)
# c1=0
# c2=0
# for i in s1:
#     if i.isupper():
#         c1+=1
#     if i.islower():
#         c2+=1
# print('upper case: ',c1)
# print('lower case: ',c2)
# import pandas as pd
# a=[1,2,3,4]
# b=[5,6,7,8]
# data={"1st":a,"2nd":b}
# df=pd.DataFrame(data)
# print(df)
import pandas as pd
import csv
f=open("c:\\python37\\practice/emp.csv")
data=f.read().split()
for line in data:
       print(line,'\t',end=' ')
       print()




