#using python 3.6
#p17095-applied algebra program no.3


print ("dwse mhtres ABCDE mia ana grammh(px. 3x3)")
mhtres=[]
numbers=[]
for i in range(5):
    given=raw_input("")
    mhtres.append(map(int, given.split("x")))
print("oi mhtres einai :"+str(mhtres))                                          #testline

count=0
def synarthsh(nunbers):
    max=0
    n=0
    m=0
    count=0
    help1=0
    help2=0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
             if numbers[i][1]==numbers[j][0] and numbers[j][0]>max:
                max=numbers[j][0]
                n=numbers[i][0]
                m=numbers[j][1]
                help1=i
                help2=j
    numbers.remove(numbers[help1])
    numbers.remove(numbers[help2])
    numbers.append([n,m])
    count=(n*max*m)+count
    return numbers,count

while len(numbers)!=1:
    synarthsh(numbers)
print("h mhtra einai:"+ str(numbers) )
print("oi pol/smoi pou xreiasthkan einai :"+str(count))
