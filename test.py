import pickle
#data = [{'name': 'Alice', 'age': 30, 'city': 'New York'}]
c = {a,b}

#with open('Robert_local/data.pkl', 'wb') as f:
#    pickle.dump(data, f)
with open('Robert_local/data.pkl', 'wb')  as a:
    pickle.dump(c.append, a)
with open("Robert_local/data.pkl", 'rb') as m:
    n = pickle.load(m)
print(n)