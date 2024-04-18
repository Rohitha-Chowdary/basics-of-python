word=input()
print(word)
n=len(word)
print(n)
store=dict()
print(store)
store['p']=12
store['s']=9
store['t']=8
store['s']=9
store['q']="abcf"
store["store"]=5
print(store)
keys=store.keys()
print(keys)
for ele in keys:
    print(ele,store[ele])
