#using python 3.6
#p17095-applied algebra program no.2
import random,itertools

def lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
length=input("dwse mhkos meta8eshs:")
numbers=[]
for i in range(length):
    numbers.append(i)
syndyasmoi=list(itertools.combinations(numbers,2))
print("oi dyo kykloi mporoyn na xoyn mhkos"+str(syndyasmoi))                         #testline
kykloi=[]
for i in range(len(syndyasmoi)):
    sum=0
    for j in range(2):
        sum += syndyasmoi[i][j]
    #print(sum)
    if sum==length:
        kykloi.append(syndyasmoi[i])
print ("oi 3enoi kykloi einai "+str(kykloi))                                         #testline
ta3eis=[]
for i in range(len(kykloi)):
    x=kykloi[i][0]
    y=kykloi[i][1]
    ta3eis.append(lcm(x,y))

print("oi tajeis poy yparxoyn:"+str(ta3eis))                                         #testline
maxta3h=0
for i in range(len(ta3eis)):
    if ta3eis[i]>maxta3h:
        maxta3h=ta3eis[i]

print("h megisth ta3h einai:"+str(maxta3h))
