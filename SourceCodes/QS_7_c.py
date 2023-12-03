
def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

print("OUTPUT-2")
d1 = {1: 'a', 2: 'b', 3: 120}
print(d1)
d2 = reverse_dict(d1)
print(d2)
print("OUTPUT-2")
d1 = {'a': 10, 'b': 20, 'c': 30}
print(d1)
d2 = reverse_dict(d1)
d2 = {v: k for k, v in d1.items()}
print(d2)