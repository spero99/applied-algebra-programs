#using python 3.6
#p17095-applied algebra program no.1



s = raw_input("dwse meta8esh\n")
given=[]
given.append(map(int, s.split()))
print(given)
length=len(given[0])
print("to mhkos ths meta8eshs einai:"+str(length))


meta8esh=[]
for i in range(length):
    meta8esh.append([i+1,0])
print(meta8esh)
for j in range(length):
    help1=given[0][j]
    meta8esh[j][1].append(help1)
print (meta8esh)
#def BresAntistrofh(met8esh):
'''antistrofh=[]
for i in range(length):
    help2=meta8esh[i][1]
    antistrofh[help2].append(i)
print (str(antistrofh.join(" ")))
#print ("h antistrofh einai:"+BresAntistrofh(meta8esh))
'''
