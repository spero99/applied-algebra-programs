#using python 3.6
#p17095-applied algebra program no.3


print ("dwse mhtres ABCDE mia ana grammh(px. 3x3)")

numbers=[]
for i in range(5):
    given=raw_input("")
    numbers.append(map(int, given.split("x")))
print("oi mhtres einai :"+str(numbers))                                          #testline


max=0
help1=0
help2=0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i][1]==numbers[j][0] and numbers[j][0]>max:
            max=numbers[j][0]
            help1=j
            help2=i
#print(max)                                                                  #testline                                                                 #testline                                                                  #testline                                                                  #testline                                                                  #testline
#print(help1)                                                                  #testline                                                                  #testline                                                                  #testline                                                                  #testline
#print (help2)                                                                  #testline                                                                  #testline                                                                  #testline
count1=numbers[help1][1]*numbers[help2][0]*max
numbers2=[]
for i in range(len(numbers)):
    if numbers[i][1]!=max and numbers[i][0]!=max:
        numbers2.append(numbers[i])
numbers2.append([numbers[help2][0],numbers[help1][1]])
#print(numbers2)                                                                  #testline                                                                  #testline
#print(count1)                                                                  #testline



#second phase
max=0
help1=0
help2=0
for i in range(len(numbers2)):
    for j in range(len(numbers2)):
        if numbers2[i][1]==numbers2[j][0] and numbers2[j][0]>max:
            max=numbers2[j][0]
            help1=j
            help2=i
#print(max)                                                                  #testline
#print(help1)                                                                  #testline                                                                  #testline
#print (help2)                                                                  #testline
count2=count1 + numbers2[help1][1]*numbers2[help2][0]*max
numbers3=[]
for i in range(len(numbers2)):
    if numbers2[i][1]!=max and numbers2[i][0]!=max:
        numbers3.append(numbers2[i])

numbers3.append(([numbers2[help2][0],numbers2[help1][1]]))
#print(numbers3)                                                                  #testline
#print(count2)                                                                  #testline                                                                  #testline

#third phase
max=0
help1=0
help2=0
for i in range(len(numbers3)):
    for j in range(len(numbers3)):
        if numbers3[i][1]==numbers3[j][0] and numbers3[j][0]>max:
            max=numbers3[j][0]
            help1=j
            help2=i
#print(max)                                                                  #testline
#print(help1)                                                                  #testline
#print (help2)                                                                  #testline
count3=count2 + numbers3[help1][1]*numbers3[help2][0]*max
numbers4=[]
for i in range(len(numbers3)):
    if numbers3[i][1]!=max and numbers3[i][0]!=max:
        numbers4.append(numbers3[i])

numbers4.append(([numbers3[help2][0],numbers3[help1][1]]))
#print(numbers4)                                                                  #testline
#print(count3)                                                                  #testline

#fouth phase
max=0
help1=0
help2=0
for i in range(len(numbers4)):
    for j in range(len(numbers4)):
        if numbers4[i][1]==numbers4[j][0] and numbers4[j][0]>max:
            max=numbers4[j][0]
            help1=j
            help2=i
#print(max)                                                                  #testline
#print(help1)                                                                  #testline
#print (help2)                                                                  #testline
count4=count3 + numbers4[help1][1]*numbers4[help2][0]*max
numbers5=[]
for i in range(len(numbers4)):
    if numbers4[i][1]!=max and numbers4[i][0]!=max:
        numbers4.append(numbers4[i])

numbers5.append(([numbers4[help2][0],numbers4[help1][1]]))
#print(numbers5)                                                                  #testline
#print(count4)


print("h mhtra einai:"+ str(numbers5) )
print("oi pol/smoi pou xreiasthkan einai :"+str(count4))
