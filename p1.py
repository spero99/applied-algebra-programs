s = raw_input("dwse meta8esh\n")
meta8esh = map(int, s.split())
print(meta8esh)
length=len(meta8esh)
print("to mhkos ths meta8eshs einai:"+str(len(meta8esh)))
antistrofh=[]
for i in range(length):
    antistrofh.append(i+1)
print(antistrofh)
for i in range(length):
    antistrofh[i][1]=meta8esh[i]
print (antistrofh)
