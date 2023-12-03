import pickle
print("OUTPUT-1")
# Save a variable to a file
data = {'crow': 'a bird'}
with open('data1.pkl', 'wb') as f:
    pickle.dump(data, f)
# Restore the variable from the file
with open('data1.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)
print("OUTPUT-2")
# Save a variable to a file
data = {'apple': 'a fruit'}
with open('data2.pkl', 'wb') as f:
    pickle.dump(data, f)
# Restore the variable from the file
with open('data2.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)